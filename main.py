from flask import Flask, render_template, request, jsonify
from vlite2 import VLite2
import json

app = Flask(__name__)

# Load the VLite2 database
vdb = VLite2(vdb_name="ye_tweets")

@app.route('/')
def index():
    return render_template('index.html')
from typing import Dict, List
@app.route('/search', methods=['POST'])
def search() -> Dict[str, List]:
    query: str = request.json['query']
    includeLyrics: bool = request.json.get('includeLyrics', False)
    print(f"Received query: {query} with includeLyrics set to {includeLyrics}")
    filtered_results = []
    top_k = 10
    attempts = 0
    while len(filtered_results) < 10 and attempts < 5:  # Limit attempts to prevent infinite loop
        results: Dict[str, List] = vdb.retrieve(text=query, top_k=top_k, get_metadata=True)
        print(f"Retrieved {len(results['texts'])} results from the database")
        for text, metadata in zip(results['texts'], results['metadata']):
            if len(filtered_results) >= 10:
                break  # Stop if we have enough results
            if includeLyrics:
                if metadata and 'artist' in metadata:
                    print(f"Including text with metadata: {metadata}")
                    filtered_results.append(text)
                else:
                    print(f"Excluding text due to missing or incorrect artist in metadata: {metadata}")
            else:
                if not metadata or 'artist' not in metadata:
                    print(f"Including text without artist in metadata: {metadata}")
                    filtered_results.append(text)
                else:
                    print(f"Excluding text due to presence of artist in metadata: {metadata}")
        top_k += 5  # Increase the number of results to retrieve in the next attempt
        attempts += 1
    print(f"Type of results: {type(results)}")
    print(f"Filtered Results: {filtered_results}")
    if filtered_results:
        print(f"First text: {filtered_results[0]}")
    return jsonify(filtered_results)
if __name__ == '__main__':
    app.run(debug=True, port=5001)