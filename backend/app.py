import os
import subprocess
from flask import Flask,redirect,request
import flask
import json
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

#Initializing all the paths
path = "/backend/upload"
path_python = "python3"
code_path = "/backend/SRXSA-CLI.py"
filename = " "

#API for uploading the file
@app.route('/')
def server():
    return "Running Backend Server"
@app.route('/api/upload', methods=["GET","POST"])
def file_upload():
    if request.method == "POST":

        if request.files:

            file = request.files["file"]

            file.save(os.path.join(path, file.filename))

            message="File uploaded successfully"

            global filename
            filename = file.filename

            print(message)

            return redirect("http://localhost:8081/query.html")
        else:
            #print("Request.files=false")
            return flask.jsonify(message="File not uploaded")
    else:
        return flask.jsonify(message="GET method is used instead of POST")

#Fetching top src-ip from data
def return_src_ip():
    global filename
    data = dict()
    mycmd = path_python + " " + code_path + " " + "-f" + path + "/" + filename + " " + "--src-ip"
    data['src_ip'] =  "<pre>"+subprocess.getoutput(mycmd)+"</pre>"
    return data

#Fetching top dst-ip from data
def return_dst_ip():
    global filename
    data = dict()
    mycmd = path_python + " " + code_path + " " + "-f" + path + "/" + filename + " " + "--dst-ip"
    data['dst_ip'] =  "<pre>"+subprocess.getoutput(mycmd)+"</pre>"
    return data

#Fetching top packets from data
def return_packets():
    global filename
    data = dict()
    mycmd = path_python + " " + code_path + " " + "-f" + path + "/" + filename + " " + "--packets"
    data['packets'] =  "<pre>"+subprocess.getoutput(mycmd)+"</pre>"
    return data

#Fetching top bytes from data
def return_bytes():
    global filename
    data = dict()
    mycmd = path_python + " " + code_path + " " + "-f" + path + "/" + filename + " " + "--bytes"
    data['bytes'] = "<pre>"+subprocess.getoutput(mycmd)+"</pre>"
    return data

#Fetching top policy from data
def return_policy():
    global filename
    data = dict()
    mycmd = path_python + " " + code_path + " " + "-f" + path + "/" + filename + " " + "--policy"
    data['policy'] = "<pre>"+subprocess.getoutput(mycmd)+"</pre>"
    return data

#Fetching top session timeout from data
def return_timeout():
    global filename
    data = dict()
    mycmd = path_python + " " + code_path + " " + "-f" + path + "/" + filename + " " + "--session"
    data['timeout'] = "<pre>"+subprocess.getoutput(mycmd)+"</pre>"
    return data

#API returning the output
@app.route('/api/output',methods=["GET"])
def output():

    output_data = dict()

    output_data.update(return_src_ip())
    output_data.update(return_dst_ip())
    output_data.update(return_packets())
    output_data.update(return_bytes())
    output_data.update(return_policy())
    output_data.update(return_timeout())

    with open('/output.json','w') as outfile:
        json.dump(output_data,outfile,indent=4)

    with open('/output.json','r') as outfile:
        data = json.load(outfile)
    return data

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=6969)