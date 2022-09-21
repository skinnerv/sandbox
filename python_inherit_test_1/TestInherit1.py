from TestInheritOrg import TestInheritOrg as TI

class TestInherit1(TI):
    def __init__(self, source_name: str, source_age: int):
        super().__init__(source_name, source_age)
        print('Child class is working')
        self.multiple(1)
        self.run_test()

    def run_test(self) -> None:
        self.multiple(2)

if __name__ == '__main__':
    TestInherit1('Jan', 40)
    