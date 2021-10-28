from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"

@app.route("/sheet/<sheetid>")
def sheet(sheetid):
    return render_template("sheet.html")


if __name__ == "__main__":
    app.run(host="localhost", port=4567, debug=True)