import pyrebase
#import firebase_admin

firebaseConfig={
    'apiKey': "AIzaSyACckbl5EBRO1hDw2Y8MKtrhMRAqMK4PaU",
    'authDomain': "fir-course-3c4f2.firebaseapp.com",
    'projectId': "fir-course-3c4f2",
    'databaseURL':'https://console.firebase.google.com/project/fir-course-3c4f2/database/fir-course-3c4f2-default-rtdb/data/~2F',
    'storageBucket': "fir-course-3c4f2.appspot.com",
    'messagingSenderId': "114171377198",
    'appId': "1:114171377198:web:3d3ee4cefb5fd24ea951bf"
}

firebase=pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

#Authentication
'''
#Login
email = input("Enter your email : ")
password = input("Enter your password : ")
try:
    auth.sign_in_with_email_and_password(email,password)
    print("successfully signed in ")
except:
    print("Invalid email or password. Try again.")    

'''

#signup
email = input("Enter your email : ")
password = input("Enter your password : ")
confirmpass = input("Enter confirm password : ")
if password==confirmpass:
    try:
        auth.create_user_with_email_and_password(email,password)
    except:
        print("Email already exists")
        
