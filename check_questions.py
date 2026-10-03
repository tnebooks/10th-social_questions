#!/usr/bin/env python3
import glob
import os
import sys

def main():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions', 'social')
    if not os.path.exists(base_dir):
        print(f"Error: {base_dir} not found.")
        sys.exit(1)

    chapters = sorted(os.listdir(base_dir))
    chapters = [c for c in chapters if os.path.isdir(os.path.join(base_dir, c))]

    print(f"Found {len(chapters)} chapters in questions/social/:\n")
    print(f"{'#':<3} {'Chapter Slug':<55} {'Questions':<10}")
    print("-" * 70)

    total_questions = 0
    for idx, chapter in enumerate(chapters, 1):
        q_files = glob.glob(os.path.join(base_dir, chapter, "*.md"))
        q_count = len(q_files)
        total_questions += q_count
        print(f"{idx:<3} {chapter:<55} {q_count:<10}")

    print("-" * 70)
    print(f"Total Questions across all chapters: {total_questions}\n")

    # Sample preview from first chapter
    if chapters:
        first_chap = chapters[0]
        sample_files = sorted(glob.glob(os.path.join(base_dir, first_chap, "*.md")))
        if sample_files:
            print(f"Preview from '{first_chap}' ({len(sample_files)} questions):")
            print("=" * 70)
            with open(sample_files[0], 'r', encoding='utf-8') as f:
                print(f.read().strip())
            print("=" * 70)

if __name__ == "__main__":
    main()
