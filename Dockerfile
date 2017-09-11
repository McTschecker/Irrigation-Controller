FROM resin/rpi-raspbian
RUN apt -y update && apt -y upgrade && apt -y install python && apt-get install build-essential python-dev git
RUN pip install GPIO
RUN git pull https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT
RUN sudo python setup.py install