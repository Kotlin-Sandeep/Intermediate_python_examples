class range_examp:

    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def next(self):
        if self.current >=self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val
for i in range_examp(5):
    print(i)
