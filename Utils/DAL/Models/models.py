from sqlalchemy import Column, Integer, String, UUID, DateTime, LargeBinary, ForeignKey
from ..Services.ServiceBase import MySqlServiceBase
import uuid
from sqlalchemy import func


class User(MySqlServiceBase):
    __tablename__ = "users"

    USER = "USER"
    ADMIN = "ADMIN"

    PERMISSIONS = {"USER": 1, "ADMIN": 2}

    uuid = Column(Integer, primary_key=True, default=str(uuid.uuid4()), index=True)
    username = Column(String(50), unique=True, index=True)
    userType = Column(String(10), default=USER, nullable=False)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f"""
        uuid : {self.uuid}
        email: {self.email}
        userType: {self.userType}
        createdAt: {self.createdAt}
        updatedAt: {self.updatedAt}
        """

    def getUserPermissions(self):
        self.PERMISSIONS[self.userType]


class Token(MySqlServiceBase):
    __table_name__ = "token"

    MOBILE = "mobile"
    WEB = "web"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    refreshedAt = Column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    expiresAt = Column(DateTime(timezone=True), nullable=False)

    deviceType = Column(String, default=WEB, nullable=False, index=True)

    refreshTokenHash = Column(LargeBinary, nullable=False)
    accessTokenId = Column(String, nullable=False, index=True)

    uuid = Column(
        UUID(as_uuid=True),
        ForeignKey("user.uuid", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return f"""
        id : {self.id}
        deviceType: {self.deviceType}
        uuid: {self.uuid}
        refreshedAt: {self.refreshedAt}
        accessTokenId: {self.accessTokenId}
        createdAt: {self.createdAt}
        updatedAt: {self.updatedAt}
        """
