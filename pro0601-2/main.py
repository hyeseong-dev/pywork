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

@app.route('/login2')
def login3():
   name = request.args.get('name');
   pwd = request.args.get('password');   
   return '<html><body>welcome %s, %s</body></html>' % (name, pwd)
   


if __name__ == '__main__':
   app.run(debug = True)