FROM python:3.8

WORKDIR /slackapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /slackapp

CMD [ "python", "App.py" ]
