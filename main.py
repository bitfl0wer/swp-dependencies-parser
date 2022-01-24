from html.parser import HTMLParser

# IDENTIFIER, CONTENT, CHILDREN[]
parsed_input = []


def iterative(data):
    iter_output = []
    curr_iter = 0
    curr_file = ''
    for data_iter in data:
        print('iter: current iter ', data_iter)
        print('iter: data_iter[1] = ', data_iter[1])
        if data_iter[1] == 'file' and data_iter[0] == 'START':
            print('iter: encountered file')
            curr_file = data_iter[2]
        if data_iter[1] == 'dependency':
            print('iter: encountered dependency')
            print('iter: curr_file: ', curr_file)
            iter_output.append([curr_file, 'a dependency'])
    return iter_output


class HTMLToAsciiDoc(HTMLParser):
    def handle_starttag(self, tag, attrs):
        children = []
        for attr in attrs:
            children.append(attr)
        parsed_input.append(["START", tag, children])

    def handle_endtag(self, tag):
        parsed_input.append(["END", tag, []])


parser = HTMLToAsciiDoc()
with open("input.html", "r") as file:
    input = file.read()
parser.feed(input)

for loop_itr in parsed_input:
    print(loop_itr)

out = iterative(parsed_input)
print("iter: output: ", out)
