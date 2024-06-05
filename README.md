# Introduction
This project demonstrates how to use a pre-trained BERT model to detect phishing emails. By fine-tuning BERT on a dataset of phishing and non-phishing emails, the model can learn to distinguish between the two, providing an effective way to enhance email security.

# Features
- Pre-trained BERT model for natural language understanding.
- Fine-tuning on a dataset of phishing and non-phishing emails.
- Flask-based web server to handle prediction requests.
- Basic HTML, CSS Frontend

# Prerequisites
- Python 3.7 or higher
- Flask
- Transformers (Hugging Face library)
- Torch (PyTorch)

# Installation
**Clone the repository:**
```bash
git clone https://github.com/yourusername/Phising-Detection-model.git
cd Phising-Detection-model
  ```
**Install required packages:**
```bash
pip install -r requirements.txt
```
**Download the BERT model:**
```bash
mkdir -p Backend/model_folder
cd Backend/model_folder
# Download the model files from Hugging Face or another source
```
**Running the Flask Server**
```bash
python Backend/app.py
```


Thank you 🤖
