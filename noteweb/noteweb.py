from flask import Flask, render_template, request
app = Flask(__name__)

memos = []

@app.route("/noteForm")
def noteForm():
    return render_template("noteForm.html")


@app.route("/noteList")
def noteList():
    global memos
    
    memo = request.args.get("memo")
    memos.append(memo)

    result = {
        "memos":memos        
        }

    return render_template("noteList.html", result=result)


if __name__ == '__main__':
    app.run(debug = True)