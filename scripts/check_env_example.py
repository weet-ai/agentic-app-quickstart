#!/usr/bin/env python3
"""
Pre-commit hook to check for 'prx_live' tokens in environment files.

This script prevents accidentally committing real API keys containing 'prx_live'
in any .env* files except .env (which is gitignored).
"""

import sys
from pathlib import Path
from typing import List, Tuple


def check_for_prx_live(filepath: Path) -> List[Tuple[str, str, int]]:
    """
    Check an environment file for 'prx_live' tokens.

    Args:
        filepath: Path to the environment file

    Returns:
        List of tuples (key, value, line_number) for entries containing 'prx_live'
    """
    suspicious_entries = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith("#"):
                    continue

                # Check if line contains 'prx_live'
                if "prx_live" in line:
                    # Try to parse KEY=VALUE format
                    if "=" in line:
                        key, value = line.split("=", 1)
                        key = key.strip()
                        value = value.strip().strip('"').strip("'")
                        suspicious_entries.append((key, value, line_num))
                    else:
                        # If not KEY=VALUE format, just flag the line
                        suspicious_entries.append(("", line, line_num))

    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []

    return suspicious_entries


def main() -> int:
    """Main function to check environment files for 'prx_live' tokens."""
    if len(sys.argv) < 2:
        print("Usage: python check_env_example.py <file1> [file2] ...")
        return 1

    exit_code = 0

    for filepath_str in sys.argv[1:]:
        filepath = Path(filepath_str)

        if not filepath.exists():
            print(f"File not found: {filepath}")
            exit_code = 1
            continue

        # Skip .env files (they won't be committed anyway)
        if filepath.name == ".env":
            print(f"⏭️  Skipping {filepath} (not committed to git)")
            continue

        suspicious_entries = check_for_prx_live(filepath)

        if suspicious_entries:
            print(f"🚨 SECURITY WARNING: Found 'prx_live' tokens in {filepath}")
            print("These look like real API keys that shouldn't be committed:")
            print()

            for key, value, line_num in suspicious_entries:
                if key:  # KEY=VALUE format
                    # Mask the value for security
                    masked_value = (
                        f"{value[:8]}...{value[-4:]}" if len(value) > 12 else "***"
                    )
                    print(f"  Line {line_num}: {key}={masked_value}")
                else:  # Just a line containing prx_live
                    print(f"  Line {line_num}: {value}")

            print()
            print("✅ To fix this:")
            print("  1. Move real API keys to .env (which is gitignored)")
            print("  2. Use placeholder values in .env.example like:")
            print('     OPENAI_API_KEY="your_openai_api_key_here"')
            print()

            exit_code = 1
        else:
            print(f"✅ {filepath} looks good - no 'prx_live' tokens found")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
