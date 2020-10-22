import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from google.cloud import datastore



client = datastore.Client()

## Firebase Connection Variables
cred = credentials.Certificate("./f_keys.json")
app = firebase_admin.initialize_app(cred)
store = firestore.client()
## </end> Firebase Connection Variables


class FirebaseReplication:

    def __init__(self, ds_entity, ds_key, ds_list, collection, toList):
        self.collection = collection
        self.toList = toList
        self.ds_key = ds_key
        self.ds_entity = ds_entity
        self.ds_list = ds_list


    

    def update(self):
        key = client.key(self.ds_entity, self.ds_key)
        entity = datastore.Entity(key=key)
        result = client.get(key)
        toDict = {}
        for idx, elem in enumerate(self.toList):
            toDict[elem] = result[self.ds_list[idx]]
        doc_ref = store.collection(self.collection)
        doc_ref.add(toDict)


# Example:- FirebaseReplication(ds_entity="EntityKind", ds_key=1234, ds_list=["baz", "foo"], collection="NewOne", toList=["foo", "bar"]).update()