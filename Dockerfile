# Specify our container base image
FROM python: 2.7.18

# Select a directory within our container
WORKDIR /usr/app

# Copy everything from our project root into our WORK DIRECTORY directory
COPY app/ .

# Install dependencies
RUN pip install -r requirements.txt

# Give our container internet access
EXPOSE 80

# Execute this command on start
ENTRYPOINT ["python", "mini_project.py"]