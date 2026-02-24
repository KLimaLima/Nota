import subprocess

import parser.parser as parser
import template.template as template

def greet(name):

    return f"Hello {name[0]}! You are {name[1]} years old."

# TODO: check if file already exist
def create_md(filename):

    with open(f'./notes/{filename}.md', 'w') as f:
        f.write('')

# TODO: take md in notes and become html
def create_nota(filename):

    parser.convert_md_html(filename)

    template.create_template(filename)

    template.render_template(filename)

    process_npm = subprocess.check_output(["npm run build"], text=True, shell=True)
    print(process_npm)

    process_mv = subprocess.check_output(["mv -v dist/index.html result/"], text=True, shell=True)
    print(process_mv)