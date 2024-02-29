from flask import Flask, render_template, request, jsonify
from vlite2 import VLite2
import json

app = Flask(__name__)

# Load the VLite2 database
vdb = VLite2(vdb_name="ye_tweets")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    results = vdb.retrieve(text=query, top_k=10, get_metadata=True)
    return jsonify(results['texts'])

if __name__ == '__main__':
    app.run(debug=True)