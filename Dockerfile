FROM python:3.6
ADD . /srv/bienebot
WORKDIR /srv/bienebot
RUN pip3 install -r requirements.txt
CMD python3 -m hackupc.bienebot