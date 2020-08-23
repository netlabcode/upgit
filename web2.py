# all the imports
import os
import sqlite3
import pandas as pd
from flask import Flask, g, render_template
from contextlib import closing

# create our little application :)
app = Flask(__name__)

# configuration
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'test.db'),
))

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def stacked_bar_chart():
    # Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect("test.db")
    df = pd.read_sql_query("SELECT * from substation3", con)

    # verify that result of SQL query is stored in the dataframe
    print(df.to_json())

    con.close()

    xid = df['id'].values.tolist() # x axis
    data1 = df['value1'].values.tolist()
    data2 = df['value2'].values.tolist()

    return render_template('linegraph.html', xid=xid, data1=data1, data2=data2)

if __name__ == '__main__':
    #init_db()
    app.run(debug=True)