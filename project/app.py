from flask import *

app = Flask(__name__)
s = '-'


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here

    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    mydict = {'First Name': request.form.get('First Name'), 'Last Name': request.form.get('Last Name'),
              'User Name': request.form.get('uname'), 'Password': request.form.get('password'),
              'Gender':request.form.get('myGender'),
              'Hobbies': s.join(request.form.getlist('hobby')), 'Country': request.form.get('country'),
              'Address':request.form.get("address")}

    return render_template("result.html", result=mydict)

if __name__ == '__main__':
    app.run(debug=True)
