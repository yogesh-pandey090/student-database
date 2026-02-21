from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Save data
@app.route("/save", methods=["POST"])
def save():
    name = request.form["name"]
    email = request.form["email"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, email TEXT)")
    cur.execute("INSERT INTO students VALUES (?, ?)", (name, email))

    conn.commit()
    conn.close()

    return "Data Saved Successfully ✅"

if __name__ == "__main__":
    app.run(debug=True)