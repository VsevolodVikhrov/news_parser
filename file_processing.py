import json


def save_articles(articles):
    with open("backuped_articles.json", "w") as write_file:
        json.dump(articles, write_file)


def load_articles(count_of_articles):
    with open("backuped_articles.json", "r") as read_file:
        articles = json.load(read_file)
    counter = 0
    if articles:
        for i in articles:
            for j, k in i.items():
                print(f"{j}: {k}")
            print("\n")
            counter += 1
            if counter == count_of_articles:
                break

