from flask import Flask
import altair as alt

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Altair data viz demo.'

@app.route('/plot')
def plot():
    return 'Nothing here yet.'

if __name__ == '__main__':
    app.run()
