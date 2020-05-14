#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")

@app.route("/puppy")
def fun():
    return render_template("puppy.html")

#start the server
if __name__ == "__main__":
    app.run()
