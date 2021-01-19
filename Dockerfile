FROM python:3.8.5

COPY . /chaos
WORKDIR /chaos

RUN apt-get update

RUN pip install -r requirements.txt
RUN pip install -e ./

ENV YOTTA_ML3_CONFIGURATION_PATH="/secret/config.yml"
ENV FLASK_PORT=5000
EXPOSE ${FLASK_PORT}

CMD ["gunicorn", "chaos.application.server:app", "-b", "0.0.0.0:5000"]
