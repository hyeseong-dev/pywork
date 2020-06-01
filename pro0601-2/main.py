from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
   return '''
   <html>
   <body>
   <form action="/login2">
      <input type="text" name="name">
      <input type="text" name="password">
      <input type="submit">
   </form>
   </body>
   </html>
   '''


@app.route('/login1/<name>')
def login1(name):
   return 'welcome %s' % (name)


@app.route('/login2')
def login2():
   name = request.args.get('name');
   pwd = request.args.get('password');
   return 'welcome %s, %s' % (name, pwd)


@app.route('/login3')
def login3():
   name = request.args.get('name');
   pwd = request.args.get('password');   
   return '<html><body>welcome %s, %s</body></html>' % (name, pwd)
   


@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)