import os

def remove_ts_comments(line):
    in_single_quote = False
    in_double_quote = False
    escaped = False
    i = 0

    while i < len(line):
        char = line[i]

        if char == '\\':  # escape next character
            escaped = not escaped
            i += 1
            continue

        if not escaped:
            if char == "'" and not in_double_quote:
                in_single_quote = not in_single_quote
            elif char == '"' and not in_single_quote:
                in_double_quote = not in_double_quote
            elif char == '/' and i + 1 < len(line) and line[i + 1] == '/' and not in_single_quote and not in_double_quote:
                return line[:i].rstrip() + '\n'

        escaped = False
        i += 1

    return line

def delete_ts_style_comments(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            modified_lines = [remove_ts_comments(line) for line in f]
    except Exception as e:
        print(f"[READ ERROR] {file_path}: {e}")
        return

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(modified_lines)
        print(f"[OK] Cleaned: {file_path}")
    except Exception as e:
        print(f"[WRITE ERROR] {file_path}: {e}")

def process_directory_recursive(root_dir):
    print(f"Scanning directory and subdirectories: {root_dir}")
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.ts') or filename.endswith('.tsx'):
                full_path = os.path.join(dirpath, filename)
                delete_ts_style_comments(full_path)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    process_directory_recursive(script_dir)
