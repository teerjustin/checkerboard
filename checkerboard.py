from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/4')
def eight_by_four():
    return render_template("eightbyfour.html")

@app.route('/<int:x>/<int:y>')
def userBoard(x, y):
    return render_template("index2.html", x = x, y = y)

if __name__=="__main__":
    app.run(debug=True)