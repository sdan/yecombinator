# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt --upgrade numpy torch

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run main.py with 30 workers when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app", "-w", "5", "-t", "300"]