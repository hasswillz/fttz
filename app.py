from flask import Flask, render_template, url_for

app = Flask(__name__)
#print(__name__)

@app.route('/')
def my_home():
    return render_template ("index.html")

@app.route('/index.html')
def my_homeS():
    return render_template ("index.html")

@app.route('/about_us.html')
def my_about():
    return render_template ("about_us.html")

@app.route('/contact_us.html')
def my_contact():
    return render_template ("contact_us.html")

@app.route('/project.html')
def my_blog():
    return render_template ("project.html")

@app.route('/services.html')
def my_services():
    return render_template ("services.html")

if __name__ == '__main__':
    app.run()
