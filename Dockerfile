FROM python:3.11.9-slim

WORKDIR /app


COPY . /app/

RUN apt-get update && apt-get install -y gcc python3-dev
RUN pip install -r requirements.txt


EXPOSE 8080

CMD ["uvicorn", "gemma:app", "--host", "0.0.0.0", "--port", "8080"]