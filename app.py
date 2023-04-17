from flask import Flask, request, render_template, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB("songs.json")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            db.insert({"title": title})
            return redirect(url_for("index"))
    songs = db.all()
    return render_template("index.html", songs=songs)

if __name__ == "__main__":
    app.run(debug=True)
