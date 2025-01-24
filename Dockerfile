# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Set environment variables to limit OpenBLAS threads
ENV OMP_NUM_THREADS=1
ENV OPENBLAS_NUM_THREADS=1

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run main.py with 30 workers when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app", "-w", "3", "-t", "120"]