from flask import Flask, render_template

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "hola otto"

@app.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")
    
@app.route('/productos', strict_slashes=False)
def productos():
    return render_template("productos.html")

@app.route('/login', strict_slashes=False)
def login():
    return render_template("login.html")

@app.route('/items', strict_slashes=False)
def items():
    return render_template("items.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)