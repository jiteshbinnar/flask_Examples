from store import login_manager
from store import bcrypt
from store import db
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),nullable=False, unique=True)
    email_address=db.Column(db.String(30),nullable=False,unique=True)
    password_hash=db.Column(db.String(60),nullable=False)
    items=db.relationship("Item", backref='owned_user',lazy=True)
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash=bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(self.password_hash,attempted_password)    
   
   

   

class Item(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    pname=db.Column(db.String(30),nullable=False,unique=True)
    price=db.Column(db.Integer,nullable=False,unique=True)
    owner=db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self) -> str:
        return f"{self.id},{self.pname},{self.price}"
    

    def buy(self,user):
        self.owner=user.id
        db.session.commit()

    def sell(self):
        self.owner=None
        db.session.commit()