import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify
import pickle

df_jd = pd.read_csv('jd.csv')

df_jd=df_jd[['position_title','company_name','model_response']]

model=SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


try:
    with open('jd_embedding','rb') as f:
        data=pickle.load(f)
        jd_embeddings=data['jd_embeddings']
        df_jd=pd.DataFrame(data['df_jd'])
except FileNotFoundError:
    jd_embeddings = model.encode(df_jd['model_response'].tolist(), convert_to_numpy=True,show_progress_bar=True,normalize_embeddings=True)
    with open('jd_embedding','wb') as f:
        pickle.dump({
            'jd_embeddings':jd_embeddings,
            'df_jd': df_jd[['position_title', 'company_name', 'model_response']].to_dict(orient='records')
        },f)
    

app=Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
    try:
        resume = request.json['resume']
        if not resume:
            return jsonify({'error': 'No resume provided'}), 400
        
        resume = " ".join(str(value) for value in resume.values())

        resume_embedding = model.encode(resume, convert_to_numpy=True)

        similarities = cosine_similarity([resume_embedding], jd_embeddings)[0]

        top_indices = similarities.argsort()[-3:][::-1]
        top_matches = df_jd.iloc[top_indices].to_dict(orient='records')

        return jsonify({'matches': top_matches})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
