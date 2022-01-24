from html.parser import HTMLParser

# IDENTIFIER, CONTENT, CHILDREN[]
parsed_input = []


def iterative(data):
    iter_output = []
    curr_iter = 0
    for data_iter in data:
        curr_file = ''
        if data[curr_iter][1] == 'file':
            curr_file = file
        if data[curr_iter][1] == 'dependency':
            iter_output.append([curr_file, data[curr_iter][2][1]])
        curr_iter = curr_iter + 1
        if curr_iter > len(data):
            break
    return iter_output


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

# for loop_itr in parsed_input:
#    print(loop_itr)

out = iterative(parsed_input)
print(out)
