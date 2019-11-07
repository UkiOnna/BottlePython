from bottle import route, run, request, static_file, template, get, post, redirect
from peewee import *

messages = []


@route('/')
def home():
    contacts = [
        {'name': 'John', 'surname': 'Doe', 'phone-number': '870007078979', 'address': 'Abay 1', },
        {'name': 'Sam', 'surname': 'Smith', 'phone-number': '87777899456', 'address': 'Esil 27', },
    ]
    return template('index.html', root='./', contacts=contacts, messages=messages)


@get('/message')
def message():
    return template('form.html', root='./')


@post('/message')
def getMessage():
    message = {
            'name': request.forms.get('name'),
            'phone': request.forms.get('phone'),
            'message': request.forms.get('message')
        }

    messages.append(message)
    print(message)
    redirect("/")


run(host='localhost', port=8080, debug=True)
