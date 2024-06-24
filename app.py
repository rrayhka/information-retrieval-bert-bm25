from flask import Flask, render_template, request, jsonify
from transformers import BertTokenizer, BertModel
from rank_bm25 import BM25Okapi
import pandas as pd
import torch
import pickle
import json
with open('bert_embeddings.pkl', 'rb') as f:
    df = pickle.load(f)
with open('bm25_model.pkl', 'rb') as f:
    bm25 = pickle.load(f)
with open('data/json/all_meta.json') as f:
    meta_data = [json.loads(line) for line in f]
meta_df = pd.DataFrame(meta_data)
df = pd.merge(df, meta_df, on='id')
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/query', methods=['POST'])
def query():
    try:
        user_query = request.form['query']
        tokenized_query = user_query.split()
        scores = bm25.get_scores(tokenized_query)
        best_idx = scores.argmax()
        best_doc = df.iloc[best_idx]
        result = {
            'id': best_doc['id'],
            'text': best_doc['text'],
            'verdict': best_doc['verdict'],
            'indictment': best_doc['indictment'],
            'lawyer': best_doc['lawyer'],
            'owner': best_doc['owner']
        }
        return render_template('results.html', result=result)
    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', error="Error occurred while fetching results.")
if __name__ == '__main__':
    app.run(debug=True, port=5005)
