import os
import mimetypes

def is_code_file(file_path):
    """Check if the file is a code file based on its extension."""
    code_extensions = {".js", ".jsx", ".ts", ".tsx", ".php", ".html", ".css", 
                       ".py", ".c", ".cpp", ".java", ".cs", ".go", ".sh", ".rb",
                       ".json", ".xml", ".yml", ".yaml", ".sql", ".md", ".txt"}
    return any(file_path.endswith(ext) for ext in code_extensions)

def extract_codes(directory):
    """Extract code from files and save it to extracted_codes.txt."""
    extracted_codes = []
    non_text_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_type, _ = mimetypes.guess_type(file_path)

            if is_code_file(file_path) or (file_type and file_type.startswith("text")):
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        code_content = f.read()
                        extracted_codes.append(f"\n\n--- {file_path} ---\n{code_content}")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
            else:
                non_text_files.append(file_path)

    # Save extracted code to a file
    with open("extracted_codes.txt", "w", encoding="utf-8") as f:
        f.writelines(extracted_codes)

    # Print non-text files (e.g., images, videos, etc.)
    for non_text_file in non_text_files:
        print(f"Non-text file found: {non_text_file}")

    print("\nExtraction complete. Check extracted_codes.txt")

# Change this to your directory path
directory = "/home/bashira/Music/agentsending-main/"
extract_codes(directory)
