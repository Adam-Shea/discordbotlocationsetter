FROM python:3
# Adding build tools to make yarn install work on Apple silicon / arm64 machines
ADD main.py /

ARG TOKEN

ENV TOKEN $TOKEN

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN apt-get -y update
CMD ["python3", "/main.py"]