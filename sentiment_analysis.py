from transformers import pipeline

# Define the model name
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Initialize the classifier pipeline
classifier = pipeline('text-classification', model=model_name)

# Example usage
result = classifier("I love using Hugging Face transformers!")
print(result)