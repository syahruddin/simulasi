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
        code = code +"<tr><td>"+str(temp[0])+"</td><td>" + str(temp[1]) +  "</td><td>" + "<form action=\"/masuk?id_unit="+ str(temp[0]) +"\") }}\" method=\"POST\"><label for=\"lname\">ID Mahasiswa:</label><input type=\"int\" id=\"id_mahasiswa\" name=\"id_mahasiswa\"><button type=\"submit\" value=\"Submit\">Masuk </button> </form>" + "</td><td>" +  "<form action=\"/keluar?id_unit="+ str(temp[0]) +"\") }}\" method=\"POST\"><label for=\"lname\">ID Mahasiswa:</label><input type=\"int\" id=\"id_mahasiswa\" name=\"id_mahasiswa\"><button type=\"submit\" value=\"Submit\">Keluar </button> </form>" +"</td></tr>"
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

    url = "https://apismartsekre.herokuapp.com/getlog"
    data = requests.get(url).json()
    code3 = ""
    j = 0
    for i in data:
        temp = data[j]
        code2 = code2 +"<tr><td>"+str(temp[0])+"</td><td>" + str(temp[1])+"</td><td>" +str(temp[2])+ "</td><td>" +str(temp[3])+ "</td></tr>"
        j+=1

    return render_template('index.html' , d = Markup(code) ,e = Markup(code2),f= Markup(code3))

@app.route('/masuk', methods=['POST','GET'])
def masuk():
    id_unit = int(request.args['id_unit'])
    id_mahasiswa = int(request.form['id_mahasiswa'])

    url = "https://apismartsekre.herokuapp.com/getanggota?id_unit=" + str(id_unit)
    data = requests.get(url).json()
    ada = False
    j = 0
    for i in data:
        temp = data[j]
        if str(id_mahasiswa) == str(temp[0]):
            ada = True
        j+=1
    if ada:
        req = "https://apismartsekre.herokuapp.com/postbuka?id_unit=" + str(id_unit) + "&id_mahasiswa=" + str(id_mahasiswa)
        a =requests.get(req)

        req = "https://apismartsekre.herokuapp.com/updatestatus?id_unit=" + str(id_unit) + "&status_pintu=1&status_listrik=1"
        a =requests.get(req)



    return redirect(url_for('index'))


@app.route('/keluar', methods=['POST','GET'])
def keluar():
    id_unit = int(request.args['id_unit'])
    id_mahasiswa = int(request.form['id_mahasiswa'])

    url = "https://apismartsekre.herokuapp.com/getanggota?id_unit=" + str(id_unit)
    data = requests.get(url).json()
    ada = False
    j = 0
    for i in data:
        temp = data[j]
        if str(id_mahasiswa) == str(temp[0]):
            ada = True
        j+=1
    if ada:
        req = "https://apismartsekre.herokuapp.com/posttutup?id_unit=" + str(id_unit) + "&id_mahasiswa=" + str(id_mahasiswa)
        a =requests.get(req)

        req = "https://apismartsekre.herokuapp.com/updatestatus?id_unit=" + str(id_unit) + "&status_pintu=0&status_listrik=0"
        a =requests.get(req)



    return redirect(url_for('index'))


if __name__ == '__main__':

    app.run(threaded=True, port=5000)
