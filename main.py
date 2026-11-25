#!/usr/bin/env python3
"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Writes a one-line elevator pitch from a city pigeon to investors
for its startup: vertical infrastructure auditing via beak-mounted LiDAR.
"""
import os
import sys

LINE = "We're not pigeons - we're 'vertical infrastructure auditors.' Series A funds beak-mounted LiDAR, city pays us to scan facades, we nest rent-free on every ledge."

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', 'out')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')
    
    content = LINE + '\n'
    
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError(f"Content validation failed: length={len(content)}, stripped={bool(content.strip())}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Output: {output_path}")
    print(f"Characters: {len(content)}")

if __name__ == '__main__':
    main()
