import argparse
from pathlib import Path

from fasthtml.components import html2ft

def main(file):
    content = open(file, 'r').read()
    assert content
    tags = html2ft(content)
    print(str(tags))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="HTML to FT converter.")
    parser.add_argument('filename', help='HTML document to convert')

    args = parser.parse_args()
    document = Path(args.filename)
    main(document)
