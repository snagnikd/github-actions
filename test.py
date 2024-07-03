from spellchecker import SpellChecker

def spell_check_line(line):
    spell = SpellChecker()

    # Split the line into words
    words = line.split()

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Correct misspelled words and print corrections
    corrected_line = []
    for word in words:
        if word in misspelled:
            corrected_line.append(spell.correction(word))
        else:
            corrected_line.append(word)

    # Join corrected words back into a line
    corrected_line = ' '.join(corrected_line)

    return corrected_line

# Example usage
line = "Thiss is a samplee sentance witht somee misspelled wordss."
corrected_line = spell_check_line(line)
print("Original:", line)
print("Corrected:", corrected_line)
