from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///IOT.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class iot(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    mail=db.Column(db.String(100),nullable=False)
    pswd=db.Column(db.String(100),nullable=False)

def __repr__(self) -> str:
    return f'{self.sno}-{self.mail}'   
@app.route("/")
def hello_world():
    return render_template("home.html")

if(__name__)=="__main__": #main fxn
    app.run(debug=True) #reflect o/p. any error will show in run time on browser