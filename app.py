from flask import Flask , render_template ,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conect.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Conect(db.Model):
    idcons = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    mail = db.Column(db.String(80), unique=True, nullable=False)
    coment = db.Column(db.String(200), unique=True, nullable=False)
    date = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route("/" , methods = ["GET","POST"])
def index():
    # form submit
    if request.method == 'POST':
        name = request.form['name']
        mail = request.form['mail']
        coment = request.form['coment']

        contact = Conect(name = name, mail = mail, coment=coment)
        db.session.add(contact)
        db.session.commit()
        return render_template("thankyou.html")

    return render_template("index.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@app.route("/error")
def error():
    return render_template("error.html")    

@app.route("/graphic")
def graphic():
    return render_template("grapic.html")    

if __name__ == "__main__":
    app.run(debug=True)    