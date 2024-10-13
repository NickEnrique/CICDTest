from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", result1=None, result2=None)

@app.route("/basicCalculation", methods=["POST"])
def basic_calculation():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation1"]

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "division":
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
    except ValueError:
        result = "Invalid input"

    return render_template("index.html", result1=result, result2=None)

@app.route("/complexCalculation", methods=["POST"])
def complex_calculation():
    try:
        num = float(request.form["num3"])
        operation = request.form["operation2"]

        if operation == "squareroot":
            result = num ** 0.5
        elif operation == "square":
            result = num ** 2
        elif operation == "cube":
            result = num ** 3
    except ValueError:
        result = "Invalid input"

    return render_template("index.html", result1=None, result2=result)

if __name__ == "__main__":
    app.run(debug=True)
