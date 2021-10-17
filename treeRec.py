class A:
    def __init__(self) -> None:
        self.name = "Vikas"

    def f1(self):
        def f2(self):
            return self.name
        return f2(self)


a = A()
x = a.f1()
print(x)
