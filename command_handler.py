import parse_data
import file_processing

def inputting_commands():
    while True:
        user_input = input("Input your command: ")
        command = user_input.split()
        handler(command)


def handler(command):
    if command[0] == "show":
        if command[1] == "page":
            show_page(command)
        elif len(command) == 2:
            show_articles(command)
        elif "toprating" in command[1]:
            show_toprated(command)
        elif "points" in command[1]:
            show_higher_than_x_points(command)
    if "contains" in command[0] or "author" in command[0]:
        x_word_contains_in_key(command)
    if command[0] == "save":
        save_articles(command)
    if command[0] == "load":
        file_processing.load_articles(int(command[1]))


def show_page(command):
    articles = parse_data.parse_united_data_blocks(page=int(command[2]))
    printer(articles)


def show_articles(command):
    articles = parse_data.parse_united_data_blocks(articles_count=int(command[1]))
    printer(articles)


def show_toprated(command):
    if len(command) == 3:
        pre_articles = parse_data.parse_united_data_blocks(page=1)
        printable_count = int(command[2])
    else:
        pre_articles = parse_data.parse_united_data_blocks(articles_count=int(command[2]))
        printable_count = int(command[3])
    pre_articles = sorted(pre_articles, key=lambda i: i["Points: "], reverse=True)
    counter = 0
    articles = []
    for j in pre_articles:
        articles.append(j)
        counter += 1
        if counter == printable_count:
            break
    printer(articles)


def show_higher_than_x_points(command):
    pre_articles = parse_data.parse_united_data_blocks(articles_count=int(command[2]))
    articles = []
    rated_higher_than = int(command[1][7:])
    printable_count = int(command[3])
    counter = 0
    for i in pre_articles:
        if i["Points: "] > rated_higher_than:
            articles.append(i)
            counter += 1
        if counter == printable_count:
            break
    printer(articles)


def x_word_contains_in_key(command):
    keys = {"urlcontains": "URL: ", "titlecontains": "Title: ", "author": "Author: "}
    key = keys[command[0]]
    if len(command) == 2:
        pre_articles = parse_data.parse_united_data_blocks(page=1)
        keyword = command[1]
    else:
        pre_articles = parse_data.parse_united_data_blocks(articles_count=int(command[1]))
        keyword = command[2]
    articles = []
    for i in pre_articles:
        if keyword in i[key].lower():
            articles.append(i)
    printer(articles)


def save_articles(command):
    articles = parse_data.parse_united_data_blocks(articles_count=int(command[1]))
    file_processing.save_articles(articles)


def printer(articles):
    if articles:
        for i in articles:
            for j, k in i.items():
                print(f"{j}: {k}")
            print("\n")
    else:
        print("Not found")


inputting_commands()
