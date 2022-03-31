from flask import Flask, render_template, request, jsonify, redirect
import pymongo
#from mongodb import Class
app = Flask(__name__) # 객체 생성 

conn = pymongo.MongoClient()
mydb = conn.database
Class =mydb.Class

@app.route("/class")
def hello() :
    return "<h1>HELLO CHECKMATE!</h1>"

# Class 추가
@app.route("/class",methods=['POST']) # 라우팅경로
def ClassCreate() :
    if request.method =='POST' :
        data = request.get_json()
        Class.insert_one(data)
        return render_template('Create_class.html')
    
# Class 이름변경
@app.route("/class",methods=['PATCH']) # 라우팅경로
def ClassNameChange() :
    if request.method =='PATCH' :
        data = request.get_json()
        Class.update_one({"ClassIdx" : 3}, 
                {   "$set" :
                    {"name" : data['name']}
                }
            ) 
        return render_template('Create_class.html')

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port = "8080")


