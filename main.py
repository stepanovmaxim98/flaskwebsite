from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/modules')
def modules():
    return render_template('modules.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)