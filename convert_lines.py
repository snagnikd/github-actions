output_str = ""

with open('changed_lines.txt', 'r') as file:
    output_str += file.read().strip()

output_dict = {}
output_str = output_str.strip('{}')
pairs = output_str.split('], ')
for pair in pairs:
    key_value = pair.split(': [')
    key = key_value[0].strip()
    value_str = key_value[1]
    value_str = value_str.strip(']')
    line_numbers = value_str.split(', ')
    value = [int(num) for num in line_numbers]
    output_dict[key] = value
print(output_dict)

text_strings = []

for file_path, line_numbers in output_dict.items():
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_number in line_numbers:
            if line_number <= len(lines):
                text = lines[line_number - 1].strip()
                text_string = f"{file_path}:{line_number}:{text}"
                text_strings.append(text_string)
result_text = "\n".join(text_strings)

print(result_text)