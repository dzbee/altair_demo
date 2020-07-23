from flask import Flask, render_template
import altair as alt
import pandas as pd

from lib.git import get_user_events

app = Flask(__name__)

def count_events(user_data):
    events = pd.DataFrame([{
        'type': event['type'],
        'datetime': pd.Timestamp(event['created_at'])
    } for event in user_data])
    counts = events.groupby([events['datetime'].dt.date, 'type']).count() \
                 .rename(columns={'datetime': 'count'}) \
                 .reset_index().rename(columns={'datetime': 'date'})
    counts['date'] = counts['date'].astype(str)
    return counts

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
