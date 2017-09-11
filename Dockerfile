FROM resin/rpi-raspbian
RUN apt -y update && apt -y upgrade && apt -y install python
RUN pip install GPIO
