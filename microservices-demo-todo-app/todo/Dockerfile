FROM python:2

RUN mkdir -p /opt/todoapp/todo
COPY . /opt/todoapp/todo
WORKDIR /opt/todoapp/todo

RUN pip install -r requirements.txt

EXPOSE 5001
CMD ["python", "run.py"]

