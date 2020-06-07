from flask import Flask, render_template, request, redirect, session, abort
import dao.member_dao as memberDao

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/member/memberList.html')
def memberList():
    if 'logged_in' in session and session['role'] == 'ADMIN':
        members = memberDao.select_members()
        print(members)
        result = {'members': members}
        return render_template('/member/memberList.html', result=result)
    else:
        abort(401)

@app.route('/member/addMember')
def addMember():
    username = request.args.get('username')
    name = request.args.get('name')
    password = request.args.get('password')    
    memberDao.insert_member(username, password, name)
    return redirect('/member/memberList.html')

@app.route('/member/memberDetail.html')
def memberDetail():
    return render_template('/member/memberDetail.html')

@app.route('/member/addMemberForm.html')
def addMemberForm():
    return render_template('/member/addMemberForm.html')

@app.route('/member/loginForm.html')
def loginForm():
    return render_template('/member/loginForm.html')

@app.route('/member/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    print(password, username)
    member = memberDao.select_member_by_username_and_password(username, password)
    print(member)
    if member is not None:
        if member['username'] == username and member['password'] == password:
            print('logined')
            session['logged_in'] = True
            session['role'] = member['role']
            return redirect('/index.html')
    error = '가입하지 않은 아이디이거나, 잘못된 비밀번호입니다.'
    return render_template('/member/loginForm.html', error=error)

@app.route('/member/logout')
def logout():
    # session.pop('logged_in', None)
    session.clear()
    return redirect('/index.html')

@app.route('/member/setMemberForm.html')
def setMemberForm():
    return render_template('/member/setMemberForms.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/error/404.html'), 404

@app.errorhandler(401)
def page_not_found(e):
    return render_template('/error/404.html'), 401

if __name__ == '__main__':
    app.run(debug = True)