FROM python:3.11

CMD ["uvicorn main:app --reload"]