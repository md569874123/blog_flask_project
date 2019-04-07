from flask import Flask, render_template
from flask import abort
from flask_script import Manager


app = Flask(__name__)
# manager = Manager(app)

@app.route("/")
def index():
    # return '<h1>Hello World!</h1>'
    return render_template('index.html')


@app.route("/user/<name>")
def user(name):
    # abort(404)
    # return '<h1>Hello %s!</h1>' % name
    return render_template('user.html',name = name)


if __name__ == '__main__':
    app.run(debug = True)
    # manager.run()