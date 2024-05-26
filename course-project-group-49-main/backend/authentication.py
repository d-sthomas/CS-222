import pyrebase 
import firebase_admin 
from firebase_admin import credentials
import json
import os 
from dotenv import load_dotenv

#establishing connection to firebase
connection_string = json.loads(os.getenv('FIREBASE_AUTHENTICATION'))
cred = credentials.Certificate(connection_string)
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://filmfinder-5145d-default-rtdb.firebaseio.com/',
        }
)

firebase = pyrebase.initialize_app(cred)
auth = firebase.auth()

email = 'test@gmail.com'
password = '123456'

# user = auth.create_user_with_email_and_password(email, password)
# print(user)

user = auth.sign_in_with_email_and_password(email,password)

#gets the account password, emailID, and the last time password was updated
info = auth.get_account_info(user['idToken'])

# sends email verifcation to verify the email
auth.send_email_verification(user['idToken'])

#resets the password
auth.send_password_reset_email(email)