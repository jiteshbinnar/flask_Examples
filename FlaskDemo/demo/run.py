from store import app
from store import db

if __name__=="__main__":


    @app.before_first_request
    def create_tables():

        
       db.create_all()
       

    
    app.run(debug=True)

