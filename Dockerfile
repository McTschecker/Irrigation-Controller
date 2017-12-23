#Set OS
FROM resin/rpi-raspbian
# Defines our working directory in container
WORKDIR /usr/src/app
ENV INITSYSTEM on
#Add files
ADD testSubFunctions.py /usr/src/app/
#get dependencies
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python apt-utils
#DHT 22 Libs
RUN  apt-get install build-essential python-dev git wget python3-spidev python-spidev python-dev 
#gpio zero
RUN sudo apt-get install  python-dev
#pigpio
RUN apt install pigpio
#pip
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN rm get-pip.py
#install requirements.txt
RUN pip install requests gpiozero statistics rpio pigpio RPi.Gpio
#DHT22
#RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
#RUN cd Adafruit_Python_DHT && python setup.py install --force-pi
#RUN pip install Adafruit_Python_DHT==1.1.2
#pigpiod deamon start
RUN export PIGPIO_ADDR=soft
RUN export PIGPIO_PORT=8888
RUN pigpiod
#Add files
ADD . /usr/src/app/
ADD main.py /usr/src/app/
ADD subsystems/ /usr/src/app/
RUN chmod +x run.sh
#Run it
CMD ["./run.sh"]