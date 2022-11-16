from flask import Flask
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL

app = Flask(__name__)
CORS(app)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ueg8)ae-:!Nl'
app.config['MYSQL_DATABASE_DB'] = 'chemistry'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)