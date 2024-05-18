FROM python:3.10.12

WORKDIR /app


COPY . /app/

RUN apt update && apt install -y curl
RUN pip install -r requirements.txt


EXPOSE 8080

CMD ["python3", "chatbot.py"]
