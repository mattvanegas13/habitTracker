FROM python:3.11-slim
WORKDIR /api
COPY requirements.txt .
RUN apt-get update && apt-get install -y curl
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["flask", "--debug", "run","--host=0.0.0.0", "--port=8000"]