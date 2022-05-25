from flask import Flask, request, jsonify

StuData=[
         {  'Name':'Sunil Naruka',
            'stu_id':'0',
            'City':'Alwar'},
         {  'Name':'Govind Naruka',
            'stu_id':'1',
            'City':'Jaipur'},
        {   'Name':'Rahul Naruka',
            'stu_id':'2',
            'City':'Kota'},
                 
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
@app.route('/studentadd',methods=['POST'])
def create_stu():
     if request.method == "POST":
      data= { 'Name':'Ram','stu_id':'5','City':'lax'},        
      StuData.append(data)      
      return jsonify({'stu':StuData})

if __name__ == '__main__':
    app.run(debug=True)

