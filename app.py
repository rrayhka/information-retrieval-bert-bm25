import json
import torch
import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

with open('bert_embeddings.pkl', 'rb') as f:
    df = pickle.load(f)
with open('bm25_model.pkl', 'rb') as f:
    bm25 = pickle.load(f)
with open('data/json/all_meta.json') as f:
    meta_data = [json.loads(line) for line in f]
meta_df = pd.DataFrame(meta_data)


unique_courts = df['entities'].apply(lambda x: x[1]).unique()
unique_verdicts = meta_df['verdict'].unique()

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('query')
        court_name = request.form.get('court_name')
        verdict_filter = request.form.get('verdict')

        tokenized_query = query.split()
        scores = bm25.get_scores(tokenized_query)

        if court_name:
            mask = df['entities'].apply(lambda x: x[1] == court_name)
            scores = np.where(mask, scores, 0)
        if verdict_filter:
            mask = meta_df['verdict'] == verdict_filter
            filtered_ids = meta_df[mask]['id'].tolist()
            scores = np.where(df['id'].isin(filtered_ids), scores, 0)

        top_indices = scores.argsort()[-10:][::-1]
        results = df.iloc[top_indices]
        results_dict = results.to_dict(orient='records')
        meta_results_dict = {int(row['id']): row for _, row in meta_df.iterrows() if int(row['id']) in results['id'].tolist()}

        return render_template('results.html', query=query, results=results_dict, meta_results=meta_results_dict)

    return render_template('index.html', courts=unique_courts, verdicts=unique_verdicts)

@app.route('/details/<int:doc_id>')
def details(doc_id):
    document = df[df['id'] == doc_id].iloc[0]
    meta = meta_df[meta_df['id'] == doc_id].iloc[0]
    return render_template('details.html', document=document, meta=meta)

if __name__ == '__main__':
    app.run(debug=True, port=5006)
