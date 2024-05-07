import os
import json
from bs4 import BeautifulSoup

def htm_to_json(input_dir, output_dir):
    """Converts individual HTM files in a directory to separate JSON files.
    Extracts relevant structures and context from the HTML document.
    Args:
        input_dir: Path to the directory containing HTM files.
        output_dir: Path to the directory where the JSON files will be saved.
    You may need to change this depending on the structure of your HTML document    
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    htm_files = [f for f in os.listdir(input_dir) if f.endswith(".htm")]
    
    for htm_file in htm_files:
        input_path = os.path.join(input_dir, htm_file)
        output_file = os.path.splitext(htm_file)[0] + ".json"
        output_path = os.path.join(output_dir, output_file)
        
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as infile:
            soup = BeautifulSoup(infile, 'html.parser')
            
            # Extract the title
            title = soup.title.string if soup.title else ""
            
            # Extract headings (h1 to h6)
            headings = [{"level": int(h.name[1]), "text": h.get_text(strip=True)} for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])]
            
            # Extract paragraphs
            paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
            
            # Extract links
            links = [{"text": a.get_text(strip=True), "url": a.get("href")} for a in soup.find_all("a")]
            
            # Extract images
            images = [{"alt": img.get("alt", ""), "url": img.get("src")} for img in soup.find_all("img")]
            
            # Create the JSON structure
            json_data = {
                "title": title,
                "headings": headings,
                "paragraphs": paragraphs,
                "links": links,
                "images": images
            }
        
        with open(output_path, "w", encoding="utf-8") as outfile:
            json.dump(json_data, outfile, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_dir = "NASUNI_DIR"
    output_dir = "OUTPUT_DIR"
    htm_to_json(input_dir, output_dir)