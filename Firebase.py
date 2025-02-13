import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import auth 
cred=credentials.Certificate("C:Users/jayac/Downloads/circuit-builder-2f673-firebase-adminsdk-fbsvc-6f134218aa.json")
firebase_admin.initialize_app(cred)
db=firestore.client()