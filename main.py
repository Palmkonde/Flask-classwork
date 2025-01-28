from flask import Flask, render_template
from flask import request
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/sumsq/<int:value1>/<int:value2>")
def sumsq(value1: int, value2: int) -> None:
    result = value1 ** 2 + value2 ** 2
    return f"<p>Sum of 2 square is {result} </p>"

@app.route("/plotter", methods=["GET", "POST"])
def plotter() -> None:
    if request.method == "POST":
        x_from = int(request.form["from-x"])
        x_to = int(request.form["to-x"])
        histogram_data = request.form.get("histogram-data", None) 

        function = []
        function_name = ["sin", "cos", "parabola", "sqrt"]
        
        for name in function_name:
            try:
                function.append((name, request.form[name]))
            except Exception as e:
                print(f"Error to get function: {e}")
                
        is_separate_graph = request.form.get("separate-plots", None)
        images = []

        if histogram_data:
            values = [float(v) for v in histogram_data.split(",")]
            plt.hist(values)
            image_name = "static/image/histogram.jpg"
            plt.savefig(image_name)
            plt.close()
            images.append(image_name)

        x = np.linspace(x_from, x_to)
        y = None
        if is_separate_graph:
            for name, _ in function:
                if name == "sin":
                    y = np.sin(x)
                    plt.plot(x, y, label="sin")
                if name == "cos":
                    y = np.cos(x)
                    plt.plot(x, y, label="cos")
                if name == "parabola":
                    y = np.power(x, 2)
                    plt.plot(x, y, label="parabola")
                if name == "sqrt":
                    y = np.sqrt(x)
                    plt.plot(x, y, label="square root")
        
                plt.xlim(x_from, x_to)
                plt.ylim(-10, 10)
                image_name = f"static/image/{name}.jpg"
                plt.savefig(image_name)
                images.append(image_name)
                plt.close()
        else:
            for name, _ in function:
                if name == "sin":
                    y = np.sin(x)
                    plt.plot(x, y, label="sin")
                if name == "cos":
                    y = np.cos(x)
                    plt.plot(x, y, label="cos")
                if name == "parabola":
                    y = np.power(x, 2)
                    plt.plot(x, y, label="parabola")
                if name == "sqrt":
                    y = np.sqrt(x)
                    plt.plot(x, y, label="square root")
            plt.xlim(x_from, x_to)
            plt.ylim(-10, 10)
            plt.legend() 
    
            image_name = "static/image/graph.jpg"
            plt.savefig(image_name)
            images.append(image_name)
            plt.close()

        return render_template("plotter.html", image_path=images)
    else:
        return render_template("plotter.html")

if __name__ == "__main__":
    app.run(debug=True)