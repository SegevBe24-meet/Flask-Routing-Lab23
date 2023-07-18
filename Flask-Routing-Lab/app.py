from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',
    static_folder='static' 
)

@app.route('/')
def homePage():
    return render_template("home.html")

@app.route('/items')
def product():
    return render_template("product.html")

@app.route('/cart')
def cart():
    return render_template("cart.html")

if __name__ == "__main__": 
    app.run(debug=True)
