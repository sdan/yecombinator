from flask import Flask, render_template, request, jsonify, send_from_directory
from vlite import VLite
import json
from typing import Dict, List
import re


app = Flask(__name__)

# Load the VLite database
vdb = VLite("ye_0428")

@app.route('/')
def index():
    return render_template('index.html')


def clean_text(text: str) -> str:
    
    # Split the text into lines
    lines = text.split("\\n")
    
    # Remove empty lines
    lines = [line.strip() for line in lines if line.strip()]
    
    # Join the lines back together with a space separator
    cleaned_text = " ".join(lines)
    
    # Replace multiple spaces with a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    return cleaned_text.strip()  # Remove leading/trailing whitespace

@app.route('/search', methods=['POST'])
def search() -> Dict[str, List]:
    query: str = request.json['query']
    includeLyrics: bool = request.json.get('includeLyrics', False)
    print(f"Received query: {query} with includeLyrics set to {includeLyrics}")
    
    if includeLyrics:
        results = vdb.retrieve(query, top_k=10)
        print(f"Raw results: {results}")
        processed_results = [{'text': clean_text(item[1]), 'date': item[2].get('title', '')} for item in results]
    else:
        raw_results = vdb.retrieve(query, metadata={'type': 'tweet'}, top_k=10, top_k_multiplier=25)
        processed_results = [{'text': clean_text(item[1]), 'date': item[2].get('date', '')} for item in raw_results]
    
    print(f"Processed results: {json.dumps(processed_results)}")
    return jsonify(processed_results)

@app.errorhandler(Exception)
def handle_exception(error):
    # Log the error here if you want
    print(f"[Error] An error occurred: {str(error)}")
    # Return image file on any error
    return send_from_directory('static', 'bajablast.jpg'), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)