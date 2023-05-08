from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

''''''


@app.route('/')
def get_site_location():
    con = mysql.connector.connect(user='root', password='root',
                              host='db', database='whc_db',
                              port=3306)
    cur = con.cursor()
    cur.execute('SELECT DISTINCT site, latitude, longitude FROM sites')
    names = list(map(lambda x: x[0], cur.description))
    ret = jsonify([dict(zip(names, row)) for row in cur.fetchall()])
    cur.close()
    con.close()
    return ret 

if __name__ == '__main__':
    app.run(host='0.0.0.0')