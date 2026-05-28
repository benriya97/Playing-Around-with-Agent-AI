# Local AI Chatbot with Persistent Memory

An autonomous local chatbot built using Python and Ollama, running the open-source Llama 3 model directly on local hardware. 

## Features
- **100% Local Execution:** No data leaves the host machine, ensuring complete privacy.
- **Context Preservation:** Implements conversational state tracking to maintain context across multi-turn dialogues.
- **Dynamic System Prompting:** Configured with specific role boundaries to act as an adaptive engineering pair.

## Tech Stack
- Python 3
- Ollama API
- Llama 3 (8B LLM)

## How to Run
1. Ensure Ollama is running locally: `ollama run llama3`
2. Install dependencies: `pip install ollama`
3. Run the script: `python app.py`