from flask import Flask, render_template
app = Flask(__name__)

@app.route("/noteForm")
def noteForm():
    return render_template("noteForm.html")


@app.route("/noteList")
def noteList():
    return render_template("noteList.html")


if __name__ == '__main__':
    app.run(debug = True)