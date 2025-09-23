import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key JSON
cred = credentials.Certificate(r"C:\Users\yashh\OneDrive\Documents\VSC Workspace\Python\Django\Learning\myapp\learning-9b624-firebase-adminsdk-fbsvc-f925b62aba.json")
firebase_admin.initialize_app(cred)

db = firestore.client()   # Firestore DB client
