FROM python:3.7-buster

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

#configures the container to run as an executable; only the last ENTRYPOINT instruction executes
ENTRYPOINT [ "python" ]
CMD [ "count_server.py" ] 