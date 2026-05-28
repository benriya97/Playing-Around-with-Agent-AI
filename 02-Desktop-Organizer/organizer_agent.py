import os
import shutil
from ollama import chat

standard_desktop = os.path.expanduser("~/Desktop")
onedrive_desktop = os.path.expanduser("~/OneDrive/Desktop")
DESKTOP_PATH = onedrive_desktop if os.path.exists(onedrive_desktop) else standard_desktop

OUTPUT_DIR = os.path.join(DESKTOP_PATH, "Organized_Archive")

def extract_file_snippet(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext in ['.txt', '.csv']:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read(150) # Reduced to 150 characters for speed
                
        elif ext == '.pdf':
            from pypdf import PdfReader
            reader = PdfReader(file_path)
            if reader.pages:
                # Only read the first page's text stream
                text = reader.pages[0].extract_text()
                return text[:150] if text else "[Empty PDF]"
                
        elif ext == '.docx':
            import docx
            doc = docx.Document(file_path)
            text = " ".join([p.text for p in doc.paragraphs[:2]]) # Only grab first 2 paragraphs
            return text[:150]
            
        elif ext in ['.xlsx', '.xls']:
            return "[Excel Spreadsheet - Skipping deep text read for speed]"
            
    except Exception:
        return "[Parser Timeout - Using filename instead]"
    return "[Visual Format]"

print("--- ⚡ Turbo Desktop Organizer Activated ⚡ ---")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

files_to_process = []
for root, dirs, files in os.walk(DESKTOP_PATH):
    if OUTPUT_DIR in root:
        continue
    for file in files:
        if file.lower() in ['desktop.ini', 'thumbs.db'] or file.lower().endswith('.lnk'):
            continue
        files_to_process.append((os.path.join(root, file), file))

print(f"🚀 Processing {len(files_to_process)} files with Hardware Restrictions Enabled...\n")

for source_file_path, filename in files_to_process:
    text_context = extract_file_snippet(source_file_path)

    prompt = f"""
    Classify this file into exactly ONE of these categories: 'Finance', 'Resumes', 'Healthcare', 'Visas', 'Education', 'Code', 'Images'.
    Filename: {filename}
    Snippet: {text_context}
    Respond with ONLY the category word. No other text.
    """

    print(f"🧠 AI analyzing: '{filename}'...", end="", flush=True)
    
    try:
        # The speed magic happens right here in the options block
        response = chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}],
            options={
                "num_predict": 5,       # Forces the AI to stop thinking after 5 words max
                "temperature": 0.0      # Makes the AI answer instantly without second-guessing
            }
        )
        category = response["message"]["content"].strip().replace(".", "").replace("'", "")
        if len(category.split()) > 1:
            category = category.split()[0]
        if not category.isalpha():
            category = "Unsorted"
    except Exception:
        category = "Unsorted"

    print(f" ➔ [{category}]")

    target_child_folder = os.path.join(OUTPUT_DIR, category)
    if not os.path.exists(target_child_folder):
        os.makedirs(target_child_folder)

    shutil.copy(source_file_path, os.path.join(target_child_folder, filename))

print("\n🎉 Done! Check your 'Organized_Archive' folder on your Desktop.")