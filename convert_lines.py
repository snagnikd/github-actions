output_str = ""

# Read the content of 'changed_lines.txt' and store it in output_str
with open('changed_lines.txt', 'r') as file:
    output_str += file.read().strip()

output_dict = {}
# Remove the curly braces from the string representation of the dictionary
output_str = output_str.strip('{}')

# Split the string into key-value pairs
pairs = output_str.split('], ')
for pair in pairs:
    key_value = pair.split(': [')
    key = key_value[0].strip().strip('"')  # Remove any extra spaces and quotes
    value_str = key_value[1].strip(']')
    line_numbers = value_str.split(', ')
    value = [int(num) for num in line_numbers]
    output_dict[key] = value

print(output_dict)  # Debugging: Check the parsed dictionary

text_strings = []

# Read the specified lines from each file
for file_path, line_numbers in output_dict.items():
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_number in line_numbers:
            if line_number <= len(lines):
                text = lines[line_number - 1].strip()
                text_string = f"{file_path}:{line_number}:{text}"
                text_strings.append(text_string)

result_text = "\n".join(text_strings)

# Create the prompt for grammar and spelling checking
prompt = f'''Out of the following lines of code provided, look for any text present, check the text for correct grammar and spellings. Remove the lines that are correct.
Report the text as it is provided after removing the lines that have correct grammar and spellings. Leave the wrong ones there. Only return the text. Nothing else

Here is the text
{result_text}'''

print(prompt)