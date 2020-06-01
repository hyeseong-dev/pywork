from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/login2')
def login2():
   name = request.args.get('name');
   pwd = request.args.get('password');   
   args = {'name':name, 'pwd':pwd}
   return render_template('login2.html', result=args)
   # return '<html><body>welcome %s, %s</body></html>' % (name, pwd)
   


if __name__ == '__main__':
   app.run(debug = True)