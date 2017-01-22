import jinja2
import json
import os
from markdown import markdown

SITE_ROOT_FOLDER = './docs/'
ARTICLE_ROOT_FOLDER = './articles/'
INDEX_TEMPLATE_PATH = 'templates/index_template.html'
ARTICLE_TEMPLATE_PATH = 'templates/article_template.html'
INDEX_FILE = 'index.html'


def ensure_dir_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def open_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as opened_file:
        return opened_file.read()


def get_config_from_json():
    with open("config.json", "r", encoding='utf8') as json_data_file:
        return json.load(json_data_file)


def convert_markdown_to_html(template, file_info, article_title, topic, index_file_path):
    html_text = markdown(file_info, extensions=['codehilite', 'fenced_code'])
    data_to_render = {'html': html_text, 'title': article_title, 'topic': topic,
                      'link': '../index.html'}
    return template.render(data_to_render)


def save_html_file(html_text, path_to_save):
    with open(path_to_save, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html_text)


def form_path_to_html_file(markdown_path):
    return markdown_path.replace('.md', '.html')


if __name__ == '__main__':
    config = get_config_from_json()
    articles = config['articles']
    ensure_dir_exists(SITE_ROOT_FOLDER)
    jin_env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))
    article_template = jin_env.get_template(ARTICLE_TEMPLATE_PATH)
    index_file_path = '{}{}'.format(SITE_ROOT_FOLDER, INDEX_FILE)
    link_article_to_index = '{}{}'.format('../', INDEX_FILE)
    for article in articles:
        source = article['source']
        file_info = open_file('{}{}'.format(ARTICLE_ROOT_FOLDER, source))
        html_article = convert_markdown_to_html(article_template, file_info, article['title'],
                                                article['topic'], link_article_to_index)
        path_to_save_html = '{}{}'.format(SITE_ROOT_FOLDER, form_path_to_html_file(source))
        ensure_dir_exists(os.path.split(path_to_save_html)[0])
        save_html_file(html_article, path_to_save_html)
    index_template = jin_env.get_template(INDEX_TEMPLATE_PATH)
    index_template.globals['form_article_path'] = form_path_to_html_file
    result_html = index_template.render(topics=config['topics'], articles=articles)
    save_html_file(result_html, index_file_path)
