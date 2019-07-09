from lib.sources.SourceEG import *


def get_instance():
    return SourceEG({
        'url': 'api/GetFcAutoToNum?fc_id=82&page=1&period=&stime=&etime=',
        'resource': 'eg',
        'area': 'bj',
        'type': 'kl8',
    })
