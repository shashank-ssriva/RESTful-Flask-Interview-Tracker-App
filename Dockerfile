FROM python:3.9
COPY requirements.txt /src/requirements.txt
RUN pip3 install --upgrade pip
WORKDIR /src
RUN pip3 install -r /src/requirements.txt
COPY app.py /src
COPY Interviews.csv /src
CMD python /src/app.py