from src.app import getResponse
from transformers import GPT2Config
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("src/model")
model_config = GPT2Config.from_pretrained("src/model/config.json")
model = AutoModelForCausalLM.from_pretrained("src/model/pytorch_model.bin", config=model_config)

def test_get_response():
    prompt = "Hello, model!"

    response = getResponse(prompt, model, tokenizer)
    assert isinstance(response, str)
    assert len(response) > 0
