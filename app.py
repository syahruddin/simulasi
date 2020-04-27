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
        code = code +"<tr><td>"+str(temp[0])+"</td><td>" + str(temp[1]) +"</td></tr>"
        j+=1


    url = "https://apismartsekre.herokuapp.com/getanggota"
    data = requests.get(url).json()
    code2 = ""
    j = 0
    for i in data:
        temp = data[j]
        code2 = code2 +"<tr><td>"+str(temp[0])+"</td><td>" + str(temp[1])+"</td><td>" +str(temp[2])+ "</td></tr>"
        j+=1


    return render_template('index.html' , d = Markup(code) ,e = Markup(code2))


if __name__ == '__main__':

    app.run(threaded=True, port=5000)
