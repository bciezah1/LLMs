input_text = "Este curso sobre LLMs se está poniendo muy interesante"

# Define pipeline for Spanish-to-English translation
translator = pipeline("translation_es_to_en", model=model_name)

# Translate the input text
translations = translator(input_text)

# Access the output to print the translated text in English
print(translations[0]['translation_text'])
