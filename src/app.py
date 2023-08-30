from transformers import GPT2Config
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("./src/model")
model_config = GPT2Config.from_pretrained("./src/model/config.json")
model = AutoModelForCausalLM.from_pretrained("./src/model/pytorch_model.bin", config=model_config)

def getResponse(prompt, model, tokenizer):
    # Create a text generation pipeline
    text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

    # Generate text using the fine-tuned model
    generated_text = text_generator(prompt, max_length=150, num_return_sequences=1)

    return generated_text[0]['generated_text']

def chatbot_response(msg):
    res = getResponse(msg, model, tokenizer)
    return res


from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)