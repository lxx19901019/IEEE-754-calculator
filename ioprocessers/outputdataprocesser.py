from consolehelper import consoleservice


class OutputProcesser:
    def __init__(self, res):
        self.__res = res

    @property
    def res(self):
        return self.__res

    @res.setter
    def res(self, res):
        self.__res = res

    def process(self):
        consoleservice.ConsoleService.print_message(str(float(self.res)))
