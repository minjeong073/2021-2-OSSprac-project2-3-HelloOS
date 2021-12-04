from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('reservation.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'ossp' or request.form['password'] != 'ossp1234':
            error = 'Incorrect authentication credentails! Please try again'
        else:
            return render_template('reservation.html')
    return render_template('login.html', error=error)


if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
