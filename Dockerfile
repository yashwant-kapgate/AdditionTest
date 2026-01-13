# Use stable Python version (recommended for GCP)
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Start app using Gunicorn (Cloud Run expects port 8080)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
