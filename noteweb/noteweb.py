from flask import Flask, render_template, request
app = Flask(__name__)

memos = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/noteAddForm")
def noteAddForm():
    return render_template("noteAddForm.html")


@app.route("/noteList")
def noteList():
    global memos
    
    memo = request.args.get("memo")
    memos.append(memo)

    result = {
        "memos":memos        
        }

    return render_template("noteList.html", result=result)


@app.route("/noteDetail")
def noteDetail():
    return render_template("noteDetail.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)