from mongoengine import Document, StringField

class BaseUser(Document):
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    email = StringField(required=True)
    password = StringField()

    meta = {"strict": False, "collection": "users"}

    def to_dict(self):
        return {
            "id": str(self.id),
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
        }
    
