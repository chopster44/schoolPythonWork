from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    bases = ["thin", "deep pan", "cheese", "mahusive"]    
    return render_template('order.html', bases=bases)

# @app.route("/submit", methods=["POST"])
# def order():

