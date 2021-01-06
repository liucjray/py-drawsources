from lib.sources.SourceLhcdr import *

s = SourceLhcdr({
    'url': '/drawNotice.php',
    'resource': 'lhcdr',
    'area': 'macau',
    'type': 'marksix',
})
s.handle()
