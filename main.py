from html.parser import HTMLParser

# IDENTIFIER, CONTENT, CHILDREN[]
parsed_input = []


def iterative(data):
    for data_iter in data:
        if data[data_iter][1] == 'file' or data[data_iter][1] == 'dependency':
            return


class HTMLToAsciiDoc(HTMLParser):
    def handle_starttag(self, tag, attrs):
        children = []
        for attr in attrs:
            children.append(["ATTR", attr, []])
        parsed_input.append(["START", tag, children])

    def handle_endtag(self, tag):
        parsed_input.append(["END", tag, []])


parser = HTMLToAsciiDoc()
with open("input.html", "r") as file:
    input = file.read()
parser.feed(input)
for loop_itr in parsed_input:
    print(loop_itr)
