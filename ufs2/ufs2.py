import lxml.html

CLASSNAMES = {
    '.h-adr': {},
    '.h-card': {},
    '.h-entry': {},
    '.h-event': {},
    '.h-geo': {},
    '.h-item': {},
    '.h-product': {},
    '.h-recipe': {},
    '.h-resume': {},
    '.h-review': {},
    '.h-review-aggregate': {},
}

def parse(fp):
    html = lxml.html.parse(fp).getroot()
    print html.cssselect(','.join(CLASSNAMES.keys()))
    return {}

#    context = etree.iterparse(StringIO(xml))
#    >>> for action, elem in context:
#    ...     print("%s: %s" % (action, elem.tag))
