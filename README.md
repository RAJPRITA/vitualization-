# vitualization-
This is the app which will tell you the price of pizza based on certain input from the user
1. Build the Docker image:
docker build -t pizzaorder .

2. Run the Docker container:

docker run -d --name pizzaorder-container -p 5000:5000 pizzaorder

3. Access the web application in your browser at http://localhost:5000.
