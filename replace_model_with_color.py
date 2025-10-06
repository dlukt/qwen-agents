#!/usr/bin/env python3
"""
Replace 'model: opus' and 'model: sonnet' with 'color: Automatic Color' in all .md files.
"""

import os
import re
from pathlib import Path


def replace_in_file(filepath):
    """Replace model entries with color in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Replace both patterns
        content = re.sub(r'model:\s*opus', 'color: Automatic Color', content)
        content = re.sub(r'model:\s*sonnet', 'color: Automatic Color', content)
        content = re.sub(r'model:\s*haiku', 'color: Automatic Color', content)

        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """Find all .md files and perform replacements."""
    current_dir = Path('.')
    md_files = current_dir.glob('**/*.md')

    modified_count = 0

    for md_file in md_files:
        if replace_in_file(md_file):
            print(f"Modified: {md_file}")
            modified_count += 1

    print(f"\nTotal files modified: {modified_count}")


if __name__ == '__main__':
    main()
