# Use a lightweight Python image
FROM python:3.12.5-slim-bullseye

# Set the working directory inside the container
WORKDIR /docker

# Copy the requirements file into the container
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .


# Command to run the Flask application
CMD [ "python3", "-m", "flask", "--app", "loan", "run", "--host=0.0.0.0" ]
