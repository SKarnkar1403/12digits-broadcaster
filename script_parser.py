import os
import re

def clean_and_chunk_text(input_file, words_per_chunk=150):
    """
    Reads a raw text file (notes/essays) and breaks it into perfectly 
    timed script chunks for audio narration.
    """
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Drop your notes here first.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Clean out unwanted formatting symbols or extra whitespaces
    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    words = cleaned_text.split(' ')
    
    print(f"Processing total of {len(words)} words...")
    
    # Chunking loop
    chunk_count = 1
    for i in range(0, len(words), words_per_chunk):
        chunk = " ".join(words[i:i + words_per_chunk])
        print(f"\n--- SCRIPT BLOCK {chunk_count} (Approx. 60 seconds of audio) ---")
        print(chunk)
        chunk_count += 1

if __name__ == "__main__":
    # Placeholder file for testing
    notes_filename = "raw_notes.txt"
    
    # Create a dummy file if it doesn't exist yet
    if not os.path.exists(notes_filename):
        with open(notes_filename, 'w') as f:
            f.write("Welcome to Mission 12digits. This is raw text that our script will parse automatically.")
            
    clean_and_chunk_text(notes_filename)
