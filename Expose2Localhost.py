from flask import Flask, Response
import time

app = Flask(__name__)

# Function to read the content of raw_files3.txt
def read_metrics_file():
    with open('raw_file2.txt', 'r') as f:
        return f.read()

# Route to expose metrics
@app.route('/metrics')
def metrics():
    content = read_metrics_file()
    return Response(content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='localhost', port=9494)

