from jinja2 import Environment, FileSystemLoader

def render_template(content_html):

    environment = Environment(loader=FileSystemLoader("template/"))
    template = environment.get_template(f'{content_html}.html')

    content = template.render()

    with open("./src/index.html", mode="w", encoding="utf-8") as f:

        f.write(content)

def create_template(content_html):

    template_tag_start = '''{% extends "base.html" %}
    
    {% block content %}'''

    content = ''

    template_tag_end = '{% endblock content %}'

    with open(f'out/{content_html}.html', mode="r") as f:

        content = f.readlines()

    with open(f'template/{content_html}.html', mode="w") as f:

        f.writelines(template_tag_start)

        f.writelines(content)

        f.writelines(template_tag_end)