import json
from sqlite3 import Date
from flask import Flask, jsonify
from sqlalchemy import select
from main import User, Status, Drug, Order
from models import session

def serialize(self):
     return {
        "Id": self.idDrug,
        "Name": self.name,
        "Duration": self.duration,
        "Photo": self.photo,
        "Category": self.id_idCategory
     }

def get_drugs():
    AllDrugs = session.execute(select(Drug))
    drugs = AllDrugs.scalars().all()
    result = ""
    for drug in drugs:
        status = session.query(Status).filter_by(idStatus = drug.idStatus).one()
        drugJSON = {
            "Id": drug.idDrug,
            "Name": drug.Name,
            "Price": drug.Price,
            "Status": status.idStatus
        }
        result+= json.dumps(drugJSON)
    return result

def get_drug_byid(id):
    drug = session.query(Drug).filter_by(idDrug = id).one()
    drugJSON = {
        "Id": drug.idDrug,
        "Name": drug.Name,
        "Price": drug.Price,
        "idStatus": drug.idStatus
    }
    return json.dumps(drugJSON)

def post_drug(id, Name, Price, idStatus):
    addeddrug = Drug(idDrug=id, Name=Name, Price=Price, idStatus=idStatus)
    session.add(addeddrug)
    session.commit()
    return 'Added a Drug with id %s' % id + get_drug_byid(id)
    #return jsonify(Drug=addeddrug.serialize)

def delete_drug(id):
    drugToDelete = session.query(Drug).filter_by(idDrug = id).one()
    session.delete(drugToDelete)
    session.commit()
    return 'Removed Drug with id %s' % id

def update_drug(id, name, price, status_id):
   updatedDrug = session.query(Drug).filter_by(idDrug = id).one()
   if name!='':
       updatedDrug.name = name
   if price!='':
       updatedDrug.price = price
   if status_id!='':
       updatedDrug.status_id = status_id
   session.add(updatedDrug)
   session.commit()
   return 'Updated a Drug with id %s' % id + get_drug_byid(id)

def get_orders():
    AllOrders = session.execute(select(Order))
    orders = AllOrders.scalars().all()
    result = ""
    for order in orders:
        orderJSON = {
            "Id": order.idOrder,
            "Drug_id": order.idDrug,
            "Quantity": order.Quantity,
            "User_id": order.idUser,
            "Status_id": order.idStatus,
        }
        result+= json.dumps(orderJSON)
    return result

def get_status():
    AllEvents = session.execute(select(Status))
    events = AllEvents.scalars().all()
    result = ""
    for event in events:
        orderJSON = {
            "Id": event.idStatus,
            "Name": event.Name,
        }
        result+= json.dumps(orderJSON)
    return result

def get_user_byUserName(UserName):
    userOne = session.query(User).filter_by(UserName = UserName).one()
    userJSON = {
        "Id": userOne.idUser,
        "UserName": userOne.UserName,
        "First Name": userOne.FirstName,
        "Second Name": userOne.LastName,
        "Email": userOne.Email,
        "Password": userOne.Password,
        "Phone": userOne.Phone
    }
    return json.dumps(userJSON)

def post_user(id, UserName, firstName, lastName, email, password, phone):
    addeduser = User(idUser=id, UserName=UserName, FirstName=firstName, LastName=lastName,
    Email=email, Password=password, Phone=phone)
    session.add(addeduser)
    session.commit()
    return 'Added a User with id %s' % id + get_user_byUserName(UserName)

def delete_user(UserName):
    userToDelete = session.query(User).filter_by(UserName = UserName).one()
    session.delete(userToDelete)
    session.commit()
    return 'Removed User with UserName %s' % UserName

def update_user(id, UserName, firstName, lastName, email, password, phone):
    updatedUser = session.query(User).filter_by(UserName = UserName).one()
    if UserName!='':
        updatedUser.UserName = UserName
    if firstName!='':
        updatedUser.FirstName = firstName
    if lastName!='':
        updatedUser.LastName = lastName
    if email!='':
        updatedUser.Email = email
    if password!='':
        updatedUser.Password = password
    if phone!='':
        updatedUser.Phone = phone
    session.add(updatedUser)
    session.commit()
    return 'Updated a User with UserName %s' % UserName + get_user_byUserName(UserName)
