from flask import Flask, request, jsonify,render_template
from transformers import BertTokenizer, BertForSequenceClassification
import torch

app = Flask(__name__)

# Load tokenizer and model
model_name = "bert-base-uncased"
model_dir = "C:\\Users\\lenovo\\Desktop\\Phising\\Backend\\model_folder"  

tokenizer = BertTokenizer.from_pretrained(model_dir)
model = BertForSequenceClassification.from_pretrained(model_dir, num_labels=2)

# Ensure the model is on the right device (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def preprocess_input(text, tokenizer, max_len):
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

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        if data == "":
            return jsonify({'error' : 'No text Selected'})
        try:
            prediction = predict_label(data,model, tokenizer, 128)
            label = {'prediction' : prediction}
            return jsonify(label)
        except:
            return jsonify({'error' : 'errow during prediction'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
