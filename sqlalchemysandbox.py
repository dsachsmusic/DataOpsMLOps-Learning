import sqlalchemy

from sqlalchemy import create_engine
engine = create_engine('mysql://helloec2rds_user:mypassword@localhost/db_helloec2rdsipaddress_misc')


#the following can be used to learn more about the database, tables, columns, etc.
#...note: the loop/creating a list of dictionaries, was my idea...there could 
# ...be better ways
#from sqlalchemy import inspect
## Use the inspector to get table information
#inspector = inspect(engine)
#
## Get a list of table names
#tables = inspector.get_table_names()
#
##get column names, per table
#tables_and_their_columns = []
#for table in tables:
#    table_name_dictionary_item = {
#        "table_name": table 
#    }
#    
#    tables_and_their_columns.append(table_name_dictionary_item)
#    
#    table_columns_dictionary_item = {
#        "table_columns": inspector.get_columns(table)
#    }
#
#    tables_and_their_columns.append(table_columns_dictionary_item)

#working with the databse/tables using orm 
#from sqlalchemy.orm import sessionmaker

#Session = sessionmaker(bind=engine)
#session = Session()

#note: because not sure off hand how to grant helloec2rds_user access to create tables...
#...created a new table, from MySQL Workbench...
#...and, granted helloec2rds_user read, update, and delete by running the following
#  CREATE TABLE db_helloec2rdsipaddress_misc.tbl_users(
#	id INT AUTO_INCREMENT PRIMARY KEY,
#	firstname VARCHAR(50),
#   lastname VARCHAR(50),
#   age INT,
#   note VARCHAR(255)
#);
#
#GRANT SELECT, INSERT, UPDATE, DELETE ON db_helloec2rdsipaddress_misc.tbl_users TO 'helloec2rds_user'@'localhost';


#note: the following is using orm with an "automap" type of base class
#...which...brings in the existing tables from the engine/session(?) as orm objects(?)
#...but can also set/use a "declarative" base class, with which...can be used to ...
# ...create new tables, etc?
#from sqlalchemy.ext.automap import automap_base
#Base = automap_base()
#Base.prepare(engine, reflect=True)
#Base.classes.keys() #lists the mapped classes, i.e. the tables created via automapping
#query_results = session.query(Base.classes.tbl_users).all()  
for result in query_results:
    print("Name is " + result.__dict__['firstname'] + " " + result.__dict__['lastname'] + ". Age is", result.__dict__['age'])
#dir(Base.classes.tbl_visitor_ip.__table__)

#get the tbl_users class(?) brought in with automap?  capture as a variable(?)
Users = Base.classes.tbl_users

#create an instance(?) of the Users(?)....class(?), use session and its methods(?)
# ...to interact with/manipulate(?) table
#insert
new_user = Users(firstname = 'David')
session.add(new_user)
session.commit()
#update
David = session.query(Users).filter_by(firstname='David').first()
David.age = 38
session.commit()

#add a bunch of users, with a script
first_names = ['David','Ben','Josie','Garfield','Mr. Wonderful','Selma','Pi','X']
last_names = ['Garcia','Johnson','Gold','Xi','Dude']
len_to_age_map = {
    5: 30,
    10: 41
}
len_to_notes_map = {
    5: "5 or less",
    10: "10 or less"
}

for first_name in first_names:
    for last_name in last_names:
        if len(first_name) + (len(last_name)) <= 5:
            age = len_to_age_map.__getitem__(5)
            note = len_to_notes_map.__getitem__(5)
        elif len(first_name) + (len(last_name)) <= 10:
            age = len_to_age_map.__getitem__(10)
            note = len_to_notes_map.__getitem__(10)
        else:
            age = "99"
            note = "nothing known of this"
        print("Name: " + first_name + " " + last_name + ", Age:",age,"... Note: " + note)
        
        new_user = Users(
            firstname = first_name,
            lastname = last_name,
            age = age,
            note = note
        )
        session.add(new_user)
        session.commit()
#example for if want to delete a row
#session.delete(David)
#session.commit()
#declarative base...making a table and updating, etc
#haven't tested the following, because permissions obstacle...(see above)
#from sqlalchemy import Column, Integer, String, create_engine
#from sqlalchemy.ext.declarative import declarative_base
#
#Base = declarative_base()
#
#class User(Base):
#    __tablename__ = 'users'
#
#    id = Column(Integer, primary_key=True)
#    name = Column(String(50))
#    age = Column(Integer)
#    note = Column(String(255))
#
#    def __repr__(self):
#        return f"<User(name='{self.name}', age='{self.age}')>"
#
#Base.metadata.create_all(engine)
