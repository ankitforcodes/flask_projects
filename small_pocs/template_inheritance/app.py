from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
	return render_template('base.html')

@app.route('/index/<name>')
def user(name):
	return render_template('user.html', name = name)



if __name__ == '__main__':
	app.run(debug=True)