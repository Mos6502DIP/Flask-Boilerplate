from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def privacy():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
