#Set OS
FROM resin/rpi-raspbian
# Defines working directory in container
WORKDIR /usr/src/app
ENV INITSYSTEM on
#Add files
ADD part2SubFunctions.py /usr/src/app/
ADD . /usr/src/app/
ADD main.py /usr/src/app/
ADD subsystems/ /usr/src/app/
#add permissions to run the run.sh
RUN chmod +x run.sh
#get dependencies
RUN apt-get update --fix-missing
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install python apt-utils
#DHT 22 Libs
RUN  apt-get install build-essential python-dev git wget python3-spidev python-spidev python-dev
#pigpio
RUN apt install pigpio
#pip
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN rm get-pip.py
#install requirements.txt
RUN pip install requests gpiozero statistics rpio pigpio RPi.Gpio
#Test part 2
RUN ls
#pigpiod
RUN export PIGPIO_ADDR=soft
RUN export PIGPIO_PORT=8888
RUN pigpiod
#Run it
CMD ["./run.sh"]
