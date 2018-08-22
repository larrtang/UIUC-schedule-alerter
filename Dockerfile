FROM python:3

ENV TWILIO_SID= 
ENV TWILIO_TOKEN=

COPY . /
RUN pip install bs4 lxml twilio selenium
CMD ["python", "main.py"]