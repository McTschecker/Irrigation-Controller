FROM resin/rpi-raspbian
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python && apt-get install build-essential python-dev git wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install GPIO 
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install --force-pi
