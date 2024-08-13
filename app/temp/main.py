from flask import Flask, redirect, render_template, url_for, request, send_file, session, flash, get_flashed_messages
from io import BytesIO, StringIO
from temp.func import read_file
import pandas as pd
import numpy as np


app = Flask(__name__)

app.secret_key = "RapemanBruh"
app.config["DEBUG"] = True



@app.route("/", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        try:
            file = request.files["csv_file"]
            '''if file.content_type != "text/csv":
                flash("invalid_filetype")
                return redirect(url_for("upload")'''
            
            s =str(file.read(), 'utf8')

            data = StringIO(s)

            df = pd.read_csv(data)

            dop = np.array(df)
            
            result = read_file(dop)

            session["file"] = result
            flash(result)
            return redirect(url_for('table'))
        except:
            flash("invalid-upload")
            return redirect(url_for("upload"))
    
    session["file"] = None
    return render_template("upload.html")

@app.route("/table", methods=["POST", "GET"])
def table():
    length = None if session["file"] == None else len(session["file"])
    return render_template("table.html", abse=session["file"], lene=length)




@app.errorhandler(404)
def error_handler(e):
    return render_template("404.html")




if __name__ == "__main__":
    app.run(port=5050)