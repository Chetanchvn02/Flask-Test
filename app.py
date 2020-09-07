from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product', methods=["GET", "POST"])
def product():
    return render_template('product.html', title="Product")

@app.route('/location')
def location():
    return render_template('location.html', title="Location")

@app.route('/movement')
def movement():
    return render_template('movement.html', title="Movement")

@app.route('/report')
def report():
    return render_template('report.html', title="report")


if __name__ == '__main__':
    app.run(debug=True)