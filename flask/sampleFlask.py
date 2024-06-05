from flask import Flask 
app = Flask(__name__) 

# routing the decorator function hello_name 
@app.route('/hello/<name>') 
def hello_name(name): 
    return 'Hello %s!' % name 

def hello_world():
    return 'hello world'
  


if __name__ == '__main__': 
    app.add_url_rule('/', 'hello', hello_world)
    app.run(debug = True) 