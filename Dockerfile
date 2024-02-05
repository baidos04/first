FROM python:3.10-alpine
# Create and set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install project dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . /app/

# Expose port 8000 for the Django application
EXPOSE 8000

COPY commands.sh /app/
RUN chmod +x /app/commands.sh

# Run the Django application
CMD ["/app/commands.sh"]