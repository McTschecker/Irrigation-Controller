FROM resin/rpi-raspbian
RUN apt -y update && apt -y upgrade && apt -y install python pip && apt-get install build-essential python-dev git
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install GPIO Adafruit_DHT
