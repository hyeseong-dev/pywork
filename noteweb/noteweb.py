from flask import Flask, render_template, request, redirect
app = Flask(__name__)

memos = [
    'memo1', 
    'memo2', 
    'memo3'
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/noteAddForm")
def noteAddForm():
    return render_template("noteAddForm.html")


@app.route("/addNote")
def addNote():
    global memos    
    memo = request.args.get("memo")
    memos.append(memo)
    return redirect("/noteList")


@app.route("/noteList")
def noteList():
    result = {
        "memos":memos        
        }
    return render_template("noteList.html", result=result)


@app.route("/noteDetail")
def noteDetail():
    index = request.args.get('index')
    memo = memos[int(index)]
    result = {'index':index, 'memo':memo}
    return render_template('noteDetail.html', result=result)


@app.route("/noteSetForm")
def noteSetForm():
    index = request.args.get('index')
    memo = memos[int(index)]
    result = {'index':index, 'memo':memo}
    return render_template('noteSetForm.html', result=result)


@app.route("/setNote")
def setNote():
    index = request.args.get("index")
    memo = request.args.get("memo")
    memos[int(index)] = memo
    return redirect("/noteList")


@app.route("/delNote")
def delNote():
    index = request.args.get("index")
    # memos.remove(int(index))
    del memos[int(index)]
    return redirect("/noteList")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)