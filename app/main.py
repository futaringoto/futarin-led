from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route("/")
@app.route("/wifi/high",methods=["post"])
def wifi_high():
    return jsonify({"status":"wifi high"}),200
            
            
if __name__ == "__main__":
    app.run(debug=True)