
from bottle import route, run, request, static_file, template


@route('/message')
def hello():
    return "JekaLox"

@route("/cars")
def get_cars():
    cars=[
        {"name":"Audi",'price':'5000'}
    ]
    return dict(data=cars)

@route('/msq')
def message():
    name=request.query.name
    age=request.query.age
    return "{0},{1}".format(name,age)
@route('/')
def home():
    cars = [
        {"name": "Audi", 'price': '5000'},
        {"name": "Audi", 'price': '5000'}
    ]
    return template('index.html',root='./',cars=cars)


run(host='localhost',port=8080,debug=True)