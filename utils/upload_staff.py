import os
import sys

import pandas as pd
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from dotenv import load_dotenv

load_dotenv()

cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

db = firestore.client()


def upload_staff(excel_file):
    df = pd.read_excel(excel_file)
    for idx, row in df.iterrows():
        doc_ref = db.collection('staff').document()
        doc_ref.set({
            'email': row['email'],
            'license': row['license'],
            'lineId': '',
            'password': 'mtc2547',
            'name': f'{row["name"]} {row["lastname"]}',
            'phone': f'{row["phone"]}',
            'pictureUrl': '',
        })


if __name__ == '__main__':
    excel_file = sys.argv[1]
    upload_staff(excel_file)