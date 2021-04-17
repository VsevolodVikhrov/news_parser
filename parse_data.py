import get_request
import re
import pprint


def parse_united_data_blocks(page=None, articles_count=None, pages=None):
    all_data_blocks = []
    if articles_count:
        pages = get_page_count(articles_count)
        for i in range(1, pages + 1):
            html_data = get_request.get_page(i)
            all_data_blocks.extend((re.findall(r'"title">\<(a href=.+?)(\n.+(comment|discuss|hide))', html_data)))
        return unite_parsed_data(all_data_blocks, articles_count)
    if page:
        html_data = get_request.get_page(page)
        all_data_blocks.extend((re.findall(r'"title">\<(a href=.+?)(\n.+(comment|discuss|hide))', html_data)))
        return unite_parsed_data(all_data_blocks)


def get_page_count(articles):
    if articles <= 30:
        pages = 1
    else:
        pages = (articles // 30) + 1
    return pages


def parse_titles(all_data_blocks):
    pre_titles = re.findall(r'storylink"\>(.+?)\<|nofollow"\>(.+?)\<', all_data_blocks)
    title = 0
    for i in pre_titles:
        for j in i:
            if j:
                title = j
    title = title.replace("\\", "")
    return "".join(title)


def parse_urls(all_data_blocks):
    url = re.findall(r'href=\"(http.+?)\"', all_data_blocks)
    if not url:
        url = "https://news.ycombinator.com/" + "".join(re.findall(r"'a href=\"(item.+?)\"", all_data_blocks))
    return "".join(url)


def parse_authors(all_data_blocks):
    author = re.findall(r'hnuser"\>(.+?)\<', all_data_blocks)
    if not author:
        author = "Hidden"
    return "".join(author)


def parse_amount_of_comments(all_data_blocks):
    amount_of_comments = re.findall(r'\>(\d+?)\&', all_data_blocks)
    if not amount_of_comments:
        amount_of_comments = "No comments"
    return "".join(amount_of_comments)


def parse_points_amount(all_data_blocks):
    points = re.findall(r'score_.+?"\>(\d+?)\ points', all_data_blocks)
    if not points:
        return 0
    return int("".join(points))


def parse_age(all_data_blocks):
    age = re.findall(r'age"><a href="item\?id=\d+?"\>(\d*.+?)\<', all_data_blocks)
    return "".join(age)


def unite_parsed_data(all_data_blocks, articles_count=None):
    articles = []
    counter = 0
    for i in all_data_blocks:
        i = str(i)
        articles.append({
        "Title: " : parse_titles(i),
        "URL: " : parse_urls(i),
        "Author: " : parse_authors(i),
        "Points: " : parse_points_amount(i),
        "Comments: ": parse_amount_of_comments(i),
        "Age: ": parse_age(i)
        })
        counter += 1
        if articles_count and counter == articles_count:
            break
    return articles





