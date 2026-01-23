FROM python:3.12-alpine
#FROM python:3.12-slim

WORKDIR /home/app

COPY . .

RUN pip install debugpy
RUN pip install -e .

CMD ["python3", "-m", "debugpy"]