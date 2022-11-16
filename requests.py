import json
from flask import Flask, request
from alembic import op
from methods import *
from main import User, Status, Drug, Order
from sqlalchemy import select
from models import session

app = Flask(__name__)

#DRUGS
@app.route('/drugs', methods = ['GET'])
def drugs_get():
       return get_drugs()

@app.route('/drug', methods = ['POST'])
def drug_post():
       id = request.args.get('id', '')
       name = request.args.get('name', '')
       price = request.args.get('price', '')
       status_id = request.args.get('status_id', '')
       return post_drug(id, name, price, status_id)

@app.route('/drug/<id>', methods = ['GET'])
def drug_get_byid(id):
       return get_drug_byid(id)

@app.route('/drug/<id>', methods = ['DELETE'])
def drug_delete(id):
    return delete_drug(id)

@app.route('/drug/<id>', methods = ['PUT'])
def drug_update(id):
       id = request.args.get('id', '')
       name = request.args.get('name', '')
       price = request.args.get('price', '')
       status_id = request.args.get('status_id', '')
       return update_drug(id, name, price, status_id)

#ORDER
@app.route('/orders', methods = ['GET'])
def orders_get():
       return get_orders()

#STATUS
@app.route('/orders/status', methods = ['GET'])
def status_get():
       return get_status()

#USER
@app.route('/user/<UserName>', methods = ['GET'])
def user_get_byid(UserName):
       return get_user_byUserName(UserName)

@app.route('/user', methods = ['POST'])
def user_post():
       id = request.args.get('id', '')
       UserName = request.args.get('UserName', '')
       firstName = request.args.get('firstName', '')
       lastName = request.args.get('lastName', '')
       email = request.args.get('email', '')
       password = request.args.get('lastName', '')
       phone = request.args.get('phone', '')
       return post_user(id, UserName, firstName, lastName, email, password, phone)

@app.route('/user/<UserName>', methods = ['PUT'])
def user_update(UserName):
       id = request.args.get('id', '')
       UserName = request.args.get('UserName', '')
       firstName = request.args.get('firstName', '')
       lastName = request.args.get('lastName', '')
       email = request.args.get('email', '')
       password = request.args.get('lastName', '')
       phone = request.args.get('phone', '')
       return update_user(id, UserName, firstName, lastName, email, password, phone)

@app.route('/user/<UserName>', methods = ['DELETE'])
def user_delete(UserName):
       return delete_user(UserName)


app.run()