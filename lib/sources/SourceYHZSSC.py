from bs4 import BeautifulSoup


class SourceYHZSSC:
    def __init__(self):
        self.data = []
        self.issues = []
        self.codes = []

    def parse(self, r):
        soup = BeautifulSoup(r.text, 'lxml')
        selector = "table#chartsTable tr"
        trs = soup.select(selector)
        for tr in trs[2:]:
            # issues
            for issue in tr.find_all("td", id="title"):
                self.issues.append(issue.text)

            # codes
            codes = []
            for code_td in tr.find_all("td")[1:6]:
                for code in code_td.find_all("div", class_="ball02"):
                    codes.append(code.text)
            self.codes.append(','.join(codes))

        self.data = dict(zip(self.issues, self.codes))
        return self.data
