from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',
    static_folder='static' 
)

@app.route('/homepage')
def homePage():
    return render_template("home.html")



if __name__ == "__main__": 
    app.run(debug=True)
