from flask import Flask, request, jsonify


StuData=[
         { 'Name':'Sunil Naruka','stu_id':'0','City':'Alwar'},
         { 'Name':'Govind Naruka','stu_id':'1','City':'Jaipur'},
         { 'Name':'Rahul Naruka','stu_id':'2','City':'Kota'},
                  ]
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
        return "Welcome to course API "

# get all students list 
@app.route('/student',methods=['GET'])
def get():
     return jsonify({'stu':StuData})

# get one student details by id
@app.route('/student/<int:stu_id>',methods=['GET'])
def get_stu(stu_id):
    return jsonify({'stu': StuData[stu_id] } )
    
# add deteails
@app.route('/studentadd',methods=['GET','POST'])

def test():
     if request.method == "GET":
        return jsonify({"response":"Get request call"})
     
     elif request.method == "POST":
        
        req_json = request.json

        t_Id = req_json["stu_id"]
        t_Name = req_json["Name"]
        t_City = req_json["City"]

        return jsonify({ "Id":   t_Id, "Name": t_Name, "City": t_City })
        
if __name__ == '__main__':
    app.run(debug=True)

