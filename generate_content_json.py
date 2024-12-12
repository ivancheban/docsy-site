import os
import json
import markdown
import yaml
import re

def get_content(directory, lang_code):
    content = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        md_content = f.read()
                        
                        # Extract frontmatter
                        frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', md_content, re.DOTALL)
                        if frontmatter_match:
                            frontmatter = yaml.safe_load(frontmatter_match.group(1))
                            title = frontmatter.get('title', '')
                            md_content = md_content[frontmatter_match.end():]
                        else:
                            title = ''

                        # If no title in frontmatter, try to extract from first H1
                        if not title:
                            title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
                            if title_match:
                                title = title_match.group(1)
                            else:
                                title = os.path.splitext(file)[0]  # Use filename as last resort
                        
                        html_content = markdown.markdown(md_content)
                        
                        # Generate URL
                        url = '/' + os.path.relpath(os.path.join(root, file), directory).replace('\\', '/')
                        url = url.replace('.md', '/')
                        if lang_code == 'ua':
                            url = f'/ua{url}'
                        
                        # Remove 'index' from the end of the URL if present
                        if url.endswith('index/'):
                            url = url[:-6]
                        
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