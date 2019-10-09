FROM python:3.7
ADD . /srv/biene-bot
WORKDIR /srv/biene-bot
RUN pip3 install -r requirements.lock
CMD python3 -m hackupc.bienebot