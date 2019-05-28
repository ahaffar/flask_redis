# BASE IMAGE
FROM python:3.7

# CHANGE WORKIN DIR AND COPY FILES
WORKDIR /code
COPY . /code

# INSTALL REQUIRED PACAKGES
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN THE APP
CMD ["python", "./main.py"]
