# Start from the official Python base image.
FROM python:3.11

# This is where we'll put the requirements.txt file and the app directory.
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#Add metadata to the image to describe that the container is listening on port 8080
EXPOSE 8080

# Copy the current directory in the project to the workdir
COPY ./app /code/app

# Set the default command for the container
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]