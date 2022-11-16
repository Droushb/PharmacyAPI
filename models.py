import datetime
from alembic import op
from main import Session, User, Drug, Order, Status

session = Session()
user1 = User(idUser=1, UserName='droush.b', FirstName="Bohdan", LastName="Drushkevych", Email="droush.b@gmail.com", Password="password", Phone="0962894556")
user2 = User(idUser=2, UserName='kindrat_2003', FirstName="Roman", LastName="Kindrat", Email="romankindrat@gmail.com", Password="password2", Phone="0967123909")
status1 = Status(idStatus=1, Name='avaliable')
drug1 = Drug(idDrug=1, Name='Fervex', Price=50, idStatus=1)
order1 = Order(idOrder=1, idDrug=1, Quantity=2, idUser=1, idStatus=1)

# session.add(user1)
# session.add(user2)
# session.add(status1)
# session.add(drug1)
# session.add(order1)

session.commit()
