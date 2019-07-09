from lib.sources.SourceBOMAOCAI import *


def get_instance():
    return SourceBOMAOCAI({
        'url': 'issueannoucement',
        'resource': 'bomaocai',
        'area': 'cq',
        'type': 'ssc',
    })
