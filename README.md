# 🧪 Agentic AI Sandbox

Welcome to my local Agentic AI development lab. This repository is a collection of hands-on projects designed to explore the inner workings of autonomous AI agents, LLM reasoning loops, and local tool integration using open-source models.

Every project here runs entirely locally on consumer hardware, leveraging **Ollama** and **Llama 3** to guarantee privacy, eliminate API costs, and maximize control over the agentic pipeline.

---

## 🗂️ Repository Structure

This workspace is organized into dedicated subfolders, tracking my progression from foundational agent concepts to complex, real-world cloud automation tools.

### 📁 [01-Local-Chatbot](./01-Local-Chatbot/)
- **Purpose:** The foundational project built to understand the core mechanics of Agent AI.
- **Key Concepts:** Context windows, system prompting, conversational loops, and basic memory state tracking.
- **Tech Stack:** Python, Ollama, Llama 3.

### 📁 [02-Desktop-Organizer](./02-Desktop-Organizer/)
- **Purpose:** An autonomous, semantic file organizer that acts as a physical agent on the operating system.
- **Key Concepts:** The **Perceive ➔ Reason ➔ Act** loop, document content extraction (PDF, Word, Excel, CSV), strict token-output constraints for speed, and 100% non-destructive execution.
- **Tech Stack:** Python, Ollama (`llama3`), `pypdf`, `python-docx`, `openpyxl`.

---

## 🛠️ Core Technology Stack

- **LLM Orchestration:** Ollama (running local `llama3` models)
- **Runtime Environment:** Python 3.10+
- **Version Control:** Git & GitHub for repository architecture

---

## 🚀 Getting Started

### Prerequisites
1. Download and install [Ollama](https://ollama.com/).
2. Pull the Llama 3 model via your command line:
   ```bash
   ollama pull llama3
