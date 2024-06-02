from flask import Flask, request, render_template
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load tokenizer and model
model_name = "bert-base-uncased"
model_dir = "C:\\Users\\lenovo\\Desktop\\Phising\\Backend\\model_folder"

tokenizer = BertTokenizer.from_pretrained(model_dir)
model = BertForSequenceClassification.from_pretrained(model_dir, num_labels=2)

# Ensure the model is on the right device (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def preprocess_input(text, tokenizer, max_len=128):
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=max_len,
        return_token_type_ids=False,
        padding='max_length',
        return_attention_mask=True,
        return_tensors='pt',
    )
    return {
        'input_ids': encoding['input_ids'].to(device),
        'attention_mask': encoding['attention_mask'].to(device),
    }

def predict_label(text, model, tokenizer, max_len):
    inputs = preprocess_input(text, tokenizer, max_len)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)

    logits = outputs.logits
    predicted_label = torch.argmax(logits, dim=1).item()
    return predicted_label

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            logging.info(f'Received text for prediction: {text}')
            try:
                prediction = predict_label(text, model, tokenizer, 512)
                result = "Phishing" if prediction == 1 else "Not Phishing"
            except Exception as e:
                logging.error(f'Error during prediction: {e}')
                result = 'Error during prediction'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
