FROM python:3.10
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
RUN pip install gunicorn
RUN pip3 install blackfire
COPY . .
WORKDIR .
EXPOSE 5000
RUN which gunicorn

CMD ["blackfire-python","gunicorn", "-w", "1", "--threads", "2", "-b", "0.0.0.0:5000", "app:app"]

