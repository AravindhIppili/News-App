from ..Connectors.Mysql import MySQLConnector
from ..BaseClass import ModelBase
import logging
from typing import Any
from sqlalchemy import func, or_


logger = logging.getLogger()


class MySqlServiceBase(MySQLConnector, ModelBase):
    __abstract__ = True

    def __init__(self, model: ModelBase = None, *args, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)

    def create(self, **data) -> Any:
        """To be used to create resource"""
        db_obj = self.model(**data)
        with self.session() as session:
            session.add(db_obj)
            session.commit()
            session.refresh(db_obj)

        return db_obj

    def get(self, **filter_args: dict) -> Any:
        """To be used to get one resource"""
        logger.debug(f"Filter args : {filter_args}")
        with self.session() as session:
            return session.query(self.model).filter_by(**filter_args).first()

    def applyFilters(
        self,
        query,
        model,
        group_by=None,
        offset: int = None,
        limit: int = None,
        order_by=None,
        **filter_args: dict,
    ):
        for filter_key, filter_value in filter_args.items():
            if "__" in filter_key:
                split_filter_key, condition = filter_key.split("__")
                if condition == "gt":  # greater than
                    query = query.filter(
                        getattr(model, split_filter_key) > filter_value
                    )
                elif condition == "ge":  # greater than or equal
                    query = query.filter(
                        getattr(model, split_filter_key) >= filter_value
                    )
                elif condition == "lt":  # less than
                    query = query.filter(
                        getattr(model, split_filter_key) < filter_value
                    )
                elif condition == "le":  # less than or equal
                    query = query.filter(
                        getattr(model, split_filter_key) <= filter_value
                    )
                elif condition == "ne":  # not equal
                    query = query.filter(
                        getattr(model, split_filter_key) != filter_value
                    )
                elif condition == "in":  # in an array
                    query = query.filter(
                        getattr(model, split_filter_key)
                        == func.ANY(
                            list(filter_value)
                        )  # converting to list as dict.keys() gives error without conversion
                    )
                elif condition == "like":  # for partual match
                    query = query.filter(
                        getattr(model, split_filter_key).like(filter_value)
                    )
                elif condition == "ilike":  # for case insensitive partual match
                    query = query.filter(
                        getattr(model, split_filter_key).ilike(filter_value)
                    )
                elif (
                    condition == "or_none"
                ):  # to match rows with equal value or value == None
                    query = query.filter(
                        or_(
                            getattr(model, split_filter_key) == filter_value,
                            getattr(model, split_filter_key).is_(None),
                        )
                    )
                else:
                    query = query.filter(getattr(model, filter_key) == filter_value)
            else:
                if model:
                    query = query.filter(getattr(model, filter_key) == filter_value)
                else:
                    query = query.filter_by(filter_key=filter_value)
        if group_by:
            query = query.group_by(group_by)
        if order_by is not None:
            query = query.order_by(order_by)
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)

        return query

    def filter(
        self, offset: int = 0, limit: int = 20, order_by=None, **filter_args
    ) -> Any:
        """To be used to get many resources"""
        with self.session() as session:
            query = session.query(self.model)
            query = self.applyFilters(
                query,
                self.model,
                offset=offset,
                limit=limit,
                order_by=order_by,
                **filter_args,
            )
            return query.all()

    def update(self, _should_commit: bool = True, **update_values) -> Any:
        """To be used to update resource"""
        for key, value in update_values.items():
            setattr(self, key, value)

        if _should_commit:
            with self.session() as session:
                session.add(self)
                session.commit()
                session.refresh(self)

        return self

    def delete(self, obj=None) -> Any:
        """To be used to delete resource"""
        with self.session() as session:
            if obj:
                session.delete(obj)
            else:
                session.delete(self)
            session.commit()

    def createTable(self):
        """To be used by inherited classes that also inherit from DAL.ModelBase"""
        self.initConnection()
        self.metadata.create_all(
            self.activeConnections.get(self._connection_name), tables=[self.__table__]
        )
