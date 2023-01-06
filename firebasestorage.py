import pyrebase
import urllib


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

storage = firebase.storage()

'''
#Storage
#upload
filename = input("Enter the name of the file you want to upload : ")
cloudfilename = input("Enter the name of the file on the cloud : ")
storage.child(cloudfilename).put(filename)
print(storage.child(cloudfilename).get_url(None))
'''

#download
#cloudfilename = input("Enter the name of the file you want to download : ")
#storage.child(cloudfilename).download("","downloaded.txt")
storage.child("google").download("","downloaded.txt")

#reading file
cloudfilename = input("Enter the name of the file you want to download : ")
url = storage.child(cloudfilename).get_url(None)
f = urllib.request.urlopen(url).read()
print(f)
