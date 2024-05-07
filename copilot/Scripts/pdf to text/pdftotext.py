import os
import PyPDF2

def convert_pdfs_to_text(input_dir, output_dir):
    """Converts PDF files in a directory to individual text files."""
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]
    print(f"Found {len(pdf_files)} PDF files to process.")  # Debugging output

    for pdf_file in pdf_files:
        input_path = os.path.join(input_dir, pdf_file)
        output_filename = os.path.splitext(pdf_file)[0] + ".txt"
        output_path = os.path.join(output_dir, output_filename)
        
        try:
            with open(input_path, 'rb') as pdf_obj:
                pdf_reader = PyPDF2.PdfReader(pdf_obj)
                text = ""
                for page in pdf_reader.pages:
                    extracted_text = page.extract_text() or ""
                    text += extracted_text

                if not text:  # Debugging output
                    print(f"No text extracted from {pdf_file}.")
            
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.write(text)
            print(f"Processed {pdf_file}.")  # Debugging output

        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")  # Catch all exceptions and print them

if __name__ == "__main__":
    input_dir = "NASUNI_DIR"
    output_dir = "OUTPUT_DIR"
    convert_pdfs_to_text(input_dir, output_dir)
