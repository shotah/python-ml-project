# python-ml-project

A quick and dirty RAG ML implementation for question answering and information retrieval.

## Description

This project demonstrates a basic Retrieval Augmented Generation (RAG) pipeline. It combines a pre-trained Large Language Model (LLM) with a vector database and retrieval mechanism to answer questions based on a given context. It uses Sentence Transformers to generate embeddings, FAISS for efficient retrieval, and [Specify your LLM, e.g., Llama 2, GPT-3.5-turbo] for text generation. This implementation is designed for educational purposes and can be extended for more complex RAG applications.

## Key Features

- Uses Sentence Transformers for generating text embeddings.
- Efficient retrieval with FAISS.
- LLM-powered text generation ([Specify your LLM]).
- API endpoints for easy integration with other applications.
- Simple web UI for interactive testing.
- Dockerized for easy setup and deployment.
- GPU acceleration (if CUDA drivers are installed).

## Installation

1.  **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd python-ml-project
    ```

2.  **WSL (if applicable):** This project is designed to run in Windows Subsystem for Linux (WSL) 2. Ensure you have WSL 2 installed and a Linux distribution (e.g., Ubuntu 20.04 or 22.04 LTS) set up.

3.  **CUDA Drivers (WSL - Optional, for GPU acceleration):**

    - If you want to use your NVIDIA GPU for faster processing, install the appropriate CUDA drivers in your WSL distribution.
    - Download the appropriate CUDA drivers for your NVIDIA GPU and Ubuntu version from: [https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local) (We recommend Ubuntu 20.04 or 22.04 LTS). Use the `local` installer.
    - Follow the NVIDIA instructions to install the drivers _inside_ your WSL distribution. Remember to install the `cuda-toolkit-12-8` package (or similar) and add the CUDA paths to your `.bashrc` or `.zshrc`.
    - Reboot WSL after installation: `wsl --shutdown` and `wsl -d Ubuntu`
    - Verify: `nvcc --version`

4.  **Docker Desktop for Windows:** Install and configure Docker Desktop for Windows. Ensure it is using the WSL 2 backend.

5.  **Build and Run:**

    ```bash
    docker-compose up -d
    ```

6.  **Environment Variables:** Create a `.env` file in the root directory of your project and set the necessary environment variables. For example:

    ```
    OPENAI_API_KEY=<your_openai_api_key>  # If using OpenAI API
    MODEL_PATH=/app/models/your_llm_model # Path to your LLM model files within the container
    VECTOR_DB_PATH=/data/my_vector_db # Path to your vector database files
    ```

## Project Structure

python-ml-project/
├── .devcontainer/ # Dev container configuration
│   └── devcontainer.json
├── .gitignore
├── .vscode/ # VS Code settings
│   ├── extensions.json
│   └── settings.json
├── README.md
├── api/ # API code (Flask or FastAPI)
│   ├── app.py
│   ├── dockerfile
│   └── requirements.txt (or pipfile/pipfile.lock)
├── docker-compose.yml
├── llm/ # LLM service
│   ├── llm_service.py
│   ├── dockerfile
│   ├── requirements.txt (or pipfile/pipfile.lock)
│   └── models/ # LLM model files go here
├── vector_db/ # Vector database configuration
│   └── dockerfile
│   └── requirements.txt (or pipfile/pipfile.lock, optional)
└── webui/ # Web UI code
    └── dockerfile
    └── package.json (and other web UI files)

## Usage

### API

Describe how to use your API endpoints. Provide example `curl` commands or Python `requests` code snippets. For example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "What is the capital of France?"}' http://localhost:5000/api/answer
```
