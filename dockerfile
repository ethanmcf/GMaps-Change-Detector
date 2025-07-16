FROM mcr.microsoft.com/playwright/python:v1.53.0-jammy

WORKDIR /app

# Copy source code
COPY src ./src


# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy google cred key
COPY google_cred_key.json .

# Set environment variables
ENV PYTHONPATH=/app/src

# Run the gmaps detector
CMD ["bash", "src/run.sh", "loop"]