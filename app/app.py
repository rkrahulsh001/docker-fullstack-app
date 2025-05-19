from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Flask App is running with PostgreSQL + Monitoring"

@app.route('/db')
def db_check():
    try:
        conn = psycopg2.connect(
            host="db",
            database="testdb",
            user="testuser",
            password="testpass"
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        conn.close()
        return f"Database time: {result[0]}"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

