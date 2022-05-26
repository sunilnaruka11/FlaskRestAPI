from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test',methods=['GET','POST'])

def test():
    if request.method == "GET":
        return jsonify({"response":"Get request call"})

    elif request.method == "POST":
        
        req_json = request.json

        t_Id = req_json["p_id"]
        t_Name = req_json["name"]
        t_City = req_json["city"]

        return jsonify({ "Id":   t_Id,
                         "Name": t_Name,
                         "City": t_City
                         })


if __name__ == '__main__':
    app.run(debug=True)