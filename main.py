from flask import Flask, render_template, request,redirect

app = Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html')


@app.route("/addstock", methods=['GET', 'POST'])
def addstock():
    if request.method == "POST":
        # print to console
        for key, value in request.form.items():
            print(f"{key}: {value}")
        return redirect("/")
    return render_template("addstock.html")


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
