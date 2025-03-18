from flask import Flask,render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World! 林冠廷"

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/welcome", methods=["GET", "POST"])

def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)



if __name__ == "__main__":
    app.debug= True
    app.run()

