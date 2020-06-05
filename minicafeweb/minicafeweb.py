from flask import Flask, render_template, request, redirect
app = Flask(__name__)

members = [
    {'username':'gdhong1', 'name':'홍길동1', 'password':1234}, 
    {'username':'gdhong2', 'name':'홍길동2', 'password':1234}, 
    {'username':'gdhong3', 'name':'홍길동3', 'password':1234}, 
    {'username':'gdhong4', 'name':'홍길동4', 'password':1234}, 
    {'username':'gdhong5', 'name':'홍길동5', 'password':1234}, 
    {'username':'gdhong5', 'name':'홍길동5', 'password':1234}, 
    {'username':'gdhong5', 'name':'홍길동5', 'password':1234}, 
    {'username':'gdhong5', 'name':'홍길동5', 'password':1234}, 
    {'username':'gdhong5', 'name':'홍길동5', 'password':1234}, 
]

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/member/memberList.html')
def memberList():   
    result = {'members': members}
    return render_template('member/memberList.html', result=result)


@app.route('/member/addMember')
def addMember():
    username = request.args.get('username')
    name = request.args.get('name')
    password = request.args.get('password')
    member = {'username':username, 'name':name, 'password':password}
    members.append(member)
    return redirect('/member/memberList.html')


@app.route('/member/memberDetail.html')
def memberDetail():
    return render_template('member/memberDetail.html')

@app.route('/member/addMemberForm.html')
def addMemberForm():
    return render_template('member/addMemberForm.html')

@app.route('/member/setMemberForm.html')
def setMemberForm():
    return render_template('member/setMemberForms.html')

if __name__ == '__main__':
    app.run(debug = True)