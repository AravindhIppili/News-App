# Use the official Python 3.11 base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /newsapp

# Install nano and bash (optional, for development purposes)
RUN apt-get update && apt-get install -y nano bash

# Copy the application code into the container
COPY . .

# Install the project dependencies
RUN pip install -r requirements.txt

# Expose the port on which the FastAPI application will run
EXPOSE 8000

# Define the command to start the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--reload"]
