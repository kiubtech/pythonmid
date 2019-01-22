from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
