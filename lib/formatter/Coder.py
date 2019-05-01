class Coder:
    def __init__(self, code=None, type=None):
        self.type = type
        self.code = code
        self.formatter_code = []

    def pk10(self):
        if type(self.code) is list:
            for code in self.code:
                self.formatter_code.append(str(code).zfill(2))
        else:
            self.formatter_code = self.code

    def klsf(self):
        if type(self.code) is list:
            for code in self.code:
                self.formatter_code.append(str(code).zfill(2))
        else:
            self.formatter_code = self.code

    def ssc(self):
        self.formatter_code = self.code

    def n115(self):
        self.formatter_code = self.code

    def kl8(self):
        self.formatter_code = self.code

    def k3(self):
        self.formatter_code = self.code

    def marksix(self):
        self.formatter_code = self.code

    def get_code(self):
        # 使用變數名稱呼叫方法
        func = getattr(self, self.type)
        func()
        return self.formatter_code
