# Use the official MongoDB image as the base image
FROM mongo:latest

# Set environment variables
ENV MONGO_INITDB_ROOT_USERNAME=admin
ENV MONGO_INITDB_ROOT_PASSWORD=!QAZ2wsxAdmin2023
ENV MONGO_INITDB_DATABASE=environment_db

# Copy the initialization script to the container
COPY mongo_init.js /docker-entrypoint-initdb.d/

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the Python script and requirements file to the container
COPY requirements.txt .
COPY load_initial_data.py .

#Install python3 and pip3
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Install Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose MongoDB default port and start MongoDB with your initialization script
EXPOSE 27017

# Run MongoDB and your Python script
CMD ["bash", "-c", "mongod --fork --logpath /var/log/mongod.log && python3 load_initial_data.py"]