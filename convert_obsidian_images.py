import re
import sys

def convert_obsidian_images(md_text):
    # Matches ![[image.png]] and replaces with ![image.png](/images/image.png)
    pattern = r'!\[\[(.+?)\]\]'
    return re.sub(pattern, r'![\1](/images/\1)', md_text)

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    converted = convert_obsidian_images(content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(converted)

    print(f"Converted image links in {filename}")
