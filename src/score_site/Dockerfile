FROM python:alpine

WORKDIR /app

COPY main_score.py .
COPY score_requirements.txt .
RUN echo 800 > Scores.txt

RUN pip install -r score_requirements.txt

CMD ["python", "main_score.py"]
