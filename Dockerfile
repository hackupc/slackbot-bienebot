FROM python:3.7
ADD requirements.lock /srv/biene-bot
RUN pip3 install -r requirements.lock
ADD . /srv/biene-bot
WORKDIR /srv/biene-bot
CMD python3 -m hackupc.bienebot
