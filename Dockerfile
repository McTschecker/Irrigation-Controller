#Set OS
FROM resin/rpi-raspbian
#Add files
COPY . /app
#get dependencies
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python 
RUN  apt-get install build-essential python-dev git wget python3-spidev python-spidev python-dev #DHT 22 Libs
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install GPIO 
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install --force-pi
#Run it
CMD ["python", "main.py"]
