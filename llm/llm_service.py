from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline
import os
import torch

app = Flask(__name__)

# Set HF_HOME to a relative path
HF_HOME = os.path.join(os.path.dirname(__file__), 'models', '.cache')
os.environ["HF_HOME"] = HF_HOME

# Base Model Path
model_base_path = os.path.join(HF_HOME, "models--bigcode--starcoder2-7b")

# Dynamically determine snapshot directory (assuming there's only one or we want the first one)
snapshots_dir = os.path.join(model_base_path, "snapshots")
snapshot_id = os.listdir(snapshots_dir)[0]  # Get the first directory name in snapshots
model_path = os.path.join(snapshots_dir, snapshot_id) # Dynamic model path

# Quantization Configuration
quantization_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)

try:
    tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, local_files_only=True, torch_dtype=torch.float16, quantization_config=quantization_config)
    llm_pipeline = pipeline(
        'text-generation',
        model=model,
        tokenizer=tokenizer,
        device_map="auto",
        do_sample=True
    )
    print("LLM pipeline initialized successfully.")
except Exception as e:
    print(f"Error initializing LLM pipeline: {e}")
    exit(1)


@app.route("/llm/generate", methods=["POST"])
def generate_text():
    try:
        data = request.get_json()
        prompt = data.get("prompt")
        max_tokens = data.get("max_tokens", 200)
        temperature = data.get("temperature", 0.7)
        top_p = data.get("top_p", 0.95)

        if not prompt:
            return jsonify({"error": "Missing 'prompt' parameter"}), 400

        generated_text = llm_pipeline(
            prompt,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )

        return jsonify({"response": generated_text[0]["generated_text"]}), 200

    except Exception as e:
        print(f"Error generating text: {e}")  # Keep the detailed error for debugging
        return jsonify({"error": "Error generating text"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)