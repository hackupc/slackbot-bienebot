FROM python:3.7
ADD . /srv/bienebot
WORKDIR /srv/bienebot
RUN pip3 install -r requirements.lock
CMD python3 -m hackupc.bienebot