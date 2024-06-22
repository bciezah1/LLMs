# loading libraries

import os
import sys
from datasets import load_dataset 
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from transformers import GenerationConfig 
from transformers import pipeline
print('ready loading data')

# Check Python version
print("Python version:", sys.version)

# Check Conda environment
conda_env = os.environ.get('CONDA_DEFAULT_ENV')
print("Conda environment:", conda_env)

#######################
#text generation
#######################

from transformers import pipeline 

# generation pipeline
generator = pipeline('text-generation',model='gpt2')

# example of text generation
result=generator("Once upon a time,")
print(result)

llm =  pipeline('text-generation')
prompt = "New York city is famous for"
outputs = llm(prompt, max_length=150)
print(outputs[0]['generated_text'])

###############################
# sentiment analysis
###############################
# loading pipeline
from transformers import pipeline

# creating sentiment analysis
classifier = pipeline('sentiment-analysis')

# esxample of sentiment analysis
result =  classifier("I love to programm in Python and R!")
print(result)
