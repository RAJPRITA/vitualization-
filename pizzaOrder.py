from flask import Flask, render_template, request

app = Flask(__name__)

# Define pizza prices in a dictionary
pizza_prices = {
    "S": 15,
    "M": 20,
    "L": 25
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        size = request.form.get('size', '').strip().upper()
        add_pepperoni = request.form.get('pepperoni', '').strip().upper()
        extra_cheese = request.form.get('extraCheese', '').strip().upper()

        # Validate user input for size
        if size not in pizza_prices:
            return "Invalid pizza size selected."

        bill = pizza_prices[size]

        if add_pepperoni == "Y":
            bill += 2
        if extra_cheese == "Y":
            bill += 1

        return f"Your final bill is ${bill}"

    return render_template('order.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
