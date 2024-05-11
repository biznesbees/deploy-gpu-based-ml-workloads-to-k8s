FROM python:3.11.9-slim

WORKDIR /app


COPY . /app/

RUN pip install -r requirements.txt


EXPOSE 8080

CMD ["uvicorn", "gemma:app", "--host", "0.0.0.0", "--port", "8080"]