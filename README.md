## Resume Parser and Job Matcher

Application for parsing resume file for experience,organization,degree,skills and using it for finding top 3 job matches using:
1) Spacy 
2) SentenceTransformer
3) Flask
4) Streamlit

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
