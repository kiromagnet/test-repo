#!/usr/bin/env python3
"""test-repo: hello world"""

import sys

def main(argv):
    name = argv[1] if len(argv) > 1 else "world"
    print(f"OK — hello, {name}!")
    print(f"python: {sys.version.split()[0]}")
    print(f"platform: {sys.platform}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
