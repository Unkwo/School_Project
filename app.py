from flask import Flask, render_template, request, jsonify
#all the momentous code lies in this file
from hr import *
import pandas as pd
import numpy as np
import requests, json

app  = Flask(__name__, template_folder="./assets/html_and_styling")

excel_file = pd.read_excel("./assets/datasets/Data.xlsx")
data_frame = pd.DataFrame(data["Employee_Name"])
names_array = np.array(data_frame)

@app.route("/")
def home():
    return render_template("page.html")

@app.route("/check")
def check():
    return render_template("check.html")

@app.route("/data", methods=["post"])
def show_data():
    name = request.json.get("name")
    
    if not name:
        return jsonify({
            "status":"error",
            "message":"No name"
        })
        
    else:
        array= check_employee(name)
        try:           
            return jsonify({
                "nom":array[0]
            })
            
        except:
            return jsonify({
                "status":"error",
                "message":"Not found"
            })
    

@app.route("/sort-employees")
def sort():
    arrays = sort_employees()

    render_template("sort.html")

if __name__ == "__main__":
    app.run(debug=True)