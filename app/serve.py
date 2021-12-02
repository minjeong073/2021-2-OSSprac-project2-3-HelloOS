from flask import Flask, render_template, request, flash, make_response

app = Flask(__name__)
app.secret_key = '비밀번호'

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/login', method = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        id = request.form.get('username')
        pw = request.form.get('password')

        if id == "":
            flash('Please input ID')
            return render_template('login.html')
        elif pw == "":
            flash('Please input PW')
            return render_template('login.html')
        elif request.form['username'] != 'ossp' or request.form['password'] != 'ossp1234':
            flash('Incorrect authentication credentials! Please try again')
            return render_template('login.html')
    else :
        return render_template('reservation.html')

@app.route('/reservation', method = ['POST', 'GET'])
def reservation():
    if request.method == 'POST':
        return render_template('submit.html')

@app.route('/submit', method = ['POST', 'GET'])
def submit():
    name = request.form.get('Name')
    date = request.form.get('Date')
    time = request.form.get('time')
    number = request.form.get('Number')

    return render_template('submit.html', )

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
