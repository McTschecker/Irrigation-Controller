#Set OS
FROM resin/rpi-raspbian
# Defines our working directory in container
WORKDIR /usr/src/app
#Add files
#COPY . /
ADD main.py /usr/src/app/
ADD subsystems/ /usr/src/app/
ADD run.sh /usr/src/app/
ADD . /usr/src/app/
#get dependencies
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python apt-utils
#DHT 22 Libs
RUN  apt-get install build-essential python-dev git wget python3-spidev python-spidev python-dev 
#gpio zero
RUN sudo apt-get install  python-dev 
RUN sudo apt-get install python-rpi.gpio python3-rpi.gpio
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install RPi.Gpio
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install --force-pi
ENV INITSYSTEM on
#Run it
#CMD ["ls"]
#CMD ["sudo exec run.sh"]
CMD ["python", "main.py"]