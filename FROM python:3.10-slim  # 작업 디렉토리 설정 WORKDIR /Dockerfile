FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

# 포트 설정
ENV PORT=8080
EXPOSE 8080

# FastAPI 앱 실행 (api.py 기준)
CMD ["uvicorn", "agentlayer.api:app", "--host", "0.0.0.0", "--port", "8080"]
