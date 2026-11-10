# Python ka official slim image use kar rahe hain
FROM python:3.11-slim

# Container ke andar working directory set karna
WORKDIR /app

# Pehle requirements.txt copy karo taake Docker caching optimize ho jaye
COPY requirements.txt .

# Saari Python dependencies install karna
RUN pip install --no-cache-dir -r requirements.txt

# Baaki ka saara backend code copy karna
COPY . .

# FastAPI ka port expose karna
EXPOSE 8000

# Server run karne ki command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]