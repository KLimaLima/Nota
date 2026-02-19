import parser.parser as parser

def greet(name):

    return f"Hello {name[0]}! You are {name[1]} years old."

# TODO: check if file already exist
def create_md(filename):

    with open(f'./notes/{filename}.md', 'w') as f:
        f.write('')

# TODO: take md in notes and become html
def create_nota(filename):

    print(type(filename))

    parser.convert_md_html(filename)