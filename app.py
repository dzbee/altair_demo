from flask import Flask, render_template
import altair as alt

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Altair data viz demo.'

@app.route('/plot')
def plot():
    chart = alt.Chart('/static/data/diam_data.json').encode(
        x='carat:Q',
        y='price:Q',
        color='cut:N'
    ).mark_point()

    return render_template('plot.html',
                           chart=chart.to_json())

if __name__ == '__main__':
    app.run()
