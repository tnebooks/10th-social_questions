#!/usr/bin/env python3
import glob
import os
import sys

def main():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions', 'social-science')
    if not os.path.exists(base_dir):
        base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions', 'social')
    if not os.path.exists(base_dir):
        print(f"Error: {base_dir} not found.")
        sys.exit(1)

    # Handle nested subject structure (e.g. social-science/history/chapter) or flat structure
    chapter_dirs = []
    for entry in sorted(os.listdir(base_dir)):
        entry_path = os.path.join(base_dir, entry)
        if os.path.isdir(entry_path):
            sub_entries = [d for d in os.listdir(entry_path) if os.path.isdir(os.path.join(entry_path, d))]
            if sub_entries:
                for sub in sorted(sub_entries):
                    chapter_dirs.append((f"{entry}/{sub}", os.path.join(entry_path, sub)))
            else:
                chapter_dirs.append((entry, entry_path))

    print(f"Found {len(chapter_dirs)} chapters in {os.path.relpath(base_dir)}/:\n")
    print(f"{'#':<3} {'Chapter Slug':<55} {'Questions':<10}")
    print("-" * 70)

    total_questions = 0
    for idx, (display_name, c_path) in enumerate(chapter_dirs, 1):
        q_files = glob.glob(os.path.join(c_path, "*.md"))
        q_count = len(q_files)
        total_questions += q_count
        print(f"{idx:<3} {display_name:<55} {q_count:<10}")

    print("-" * 70)
    print(f"Total Questions across all chapters: {total_questions}\n")

    # Sample preview from first chapter
    if chapter_dirs:
        first_chap_name, first_chap_path = chapter_dirs[0]
        sample_files = sorted(glob.glob(os.path.join(first_chap_path, "*.md")))
        if sample_files:
            print(f"Preview from '{first_chap_name}' ({len(sample_files)} questions):")
            print("=" * 70)
            with open(sample_files[0], 'r', encoding='utf-8') as f:
                print(f.read().strip())
            print("=" * 70)

if __name__ == "__main__":
    main()
