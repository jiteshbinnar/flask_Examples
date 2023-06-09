from flask import Flask,jsonify



app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/even/<int:num>")
def even_number(num):
    if(num%2==0):
        result={
            "Number":num,
            "Even":True,
            "Ip Address":"122.33.23.34"
        }

    else:
         result={
            "Number":num,
            "Even":False,
            "Ip Address":"122.33.23.34"
        }

    return jsonify(result)  
  

if __name__=='__main__':
    app.run(debug=True)