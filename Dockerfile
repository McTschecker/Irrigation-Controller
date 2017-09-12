FROM resin/rpi-raspbian
RUN apt -y update && apt -y upgrade && apt -y install python && apt-get install build-essential python-dev git
RUN curl https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install GPIO Adafruit_DHT
