
def print_welcome_message():
    print("Welcome to Madlib game! Please follow the instructions to create your story.")

def read_template(template_file):
    with open(template_file, "r") as file:
        template = file.read()
    return template

def parse_template(template):
    parts = []
    parsed_template = ""
    index = 0
    while index < len(template):
        if template[index] == "{":
            end_index = template.index("}", index)
            parts.append(template[index+1:end_index])
            parsed_template += "{}"
            index = end_index+1
        else:
            parsed_template += template[index]
            index += 1
    return (parsed_template, parts)

def get_input(part):
    return input(f"Enter {part}: ")

def merge(parsed_template, user_inputs):
    return parsed_template.format(*user_inputs)

def write_to_file(content):
    with open("completed_madlib.txt", "w") as file:
        file.write(content)

def main():
    print_welcome_message()
    template_file = "assets/madlib_example.txt"
    template = read_template(template_file)
    parsed_template, parts = parse_template(template)
    user_inputs = []
    for part in parts:
        user_input = get_input(part)
        user_inputs.append(user_input)
    completed_madlib = merge(parsed_template, user_inputs)
    print(completed_madlib)
    write_to_file(completed_madlib)

if __name__ == "__main__":
    main()
