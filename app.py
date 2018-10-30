from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.utcnow()
    then = now - timedelta(hours = 12)
    return render_template('index.html', then=then)

if __name__ == "__main__":
    app.run(host='0.0.0.0')