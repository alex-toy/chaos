FROM python:3.8.5

COPY . /lead_scoring
WORKDIR /lead_scoring

RUN apt-get update

RUN pip install -r requirements.txt
RUN pip install -e ./

ENV FLASK_PORT=5000
EXPOSE ${FLASK_PORT}

CMD ["gunicorn", "lead_scoring.application.server:app", "-b", "0.0.0.0:5000"]
