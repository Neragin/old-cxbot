FROM python:3.8

ADD src .
ADD requirements.txt .


RUN pip install -r requirements.txt
RUN ls
CMD [ "python", "./main.py" ]