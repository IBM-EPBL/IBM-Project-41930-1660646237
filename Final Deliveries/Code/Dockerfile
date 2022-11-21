  FROM python:3.9.13
  LABEL maintainer="Kunal Malhotra, kunal.malhotra1@ibm.com"
  RUN mkdir /app
  WORKDIR /app
  COPY . /app
 

  WORKDIR /app

  RUN pip install --upgrade setuptools
  RUN pip install --upgrade pip
  RUN pip install ibm-db
  RUN pip install flask
  EXPOSE 5000
  ENTRYPOINT [ "python" ]
  CMD [ "app.py" ]