# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Scrapy
RUN pip install scrapy scrapy-user-agents

# Run scrapy when the container launches
CMD ["scrapy", "crawl", "top50_movies"]
