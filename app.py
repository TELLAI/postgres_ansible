from flask import Flask, jsonify
import psycopg2
app = Flask(__name__)

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
    cur.execute("CREATE TABLE IF NOT EXISTS test2 (id serial PRIMARY KEY, num_test int)")
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
