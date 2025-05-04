# Use official Ubuntu as the base image
FROM ubuntu:22.04

# Prevents interactive prompts during package install
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy the Python code to the container
COPY main.py /app/main.py

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python3", "main.py"]
