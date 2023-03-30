FROM python:3.10.10-slim

WORKDIR app/harlok13/aio

COPY requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt

COPY bot_ai ./bot_ai

CMD ["python", "-m", "bot_ai"]
