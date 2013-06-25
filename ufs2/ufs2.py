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

def parse_item(item):
    return {
        'type': item.attrib['class'],
        'properties': {},
    }

def parse(fp):
    html = lxml.html.parse(fp).getroot()
    items = html.cssselect(','.join(CLASSNAMES.keys()))
    return {'items': [parse_item(item) for item in items]}

#    context = etree.iterparse(StringIO(xml))
#    >>> for action, elem in context:
#    ...     print("%s: %s" % (action, elem.tag))
