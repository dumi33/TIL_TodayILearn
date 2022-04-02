import json
from sre_constants import SUCCESS
from flask import Flask, make_response, render_template, request, jsonify, redirect
import pymongo
from tkinter import filedialog
#from ai_model import Embedding
#from mongodb import Class
app = Flask(__name__) # 객체 생성 

from model2 import please

conn = pymongo.MongoClient()
mydb = conn.database
Class =mydb.Class
Student =mydb.Student


please.hi()

@app.route("/class")
def hello() :
    return "<h1>HELLO CHECKMATE!</h1>"

def AddStduentImg () :
            dir_path = filedialog.askdirectory(initialdir="/",title='Please select a directory')
            return dir_path
        
        
#  auto increment
@app.route("/student/auto")
def getNextSequence() :
    auto =Student.update_one(
        {"studentIdx" : "stdIdx"},
        {
            "$set" : 
                {"seq" :1}
        }
    )
    data = jsonify(auto)
    return  data
        
# Class 추가
@app.route("/classes",methods=['POST']) # 라우팅경로
def ClassCreate() :
    if request.method =='POST' :
        data = request.get_json()
        Class.insert_one(data)
        return make_response(jsonify(SUCCESS=True),200)
    
# Class 이름변경
@app.route("/classes/<int:classIdx>",methods=['PATCH']) # 라우팅경로
def ClassNameChange(classIdx) :
    if request.method =='PATCH' :
        data = request.get_json()
        Class.update_one({"classIdx" : classIdx}, 
                {   "$set" :
                    {"name" : data['name']}
                }
            ) 
        return make_response(jsonify(SUCCESS=True),200)

# student 추가 
@app.route("/students",methods=['POST']) # 라우팅경로
def CreateStduentEmbedding() :
    if request.method =='POST' :
        Img_students_addr = AddStduentImg()
        evaluation_embs, evaluation_labels = Embedding.Create_Embedding(Img_students_addr)
        
        for i in range(len(evaluation_labels)) : 
            Student.insert_one(
                {
                    "studentIdx" : getNextSequence(),
                    "name": evaluation_labels[i],
                    "embedding" : evaluation_embs[i]
                }
            ) 
        # data = request.get_json(data)
        
        return make_response(jsonify(SUCCESS=True),200)
    

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port = "8080")
