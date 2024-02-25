# Dockerfile
# Use the official Python 3.9 Docker image as a base
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt ./

# Install the required Python packages
RUN pip install -r requirements.txt

# Remove unnecessary build files
RUN rm -rf /root/.cache

# Copy the application code to the container
COPY . .

# Set the execution PATH
ENV PATH="/app:${PATH}"

# Expose port 8000
EXPOSE 8080

# Run the application using gunicorn
CMD ["gunicorn", "validation_check.validation_check.wsgi:application", "--bind", "0.0.0.0:8080"]