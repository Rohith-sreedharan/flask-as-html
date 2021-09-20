from flask import Flask, request

from processing import calculate_mode

app = Flask(__name__)
app.config["DEBUG"] = True

inputs = []

@app.route("/", methods=["GET", "POST"])
def mode_page():
    errors = ""
    if request.method == "POST":
        try:
            inputs.append(float(request.form["number"]))
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number"])

        if request.form["action"] == "Calculate number":
            result = calculate_mode(inputs)
            inputs.clear()
            return '''
                <html>
                    <body>
                        <p>{result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    if len(inputs) == 0:
        numbers_so_far = ""
    else:
        numbers_so_far = "<p>Numbers so far:</p>"
        for number in inputs:
            numbers_so_far += "<p>{}</p>".format(number)

    return '''
        <html>
            <body>
                {numbers_so_far}
                {errors}
                <p>Enter your number:</p>
                <form method="post" action=".">
                    <p><input name="number" /></p>
                    <p><input type="submit" name="action" value="Add another" /></p>
                    <p><input type="submit" name="action" value="Calculate number" /></p>
                </form>
            </body>
        </html>
    '''.format(numbers_so_far=numbers_so_far, errors=errors)
