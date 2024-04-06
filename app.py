from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


# @app.route('/css/styles')
# def styles():
#     return render_template('styles.css')

if __name__ == '__main__':
    app.run()
