import os
import sys
import subprocess
from spellchecker import SpellChecker

def spell_check(text):
    spell = SpellChecker()

    # Split the text into words
    words = text.split()

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Return True if no misspelled words found, False otherwise
    return len(misspelled) == 0

def main():
    try:
        commit_sha = sys.argv[1]

        # Get changed files using git diff
        changed_files_cmd = f"git diff --name-only HEAD $(git merge-base HEAD {commit_sha})"
        changed_files = subprocess.check_output(changed_files_cmd, shell=True, text=True).splitlines()

        spell_check_errors = []

        for file in changed_files:
            # Check only .md and .txt files (adjust as needed)
            if file.endswith('.md') or file.endswith('.txt'):
                diff_cmd = f"git diff -U0 HEAD $(git merge-base HEAD {commit_sha}) -- \"{file}\""
                diff_output = subprocess.check_output(diff_cmd, shell=True, text=True)
                diff_lines = diff_output.splitlines()

                line_number = 0
                for line in diff_lines:
                    line_number += 1

                    # Check added lines
                    if line.startswith('+'):
                        text_to_check = line[1:].strip()  # Remove the leading '+' and trim whitespace
                        if text_to_check and not spell_check(text_to_check):
                            spell_check_errors.append({'file': file, 'line_number': line_number, 'line': text_to_check})

        # Report spell check errors
        if spell_check_errors:
            print('Spell check errors found:')
            for error in spell_check_errors:
                print(f'{error["file"]}:{error["line_number"]} - {error["line"]}')
            sys.exit(1)  # Exit with non-zero code to indicate failure
        else:
            print('No spell check errors found.')

    except Exception as e:
        print(f'Error during spell check: {e}')
        sys.exit(1)

if __name__ == "__main__":
    main()
