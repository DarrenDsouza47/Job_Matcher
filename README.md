## Resume Parser and Job Matcher

Application for parsing resume file for experience,organization,degree,skills and using it for finding top 3 job matches using:
1) Spacy 
2) SentenceTransformer
3) Flask
4) Streamlit
5) Spacy-transformer


- Resume Parser parsed the resume to extract features such as tools(skills),experience,degree,organization details

- Embedded the job descriptions using sentence transformer and used cosine similarity to compute similarity between resume parsed features and job descriptions
to get the top 3 ranked jobs


## Running the Code

1)download the model and unzip the model file
```bash
model-link: https://www.dropbox.com/scl/fo/znkpbyldb9e07kyqbfsyn/ABsaqsA64FfOe-Nr0aeknxo?rlkey=pmkc1jtax5a17hsqcwtg7k5j1&st=gc0wf5br&dl=0
```

2) clone the repository(keep the model file in the same project folder)
```bash
git clone https://github.com/DarrenDsouza47/Job_Matcher.git
```

3) install necessary libraries using
```
pip install -r requirements.txt
```
4) Starting the flask server for loading the  job description embeddings
```bash
python setup.py #for starting the flask server 
```
5) run for starting the streamlit server for frontend
```bash
streamlit run app.py for frontend and loading resume parser
```
Note:The Model can be further enhanced for performance for using in production environments.

## output

![image](https://github.com/user-attachments/assets/3eb37ef8-b750-4534-b398-8e3e2a294e5e)

![image](https://github.com/user-attachments/assets/51af99ab-c038-4cd2-93d9-1aeb7dc1c24d)

![image](https://github.com/user-attachments/assets/3613b984-b91a-4296-baf4-4fc3bf8ec196)

![image](https://github.com/user-attachments/assets/03ec76d9-597b-49a3-ae99-4513a38a2de0)

![image](https://github.com/user-attachments/assets/b9c5b835-3b06-4591-8061-ddbbd31323d0)




