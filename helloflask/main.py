from flask import Flask
app = Flask(__name__)

@app.route('/index.html')
def home():
    html = '';

    for i in range(100):
        html += '<h3><a href="/menu/blog'+str(i)+'.html">Blog'+str(i)+'<a></h3>\n'        

    html='''
    <html>
    <body>
    <h1>Flask Site</h1>
    '''+html+'''
    <h3><a href="/menu/cafe.html">Cafe<a></h3>
    <h3><a href="https://www.naver.com/">naver<a></h3>    
    </body>
    </html>
    '''
    return html

@app.route('/menu/<name>.html')
def menu(name):
    return '<html><body><h3>Flask '+name+' Main<h3></body></html>'

@app.route('/menu/blog.html')
def blog():
    return '<html><body><h3>Flask Blog Main<h3></body></html>'

@app.route('/menu/cafe.html')
def cafe():
    return '<html><body><h3>Flask Cafe Main<h3></body></html>'

#app.run()
# app.run(debug=True, host='218.51.230.100', port='5000')
app.run(debug=True)