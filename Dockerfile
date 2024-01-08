# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run app.py when the container launches
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
