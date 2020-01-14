import os
import pandas as pd
import pandas_profiling
from flask import Flask, render_template, request
os.chdir("C:/Users/ADA74/OneDrive - Sky/Documents/Python/MyApp2/app")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/success', methods=['GET','POST'])
def success_table():
    global filename
    if request.method=="POST":
        file=request.files['file']
        try:
            df=pd.read_csv(file)
            profile = pandas_profiling.ProfileReport(df)
            if os.path.exists("./Templates/output.html"):
                os.remove("./Templates/output.html")
            profile.to_file(outputfile = "./Templates/output.html")
            return render_template('output.html')
        except Exception as e:
            return render_template('index.html', text = str(e))

if __name__ == '__main__':
    app.run()