#!/usr/bin/env python3
"""Write a single predefined line to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
# Round 2 entry: output is 1-200 chars, exactly one line, deterministic.

LINE = "BenchShare sells 4-minute slots to phone scrollers — we poop on the armrest at minute three to enforce turnover, city fines fund our seed round."

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    content = LINE + "\n"
    
    # Validate
    if not (1 <= len(content) <= 200 and content.strip() and content.count(chr(10)) == 1 and content.endswith(chr(10))):
        raise ValueError("Validation failed")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Output path: {output_path}")
    print(f"Character count: {len(content)}")

if __name__ == "__main__":
    main()
