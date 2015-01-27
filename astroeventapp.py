from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.debug = True
app.secret_key = 'oh a secret key'

@app.route('/')
def index():
    return "<h3>Hello World!<h3>"


if __name__ == '__main__':
    app.run()
