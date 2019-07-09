from bs4 import BeautifulSoup


class SourceYHZPK10:
    def __init__(self):
        self.data = []
        self.issues = []
        self.codes = []

    def parse(self, r):
        soup = BeautifulSoup(r.text, 'lxml')
        selector = "table#codeTable tr"
        trs = soup.select(selector)
        for tr in trs:
            if trs.index(tr) == 0 or trs.index(tr) == 1:
                continue

            # issues
            for issue in tr.find_all("td", class_="title"):
                self.issues.append(issue.text)

            # codes
            codes = []
            for code in tr.find_all("td", class_="code"):
                codes.append(code.text)
            self.codes.append(','.join(codes))

        self.data = dict(zip(self.issues, self.codes))
        return self.data
