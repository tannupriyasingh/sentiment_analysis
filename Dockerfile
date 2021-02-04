FROM continuumio/miniconda3
RUN apt-get install -y libsndfile1
RUN mkdir /app
WORKDIR /app
ADD src /app/src
RUN pip install -r /app/src/requirements.txt
