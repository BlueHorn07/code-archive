FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "main.py"]