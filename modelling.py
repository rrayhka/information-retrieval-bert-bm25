import json
import torch
import pickle
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm
from rank_bm25 import BM25Okapi
from transformers import BertTokenizer, BertModel, AutoModel
data = open('data/json/all.json').read()
list_data = data.split('\n')
dicts = []
for line in list_data:
    if line.strip():  
        data = json.loads(line)
        ids = data.get('id')
        text_tags = data.get('text-tags')
        text = data.get('text')
        if ids and text_tags and text:
            dicts.append({
                'id': ids,
                'text-tags': text_tags,
                'text': text
            })
df = pd.DataFrame(dicts)
def extract_entities(text, tags):
    entities = []
    current_entity = []
    for word, tag in zip(text, tags):
        if tag.startswith('B-'):  
            if current_entity:
                entities.append(' '.join(current_entity))
                current_entity = []
            current_entity.append(word)
        elif tag.startswith('I-') and current_entity: 
            current_entity.append(word)
        else:
            if current_entity:
                entities.append(' '.join(current_entity))
                current_entity = []
    if current_entity:
        entities.append(' '.join(current_entity))
    return entities
df['entities'] = df.apply(lambda row: extract_entities(row['text'], row['text-tags']), axis=1)
tokenizer = BertTokenizer.from_pretrained("indobenchmark/indobert-base-p1")
model = AutoModel.from_pretrained("indobenchmark/indobert-base-p1")
def bert_encode(texts, batch_size=32, max_length=512):
    embeddings = []
    for i in tqdm(range(0, len(texts), batch_size)):
        batch_texts = [' '.join(text) if isinstance(text, list) else text for text in texts[i:i+batch_size]]  
        encoded = tokenizer(batch_texts, padding=True, truncation=True, max_length=max_length, return_tensors='pt')
        with torch.no_grad():
            outputs = model(**encoded)
        embeddings.extend(outputs.last_hidden_state.mean(dim=1).cpu().numpy())
    return embeddings
df['text'] = df['text'].apply(lambda x: ' '.join(x) if isinstance(x, list) else x)  
df['bert_embedding'] = bert_encode(df['text'].tolist(), batch_size=32, max_length=128)
df.to_pickle('bert_embeddings.pkl')
df['bm25_tokens'] = df['text'].apply(lambda x: x.split())
bm25 = BM25Okapi(df['bm25_tokens'].tolist())
with open('bm25_model.pkl', 'wb') as f:
    pickle.dump(bm25, f)
