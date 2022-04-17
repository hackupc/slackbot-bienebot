FROM python:3.7
WORKDIR /srv/biene-bot
ADD requirements.lock .
RUN pip3 install -r requirements.lock
ADD . .
CMD python3 -m hackupc.bienebot
