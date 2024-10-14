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
        operation1 = request.form["operation1"]
        result1 = None
        equation1 = None

        if operation1 == "+":
            result1 = num1 + num2
        elif operation1 == "-":
            result1 = num1 - num2
        elif operation1 == "x":
            result1 = num1 * num2
        elif operation1 == "÷":
            if num2 == 0:
                result1 = "Error: Division by zero"
            else:
                result1 = num1 / num2
        if result1 != None:
            equation1 = str(num1) + " " + operation1 + " " + str(num2) + " = " + str(result1)
    except ValueError:
        result1 = "Invalid input"
        equation1 = result1
        operation1 = None
        num1 = None
        num2 = None

    return render_template(
        "index.html",
        result1=result1,
        equation1=equation1,
        result2=None,
        equation2=None,
        num1=num1,
        num2=num2,
        num3=None,
        operation1=operation1,
        operation2=None
    )

@app.route("/complexCalculation", methods=["POST"])
def complex_calculation():
    try:
        num3 = float(request.form["num3"])
        operation2 = request.form["operation2"]
        result2 = None
        equation2 = None

        if operation2 == "√":
            result2 = num3 ** 0.5
            equation2 = operation2 + " " + str(num3) + " = " + str(result2)
        elif operation2 == " ^ 2":
            result2 = num3 ** 2
            equation2 = str(num3) + operation2 + " = " + str(result2)
        elif operation2 == " ^ 3":
            result2 = num3 ** 3
            equation2 = str(num3) + operation2 + " = " + str(result2)
    except ValueError:
        result2 = "Invalid input"
        equation2 = result2
        operation2 = None
        num3 = None

    return render_template(
        "index.html",
        result1=None,
        equation1=None,
        result2=result2,
        equation2=equation2,
        num1=None,
        num2=None,
        num3=num3,
        operation1=None,
        operation2=operation2
    )

if __name__ == "__main__":
    app.run(debug=True)
