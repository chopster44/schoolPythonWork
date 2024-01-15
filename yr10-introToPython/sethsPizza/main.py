from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    bases = ["thin", "deep pan", "cheese", "mahusive"]
    toppings = ["mozarella", "tomato sauce", "olives", "mushrooms", "peperoni"]
    sides = ["dough balls", "garlic bread", "chips", "salad"]
    return render_template('order.html', bases=bases, toppings=toppings, sides=sides)

# @app.route("/submit", methods=["POST"])
# def order():

