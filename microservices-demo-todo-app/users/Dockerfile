FROM python:2

RUN mkdir -p /opt/todoapp/users
COPY . /opt/todoapp/users
WORKDIR /opt/todoapp/users

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "run.py"]

