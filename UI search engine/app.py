from flask import Flask, render_template, request
import search_query
import time

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        start = time.time()
        res = search_query.retrieve_results(query)
        end = time.time()
        return render_template("results.html", data = res.iloc[:, [1, 2]].values, dur = end - start, n = len(res))
    return render_template("index.html")

if __name__ == "__main__":
    app.run()