from flask import Flask, request, jsonify
from transformers import pipeline  # Or your preferred LLM library

app = Flask(__name__)

try:
    llm_pipeline = pipeline("text-generation", model="bigcode/starcoder2")
except Exception as e:
    print(f"Error initializing LLM pipeline: {e}")
    exit(1)


@app.route("/llm/generate", methods=["POST"])
def generate_text():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "Missing 'prompt' parameter"}), 400

        # Generate text using the LLM pipeline
        generated_text = llm_pipeline(prompt, max_length=150)  # Adjust max_length as needed

        return jsonify({"response": generated_text[0]["generated_text"]}), 200

    except Exception as e:
        print(f"Error generating text: {e}")
        return jsonify({"error": "Error generating text"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)  # host="0.0.0.0" makes it accessible from Docker