"""The stack class contains functions that define the structure data in a list """


class Stack:
    """
    function to create an empty stack
    """

    def __init__(self):
        self.items = []

    """
    function to check if there is an item in the stack
    """

    def isEmpty(self):
        return self.items == []

    """
    function to insert a new item into a stack
    """

    def append(self, item):
        self.items.insert(0, item)

    """
    function to delete item from a stack
    """

    def pop(self):
        return self.items.pop()


"""
 function to split a given html file into a string and a list
"""


def split_htmlFile(html_file):
    tag_file = open(html_file, "r", encoding="utf-8")
    tag_string = tag_file.read()
    tag_string1 = tag_string.replace("\n", " ")
    # replace newlines with a whitespace
    tag_string2 = " ".join(tag_string1.split())
    # by splitting the string it removes extra spaces
    tag_string3 = "> ".join(tag_string2.split(">"))
    # split by > and add >
    tag_string4 = " <".join(tag_string3.split("<"))
    tag_string5 = ""
    for item in tag_string4.split():
        # splits string4 and iterates over its items
        if item.startswith("<"):
            tag_string5 += item

        else:
            continue

    delimiter = ">"
    tag_split = [tag + delimiter for tag in tag_string5.split(delimiter) if tag]
    # change a string into a list by splitting with the delimiter
    check_tag_of(tag_split)


"""
function to check tags in a a stack if they already exist in a dictionary
"""


def check_tag_of(tag_returned):
    tag_list = Stack()
    valid = True
    for tag in tag_returned:
        # iterate over items in the stack that was extract from the html file
        valid = True
        if tag[0] == "<" and tag[1] != "/":
            tag_list.append(tag)
        elif tag[0] == "<" and tag[1] == "/":
            if tag_list.isEmpty():
                valid = False
                break
            else:
                last = tag_list.pop()
                verifier = match_tag(last, tag)
                if verifier:
                    valid = True
                else:
                    valid = False
                    break
        else:
            pass

    # checks if the stack was empty
    if tag_list.isEmpty() and valid:
        if len(tag_returned) != 0:
            item = tag_returned[0]
            if item[0] == "<" and len(tag_returned) != 0:
                print(">>> valid html file")
            else:
                print("oops >>> invalid html file ")
        else:
            print("oops >>> invalid html file ")

    else:
        if tag_list.isEmpty() and not valid:
            print("oops >>> invalid html file")
        elif not tag_list.isEmpty():
            if valid:
                 print("oops >>> invalid html file")
            else:
                print("oops >>> invalid html file")


"""
function to mach tags in a stack and tags in a dictionary
 """


def match_tag(key, value):
    tag_archive = {"<html>": "</html>", "<br>": "</br>", "<body>": "</body>",
                   "<head>": "</head>", "<title>": "</title>", "<a>": "</a>",
                   "<base>": "</base>", "<big>": "</big>", "<center>": "</center>",
                   "<code>": "</code>", "<input>": "</input>", "<q>": "</q>", "<p>": "</p>",
                   "<select>": "</select>", "<div>": "</div>", "<span>": "</span>",
                   "<table>": "</table>", "<thread>": "</thread>", "<tbody>": "</tbody>",
                   "<tr>": "</tr>", "<td>": "</td>", "<script>": "</script>", "<img>": "</img>",
                   "<ul>": "</ul>", "<li>": "</li>", "<strong>": "</strong>"}
    # a dictionary with html tags

    if key in tag_archive.keys() and value in tag_archive.values():
        if tag_archive[key] == value:
            return True
        return False
    return False


split_htmlFile("lala.html")
