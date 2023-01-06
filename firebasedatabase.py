import pyrebase
#import firebase_admin

firebaseConfig={
    "apiKey": "AIzaSyACckbl5EBRO1hDw2Y8MKtrhMRAqMK4PaU",
    "authDomain": "fir-course-3c4f2.firebaseapp.com",
    #"databaseURL": "https://fir-course-3c4f2-default-rtdb.firebaseio.com",
    "databaseURL":"https://console.firebase.google.com/project/fir-course-3c4f2/database/fir-course-3c4f2-default-rtdb/data/~2F",
    "projectId": "fir-course-3c4f2",
    "storageBucket": "fir-course-3c4f2.appspot.com",
    "messagingSenderId": "114171377198",
    "appId": "1:114171377198:web:3d3ee4cefb5fd24ea951bf"
}

firebase = pyrebase.initialize_app(firebaseConfig)

database = firebase.database()

#Database
#create
#data = {"age":32, "address":"LA", "employed":False, "name":"Mark"}
#database.push(data)
#database.child("people").push(data)
#database.child("people").child("myownid").set(data)

#update
#database.child("people").child("myownid").update({'names':'jane'})

'''
people = database.child("people").get()
for person in people.each():
    #print(person.val())
    #print(person.key())
'''

'''
people = database.child("people").get()
for person in people.each():
    if person.val()['name']=='Mark':
        database.child("people").child(person.key()).update({"name":"Jane"})
'''

''''
#Delete
#database.child("people").child("person").child("age").remove()
database.child("people").child("person").remove()

people = database.child("people").get()
for person in people.each():
    if person.val()['name']=='john smith':
        database.child("people").child(person.key()).child("age").remove()
'''

#Read
#people = database.child("person").child("myownid").get()
#print(people.val())

'''
people = database.child("people").order_by_child("name").equal_to("Jane").get()
for person in people.each():
    print(person.val())
'''

'''
people = database.child("people").order_by_child("name").equal_to("Jane").get()
for person in people.each():
    print(person.val()["age"])
'''

#people = database.child("people").order_by_child("age").equal_to(32).get()
#people = database.child("people").order_by_child("age").start_at(25).get()
#people = database.child("people").order_by_child("age").start_at(25).end_at(35).get()
#people = database.child("people").order_by_child("employed").equal_to(True).get()
people = database.child("people").order_by_child("employed").equal_to(True).limit_to_first(1).get()#Limit to first 1 result
people = database.child("people").order_by_child("employed").equal_to(True).limit_to_last(1).get()#Limit to last 1 result
for person in people.each():
    print(person.val())