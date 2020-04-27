from flask import Flask, request, jsonify,session, render_template, redirect, url_for, flash,abort, Markup
import requests
import os
app = Flask(__name__)
app.secret_key = 'ha21j3nhhi08jhfd88'
#session['logged_in'] = False

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        return render_template('index.html')

    url = "https://apismartsekre.herokuapp.com/getstatus"
    data = requests.get(url).json()
    code = ""
    j = 0
    for i in data:
        temp = data[j]
        code = code +"<tr><td>"+str(temp[0])+"</td><td>" + str(temp[1]) +  "</td><td>" + "<form action=\"{{ url_for(\"masuk\") }}\" method=\"POST\"><label for=\"lname\">ID Mahasiswa:</label><input type=\"int\" id=\"id_mahasiswa\" name=\"id_mahasiswa\"><button type=\"submit\" value=\"Submit\">Masuk </button> </form>" + "</td><td>" +   "<div class=\"col-md-4\"><a class=\"btn btn-secondary\" href=\"{{ url_for('keluar') }}\">Logout</a></div>" +"</td></tr>"
        j+=1


    url = "https://apismartsekre.herokuapp.com/getanggota?id_unit=1"
    data = requests.get(url).json()
    code2 = ""
    j = 0
    for i in data:
        temp = data[j]
        code2 = code2 +"<tr><td>"+str(temp[0])+"</td><td>" + str(temp[1])+"</td><td>" +str(temp[2])+ "</td></tr>"
        j+=1

    url = "https://apismartsekre.herokuapp.com/getanggota?id_unit=2"
    data = requests.get(url).json()
    j = 0
    for i in data:
        temp = data[j]
        code2 = code2 +"<tr><td>"+str(temp[0])+"</td><td>" + str(temp[1])+"</td><td>" +str(temp[2])+ "</td></tr>"
        j+=1


    return render_template('index.html' , d = Markup(code) ,e = Markup(code2))

@app.route('/masuk', methods=['POST','GET'])
def masuk():
    return 0


@app.route('/keluar', methods=['POST','GET'])
def keluar():
    return 0


if __name__ == '__main__':

    app.run(threaded=True, port=5000)
