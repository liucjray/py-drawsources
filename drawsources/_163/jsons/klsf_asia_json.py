from lib.sources.Source163 import *


def get_instance():
    return Source163({
        'url': 'm/getlotdata.html?DataType=1&lotCode=80208',
        'resource': '163',
        'area': 'asia',
        'type': 'klsf',
    })
