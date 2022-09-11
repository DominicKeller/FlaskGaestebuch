from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#Hier wird die Verbindung zur SQL Datenbank gemacht
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://domi:n~8o6y7X8@185.230.138.184/db_domi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#hier wird die Datenbank mit Daten gefüllt
db = SQLAlchemy(app)

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	comment = db.Column(db.String(1000))

#in diesem Abschnitt des Scripts werden die Routen auf die verschiedenen html Seiten gemacht
@app.route("/")
def hello():
	result = Comments.query.all()
	return render_template('index.html', result=result)

@app.route('/sign')
def sign():
	return render_template('sign.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	signature = Comments(name=name, comment=comment)
	db.session.add(signature)
	db.session.commit()

	return redirect('http://161.97.101.115/')

if __name__ == '__main__':
	app.run(debug=True)


#hier wird die API Schnittstelle bereitgestellt mit jsonify
@app.route('/api', methods = ['GET', 'POST'])
def homeTest():
    if(request.method == 'GET'):

        data = "Die API Schnittstelle funktioniert :)"
        return jsonify({'data': data})

#hier wird die Route auf die Loginseite gemacht (konnte leider nicht mehr ganz umgesetzt werden vom Verfasser)
@app.route('/login')
def loginPage():
	return render_template('login.html')
