FROM python:alpine

WORKDIR /app

COPY main_score.py .
COPY score_config.py .
RUN echo 800 > Scores.txt

RUN pip install Flask

CMD ["python", "main_score.py"]
