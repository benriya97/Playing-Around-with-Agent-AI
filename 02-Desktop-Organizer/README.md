# 🤖 AI-Powered Desktop File Organizer Agent

An autonomous, non-destructive semantic file organization agent built with Python and Llama 3 (via Ollama). This script deep-dives into your Desktop (including OneDrive setups) and safely analyzes text, PDFs, Word documents, and Excel layouts to organize them into intelligent categories.

## 🚀 Features
- **100% Non-Destructive:** Uses a read-and-copy mechanism leaving your original files untouched.
- **Deep-Dive Capabilities:** Crawls loose desktop icons *and* nested subfolders.
- **Omni-Parser:** Reads internal context from `.txt`, `.pdf`, `.docx`, and `.csv` files.
- **Hardware-Optimized:** Constrained token production for lightning-fast local AI inference.

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.x
- **LLM Engine:** Ollama running `llama3`
- **Libraries:** `pypdf`, `python-docx`, `openpyxl`

## 📦 Installation & Setup

1. Clone this repository and navigate to your workspace.
2. Install the required document parsing dependencies:
   ```bash
   pip install pypdf python-docx openpyxl ollama