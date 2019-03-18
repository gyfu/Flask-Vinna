from manage import db, app
class User(db.models):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.string(64),index=True,unique=True)
    password=db.Column(db.String(64),index=True,unique=True)
    def __repr__(self):
        return "<User {}>".format(self.name)

