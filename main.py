from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/sumsq/<int:value1>/<int:value2>")
def sumsq(value1: int, value2: int) -> None:
    result = value1 ** 2 + value2 ** 2
    return f"<p>Sum of 2 square is {result} </p>"

if __name__ == "__main__":
    app.run(debug=True)