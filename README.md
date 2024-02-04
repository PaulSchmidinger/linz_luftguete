This repository provides a Docker environment for setting up a MongoDB database and loading initial air quality data into it. The MongoDB instance is initialized with a specified username, password, and database. Additionally, a Python script is included to fetch air quality data from specific APIs, save it as JSON files, and then load these files into the MongoDB database.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker installed on your machine
- Python 3 and pip installed

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/PaulSchmidinger/linz_luftguete.git
   ```

2. Build the Docker image:

   ```bash
   cd linz_luftguete
   docker build -t linz_luftguete .
   ```

3. Run the Docker container:

   ```bash
   docker run -d -p 27017:27017 linz_luftguete
   ```

   This command starts the MongoDB instance and runs the data loading script to populate the database with air quality data.

4. Check MongoDB logs for successful initialization:

   ```bash
   docker logs <container_id>
   ```

## Data Loading

### Python Script

The `load_initial_data.py` script connects to the MongoDB Docker instance and loads air quality data from JSON files into the specified database and collection.

### Data Download Script

The `downloadjson.py` script fetches air quality data from predefined APIs, saves it as JSON files, and logs the process in `jsondump/jsondump.log`.

## Configuration

### Dockerfile

The `Dockerfile` sets up the MongoDB environment, copies necessary scripts, and installs Python dependencies.

### mongo_init.js

The `mongo_init.js` script initializes the MongoDB with a specified user, password, and roles. It also creates indexes on relevant fields for optimized queries.

### requirements.txt

The `requirements.txt` file lists the Python packages required for the data loading script.
