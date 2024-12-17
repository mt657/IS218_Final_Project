# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . .

# Expose the app on port 8000 (adjust based on your framework)
EXPOSE 8000

# Run the application
CMD ["python", "-m", "app.main"]
