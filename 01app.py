from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def demo_api():

  # return "Hello nipl API"
  
  return jsonify(data="hello rest api")

if __name__ == '__main__':
    app.run(debug=True)