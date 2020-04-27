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

    return render_template('index.html' , d = Markup(code))


@app.route('/view', methods=['POST','GET'])
def view():
        if request.method == 'GET':
            url = "https://apismartsekre.herokuapp.com/getstatus"
            data = requests.get(url).json()
            code = ""
            j = 0
            for i in data:
                temp = data[j]
                code = code +"<tr><td>"+str(temp[1])+"</td><td>"
                if str(temp[2]) == 'True':
                    code+= "Terbuka"
                else:
                    code+= "Tertutup"
                code += "</td><td>"
                if str(temp[3]) == 'True':
                    code+= "Menyala"
                else:
                    code+= "Mati"
                code += "</td></tr>"
                j+=1

            url2 = "https://apismartsekre.herokuapp.com/getanggota"
            data2 = requests.get(url2).json()
            code2 = ""
            j2 = 0
            for i2 in data2:
                temp = data[j2]
                code2 = code2 +"<tr><td>"+str(temp[0])+"</td><td>" + str(temp[1])+"</td><td>" +str(temp[2])+ "</td></tr>"
                j2+=1
            print(code2)

            return render_template('view.html',d = Markup(code), e = Markup(code2) )
        else:
            return redirect(url_for('logout'))


if __name__ == '__main__':

    app.run(threaded=True, port=5000)
