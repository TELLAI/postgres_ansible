import psycopg2
from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()
host = 'localhost'
dbname = 'test_ansible'
user = 'youcef'
password = 'pw'
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)

@app.route('/', methods=['GET', 'POST'])
def Home():
    result = "salut"
    return jsonify(result)

@app.route('/inc', methods=['GET', 'POST'])
def Insert():
    cur = conn.cursor()
    data = "test"
    cur.execute("INSERT INTO test2(num_test) VALUES(100);")
    result = "insertion data"
    return jsonify(result)

@app.route('/id', methods=['GET', 'POST'])
def Recup():
    cur = conn.cursor()
    cur.execute("select max(id) from test2;")
    result = cur.fetchall()
    return jsonify(result)

if __name__== "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
