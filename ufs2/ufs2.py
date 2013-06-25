import lxml.html

CLASSNAMES = {
    'h-adr': [
        'p-post-office-box',
        'p-extended-address',
        'p-street-address',
        'p-locality',
        'p-region',
        'p-postal-code',
        'p-country-name',
        'p-label',
        'p-geo',
        'p-latitude',
        'p-longitude',
        'p-altitude',
    ],
    'h-card': {},
    'h-entry': {},
    'h-event': {},
    'h-geo': {},
    'h-item': {},
    'h-product': {},
    'h-recipe': {},
    'h-resume': {},
    'h-review': {},
    'h-review-aggregate': {},
}

def parse_item(item):
    item_type = unicode(item.attrib['class'])
    properties = {}
    for property_class in CLASSNAMES[item_type]:
        prefix, _, prop_name = property_class.partition('-')
        for prop in item.cssselect('.' + property_class):
            if prefix == 'p':
                properties[prop_name] = [unicode(prop.text)]
            else:
                raise NotImplementedError('This prefix has not been implemented.')
    return {
        'type': [item_type],
        'properties': properties,
    }

def parse(fp):
    html = lxml.html.parse(fp).getroot()
    items = html.cssselect('.' + ',.'.join(CLASSNAMES.keys()))
    return {'items': [parse_item(item) for item in items]}

#    context = etree.iterparse(StringIO(xml))
#    >>> for action, elem in context:
#    ...     print("%s: %s" % (action, elem.tag))
