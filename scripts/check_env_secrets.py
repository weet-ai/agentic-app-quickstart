#!/usr/bin/env python3
"""
Security check script to prevent prx_live tokens from being committed to .env files.
"""

import sys
import os


def check_for_prx_live(file_path):
    """Check if file contains prx_live tokens."""

    violations = []

    try:
        with open(file_path, "r") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()

                # Skip comments and empty lines
                if not line or line.startswith("#"):
                    continue

                # Check if line contains prx_live
                if "prx_live" in line:
                    violations.append((line_num, line))

    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

    return violations


def main():
    """Main function to check environment files for prx_live tokens."""

    # Files to check (all .env* files)
    env_files = []
    for file in os.listdir("."):
        if file.startswith(".env"):
            env_files.append(file)

    all_violations = []

    for env_file in env_files:
        violations = check_for_prx_live(env_file)
        if violations:
            all_violations.extend([(env_file, v) for v in violations])

    if all_violations:
        print("🚨 SECURITY ALERT: prx_live tokens found in environment files!")
        print("=" * 60)

        for file_name, (line_num, line) in all_violations:
            print(f"File: {file_name}")
            print(f"Line {line_num}: {line}")
            print()

        print("❌ Please remove prx_live tokens from environment files.")
        print("💡 These tokens should not be committed to version control.")

        return 1

    print("✅ No prx_live tokens found in environment files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
