FROM python:3.11.2

WORKDIR /app

COPY requirements.txt ./

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]