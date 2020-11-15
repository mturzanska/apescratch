#!/usr/local/bin/python3

import os
import string
import random

import templates

# TODO: clean up aliased bash commands
#       move mogrify part from bash to here
#       move copying adn deploying part from bash to here
#       make it into a cli, with test and deploy options


# Inputs
PICS_DIR = os.getenv('APESCRATCH_PICS_DIR')
PIC_HTMLS_DIR = os.getenv('APESCRATCH_PIC_HTMLS_DIR')
THUMBNAILS_DIR = os.getenv('APESCRATCH_THUMBNAILS_DIR')

with open('home_template.html') as f:
    html = f.read()

with open('stylesheet_template.css') as f:
    css = f.read()


# Outputs
CSS_OUTPUT = 'stylesheet.css'
HTML_OUTPUT = 'index.html'


pics = os.listdir(PICS_DIR)
thumbnails = os.listdir(THUMBNAILS_DIR)


css_snippets = []
html_snippets = []

# clean up old files before generating new ones
for filename in os.listdir(PIC_HTMLS_DIR):
    relative_path = os.path.join(PIC_HTMLS_DIR, filename)
    os.remove(relative_path)


thumbnail_paths = [os.path.join(THUMBNAILS_DIR, t) for t in thumbnails]
pic_paths = [os.path.join('..', PICS_DIR, t) for t in thumbnails]
pic_names = [''.join(random.choices(string.ascii_letters, k=16)) for t in thumbnails]
pic_html_filenames = ['{}.html'.format(p) for p in pic_names]


for index, thumbnail in enumerate(thumbnails):
    if '.jpg' not in thumbnail.lower():
        continue

    pic_name = pic_names[index]
    pic_html_filename = pic_html_filenames[index]
    pic_path = pic_paths[index]
    thumbnail_path = thumbnail_paths[index]

    try:
        next_pic_html_filename = pic_html_filenames[index + 1]
    except IndexError:
        next_pic_html_filename = pic_html_filenames[0]

    prev_pic_html_filename = pic_html_filenames[index - 1]

    pic_html_file = open(os.path.join(PIC_HTMLS_DIR, pic_html_filename), 'w')
    pic_html = templates.pic_html_template.format(
        pic_path=pic_path,
        next_pic_html_filename=next_pic_html_filename,
        prev_pic_html_filename=prev_pic_html_filename,
    )
    pic_html_file.write(pic_html)

    thumbnail_css = templates.thumbnail_css_template.format(
            thumbnail_name=pic_name, thumbnail_path=thumbnail_path
    )
    css_snippets.append(thumbnail_css)
    pic_link = templates.pic_link_template.format(
        thumbnail_name=pic_name,
        pic_html_filename=pic_html_filename,
        PIC_HTMLS_DIR=PIC_HTMLS_DIR
    )

    html_snippets.append(pic_link)

html_snippets = "\n".join(html_snippets)
html = html.format(pics=html_snippets)

css_snippets = "\n".join(css_snippets)
css = '\n'.join([css, css_snippets])


with open(HTML_OUTPUT, "w") as f:
    f.write(html)

with open(CSS_OUTPUT, "w") as f:
    f.write(css)
