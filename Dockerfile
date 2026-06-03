# Use official Python image (base environment)
FROM python:3.11-slim

# Set working directory inside container (where code lives)
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]

# Health check
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
  interval: 30s
  timeout: 10s
  retries: 3