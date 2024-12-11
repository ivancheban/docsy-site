import os
import json
import markdown

def get_content(directory, lang_code):
    content = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        md_content = f.read()
                        html_content = markdown.markdown(md_content)
                        
                        # Generate URL based on language and handle _index.md files
                        url = os.path.relpath(os.path.join(root, file), directory).replace('\\', '/')
                        if file == '_index.md':
                            url = os.path.dirname(url)
                            title = os.path.basename(os.path.dirname(os.path.join(root, file)))
                        else:
                            url = url.replace('.md', '/')
                            title = file.replace('.md', '')
                        
                        if lang_code == 'ua':
                            url = f'/ua/{url}'
                        else:
                            url = f'/{url}'
                        
                        # Remove any double slashes and ensure a trailing slash
                        url = url.replace('//', '/').rstrip('/') + '/'
                        
                        content.append({
                            'title': title,
                            'content': html_content,
                            'url': url
                        })
                except UnicodeDecodeError:
                    print(f"Warning: Unable to read file {file} with UTF-8 encoding. Skipping this file.")
    return content

def generate_json(content_dir, output_file, lang_code):
    content = get_content(content_dir, lang_code)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print(f"Generated {output_file} with {len(content)} articles.")

# Paths
base_dir = 'content'
static_dir = 'static'
en_dir = os.path.join(base_dir, 'en')
ua_dir = os.path.join(base_dir, 'ua')
en_output = os.path.join(static_dir, 'content-en.json')
ua_output = os.path.join(static_dir, 'content-ua.json')

# Generate JSON files
generate_json(en_dir, en_output, 'en')
generate_json(ua_dir, ua_output, 'ua')

print("JSON generation complete.")