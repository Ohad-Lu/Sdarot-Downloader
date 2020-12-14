from flask import Flask, render_template
import logging, os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



@app.route('/about', methods=['GET', 'POST'])
def about():
	return render_template('about.html')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
	return render_template('blog.html')

@app.route('/blog_details', methods=['GET', 'POST'])
def blog_details():
	return render_template('blog_details.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	return render_template('contact.html')

@app.route('/elements', methods=['GET', 'POST'])
def elements():
	return render_template('elements.html')

@app.route('/help', methods=['GET', 'POST'])
def help():
	return render_template('help.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
	return render_template('main.html')

@app.route('/packages', methods=['GET', 'POST'])
def packages():
	return render_template('packages.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	return render_template('register.html')

@app.route('/services', methods=['GET', 'POST'])
def services():
	return render_template('services.html')

@app.errorhandler(404)
def not_found_error(error):
	return '<h1>404 error</h1>'

@app.errorhandler(500)
def internal_error(error):
	return '<h1>500 error</h1>'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
	#logging.basicConfig(filename='logfile.log', level=logging.DEBUG)