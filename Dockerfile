# Use the official Python image from Docker Hub with Python 3.9
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Expose port 5000 (the default Flask port)
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python", "pizzaOrder.py"]
