# Start from a base Python image with version 3.10
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Set the Python path to /app
ENV PYTHONPATH="/app"

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 8000

# Command to start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
