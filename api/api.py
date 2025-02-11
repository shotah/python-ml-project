from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Placeholder for your LLM and retrieval logic
# You'll need to integrate your actual LLM, vector database, and retrieval here.

# Sample placeholder data (replace with your actual data)
sample_data = {
    "What is the capital of France?": "Paris",
    "What is the highest mountain in the world?": "Mount Everest",
}

@app.route("/api/answer", methods=["POST"])
def answer_question():
    try:
        data = request.get_json()
        query = data.get("query")

        if not query:
            return jsonify({"error": "Missing 'query' parameter"}), 400

        # Placeholder: Replace with your actual retrieval and LLM logic
        answer = sample_data.get(query)  # Replace with your actual retrieval and LLM logic

        if not answer:
            answer = "I don't know the answer to that question."

        return jsonify({"answer": answer}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get port from environment or default to 5000
    app.run(debug=True, host="0.0.0.0", port=port)  # host="0.0.0.0" makes the API accessible from outside the container