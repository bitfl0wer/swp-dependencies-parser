from html.parser import HTMLParser


class HTMLToAsciiDoc(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag encountered: " + tag)

    def handle_endtag(self, tag):
        print("End tag encountered: " + tag)

    def handle_data(self, data):
        print("Data encountered: " + data)


parser = HTMLToAsciiDoc()
