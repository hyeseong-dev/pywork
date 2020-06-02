from flask import Flask, render_template, request

app = Flask(__name__)

contacts = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/addContactForm')
def addContactForm():
    return render_template('addContactForm.html')


@app.route('/contactList')
def contactList():
    global contacts
    name = request.args.get('name')
    phone = request.args.get('phone')
    contact = [name, phone]
    contacts.append(contact)
    result = {'contacts':contacts}
    return render_template('contactList.html', result=result)


app.run(debug = True)