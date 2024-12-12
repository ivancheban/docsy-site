import os
import json
import markdown
import yaml
import re

def clean_html_content(html_content):
    patterns_to_remove = [
        r'<div id="chatbot-toggle">.*?</script>',  # To remove chatbot HTML and JavaScript snippet
    ]
    for pattern in patterns_to_remove:
        html_content = re.sub(pattern, '', html_content, flags=re.DOTALL)
    return html_content

def get_content(directory, lang_code):
    content = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
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
                    
                    # Convert Markdown to HTML
                    html_content = markdown.markdown(md_content)
                    html_content = clean_html_content(html_content)
                    
                    # Generate URL respecting language code
                    url = '/' + os.path.relpath(os.path.join(root, file), directory).replace('\\', '/')
                    url = url.replace('.md', '/')
                    if lang_code == 'ua':
                        url = f'/ua{url}'
                    
                    # Adjust URL for '_index' pages
                    if url.endswith('_index/'):
                        url = url[:-7] + '/'
                    
                    content.append({
                        'title': title,
                        'content': html_content,
                        'url': url
                    })
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

# Generate JSON files for both English and Ukrainian versions
generate_json(en_dir, en_output, 'en')
generate_json(ua_dir, ua_output, 'ua')

print("JSON generation complete.")