import mistletoe

with open('./notes/msitletoe-dev-guide.md', 'r') as fin:
    rendered = mistletoe.markdown(fin)

    print(rendered)

with open('out/out.html', 'w') as f:
    f.write(rendered)

# from mistletoe import Document, HtmlRenderer

# with open('README.md', 'r') as fin:
#     with HtmlRenderer() as renderer:     # or: `with HtmlRenderer(AnotherToken1, AnotherToken2) as renderer:`
#         doc = Document(fin)              # parse the lines into AST
#         rendered = renderer.render(doc)  # render the AST
#         rendered = renderer.render_heading(doc.children[0])
#         rendered = renderer.render_to_plain(doc)
#         # internal lists of tokens to be parsed are automatically reset when exiting this `with` block
#         print(doc.children)
#         temp = doc.children[0]
#         # print(rendered)