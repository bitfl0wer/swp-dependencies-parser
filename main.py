from html.parser import HTMLParser

# IDENTIFIER, CONTENT, CHILDREN[]
parsed_input = []


def iterative(data):
    iter_output = []
    curr_file = ''
    for data_iter in data:
        # print('iter: current iter ', data_iter)
        # print('iter: data_iter[1] = ', data_iter[1])
        if data_iter[1] == 'file' and data_iter[0] == 'START':
            # print('iter: encountered file')
            curr_file = data_iter[2]
        if data_iter[1] == 'dependency':
            # print('iter: encountered dependency')
            # print('iter: curr_file: ', curr_file)
            iter_output.append([curr_file[1], data_iter[2][1]])
    return iter_output


class HTMLToAsciiDoc(HTMLParser):
    def handle_starttag(self, tag, attrs):
        children = []
        for attr in attrs:
            children = attr
        parsed_input.append(["START", tag, children])


parser = HTMLToAsciiDoc()
with open("input.html", "r") as file:
    input = file.read()
parser.feed(input)

list_dependencies = []
list_dependency_usages = []
iter_out = iterative(parsed_input)

count = 0
for item in iter_out:
    if not any(item[1] in sl for sl in list_dependency_usages):
        list_dependencies.append(item[1])
        list_dependency_usages.append([item[1], []])
    count = count + 1

for item in iter_out:
    pos = list_dependencies.index(item[1])
    if not item[1] in list_dependency_usages:
        list_dependency_usages[pos][1].append(item[0])


print(list_dependency_usages)
