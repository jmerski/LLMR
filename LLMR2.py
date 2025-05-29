import os

def merge_files_to_text(directory, output_file):
    file_count = 0
    total_chars = 0
    
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_count += 1
                # Use relative path for clarity in output
                rel_path = os.path.relpath(file_path, directory)
                outfile.write(f'===== {rel_path} =====\n')
                try:
                    with open(file_path, 'r') as infile:
                        content = infile.read()
                        outfile.write(content)
                        total_chars += len(content) + len(f'===== {rel_path} =====\n') + 2
                except (UnicodeDecodeError, PermissionError):
                    outfile.write('[Non-text file or access denied, skipped]\n')
                    total_chars += len('[Non-text file or access denied, skipped]\n') + len(f'===== {rel_path} =====\n') + 2
                outfile.write('\n\n')
    
    # Estimate tokens (1 token ≈ 5 characters for English text)
    token_count = total_chars // 5
    return file_count, token_count

if __name__ == '__main__':
    directory = input("Enter the target directory path: ")
    output_file = os.path.join(os.getcwd(), 'merged_output.txt')
    if not os.path.isdir(directory):
        print("Invalid directory path.")
    else:
        file_count, token_count = merge_files_to_text(directory, output_file)
        print(f"Files merged into {output_file}")
        print(f"Total files processed: {file_count}")
        print(f"Estimated token count: {token_count}")
