
class SumNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def find_sum(self):
        return self.a + self.b

obj = SumNumbers(10, 20)
print("Sum:", obj.find_sum())

