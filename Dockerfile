FROM ubuntu:focal

RUN mkdir /opt/apps
COPY . /opt/apps

WORKDIR /opt/apps

# Install python
RUN apt-get update
RUN apt-get install -y python3 python3-pip

# Install python deps
RUN pip3 install -r requirements.txt

CMD [ "flask", "--app", "app.py", "run", "--host=0.0.0.0" ]
