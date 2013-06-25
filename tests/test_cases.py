import os, json

import nose.tools as n

import ufs2.ufs2 as ufs2

def test_stuff():
    CASEDIR = os.path.join("tests", "support", "cases")
    websites = os.listdir(CASEDIR)
    for website in websites:
        website_dir = os.path.join(CASEDIR, website)
        for sub_website in os.listdir(website_dir):
            sub_website_dir = os.path.join(website_dir, sub_website)
            basenames = set([filename.split('.')[0] for filename in os.listdir(sub_website_dir)])
            for basename in basenames:
                yield check_case, sub_website_dir, basename

def check_case(sub_website_dir, basename):
    js_file = open(os.path.join(sub_website_dir, basename + '.js'))
    html_file = open(os.path.join(sub_website_dir, basename + '.html'))

    js_file.readline() # Burn the comment
    expected = json.load(js_file)

    observed = ufs2.parse(html_file)
    n.assert_dict_equal(observed, expected)
