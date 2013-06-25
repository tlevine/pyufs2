import os, json
import ufs2

def test_everything():
    CASEDIR = os.path.join("support", "cases")
    websites = os.listdir(CASEDIR)
    for website in websites:
        website_dir = os.path.join(CASEDIR, website)
        for sub_website in os.listdir(website_dir):
            sub_website_dir = os.path.join(website_dir, sub_website)
            basenames = set([filename.split('.')[0] for filename in os.listdir(sub_website_dir)])
            for basename in basenames:
                js_file = open(os.path.join(sub_website_dir, basename + '.js'))
                html_file = open(os.path.join(sub_website_dir, basename + '.html'))

                js_file.readline() # Burn the comment
                expected = json.load(js_file)

                observed = ufs2.parse(html_file)
                n.assert_dict_equal(observed, expected)
