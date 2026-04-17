from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result13():
    if request.method == "POST":
        name = request.form.get("name")
        date = request.form.get("date")
        age = request.form.get("age")


        return render_template("result13.html", name=name, date=date, age=age)

    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
