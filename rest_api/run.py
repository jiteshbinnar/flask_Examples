
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema,fields



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///apis.db'
db=SQLAlchemy(app)
app.app_context().push()


class BookStore(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60),nullable=False)
    price=db.Column(db.Integer,nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            
        }  


    
    

    def  __repr__(self) -> str:
        return f"{self.id},{self.name},{self.price}"

db.create_all()

class BookSchema(Schema):

    id = fields.Int(dump_only=True)
    name = fields.Str()
    price = fields.Int()
    
    

book_schema = BookSchema()
books_schema = BookSchema(many=True)




@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getallbooks",methods=["GET"])
def get_all_book():


    
    book=BookStore.query.all()
    result= book_schema.dump(book,many=True)
    return {"books":result}
        

@app.route("/addbooks/<int:books_id>",methods=["GET"])
def get_books_by_id(books_id):
    book=BookStore.query.filter_by(id=books_id).first()
    if book:




        result=book_schema.dump(book)
        return {"book":result}
    
    else:
        return f"Book with id: {books_id} not found"








@app.route("/update_book/<int:book_id>",methods=["PUT"])
def update_books(book_id):
    book1=  BookStore.query.filter_by(id=book_id).first()
    if book1:
        book1.name=request.json.get('name',book1.name)
        book1.price=request.json.get('price',book1.price)
        db.session.commit()

        return jsonify(book1.to_json())



@app.route("/deletebooks/<int:book_id>",methods=["DELETE"])    
def delete_books(book_id):
    book= BookStore.query.filter_by(id=book_id).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return f"Book with id {book_id} is deleted..!"


 
    return f"Book with id {book_id} not exist"
        







    
        

    











@app.route("/addbooklet",methods=["POST"])
def addbooklet():
    json_data = request.get_json()
    data = book_schema.load(json_data)
    name,price= data['name'],data['price']
    book = BookStore.query.filter_by(name=name, price=price).first()
    if book:
        return "Book Exist"
    else:

        book = BookStore(name=name, price=price)
        db.session.add(book)    
        db.session.commit()
        return book_schema.dump(book)




   




        
        
        


         




if __name__=='__main__':
    app.run(debug=True)

