# Use official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install curl for debugging purposes
RUN apt-get update && apt-get install -y curl

# Copy the app code
COPY . .

# Expose port 5000 for the Flask web app
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
