import os
import json
import PyPDF2

def convert_pdfs_to_json(input_dir, output_dir):
    """Converts PDF files in a directory to individual JSON files with structured data."""
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
    print(f"Found {len(pdf_files)} PDF files to process.")  # Debugging output

    for pdf_file in pdf_files:
        input_path = os.path.join(input_dir, pdf_file)
        output_filename = os.path.splitext(pdf_file)[0] + ".json"
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            with open(input_path, 'rb') as pdf_obj:
                pdf_reader = PyPDF2.PdfReader(pdf_obj)
                pages_text = []
                
                for i, page in enumerate(pdf_reader.pages):
                    extracted_text = page.extract_text() or ""
                    cleaned_text = extracted_text.replace('\t', ' ').replace('\r', '')  # Replace tabs with spaces and remove carriage returns
                    page_data = {
                        "page_number": i + 1,
                        "text": cleaned_text
                    }
                    pages_text.append(page_data)

                if not pages_text:  # Debugging output
                    print(f"No text extracted from {pdf_file}.")

            with open(output_path, 'w', encoding='utf-8') as outfile:
                json.dump(pages_text, outfile, ensure_ascii=False, indent=4)
            print(f"Processed {pdf_file} into JSON.")  # Debugging output

        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")  # Catch all exceptions and print them

if __name__ == "__main__":
    input_dir = "NASUNI_DIR"
    output_dir = "OUTPUT_DIR"
    convert_pdfs_to_json(input_dir, output_dir)
