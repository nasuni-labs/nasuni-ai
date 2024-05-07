import os
from bs4 import BeautifulSoup

def htm_to_text(input_dir, output_dir):
    """Converts individual HTM files in a directory to separate text files.
    ***Removes HTML structures and leaves plain text
    Args:
        input_dir: Path to the directory containing HTM files.
        output_dir: Path to the directory where the text files will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    htm_files = [f for f in os.listdir(input_dir) if f.endswith(".htm")]
    
    for htm_file in htm_files:
        input_path = os.path.join(input_dir, htm_file)
        output_file = os.path.splitext(htm_file)[0] + ".txt"
        output_path = os.path.join(output_dir, output_file)
        
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as infile:
            soup = BeautifulSoup(infile, 'html.parser')
            text = soup.get_text(separator="\n\n", strip=True)
        
        with open(output_path, "w", encoding="utf-8") as outfile:
            outfile.write(text)

if __name__ == "__main__":
    input_dir = "NASUNI_DIR"
    output_dir = "OUTPUT_DIR"
    htm_to_text(input_dir, output_dir)
