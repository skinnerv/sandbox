class TestInheritOrg:
    def __init__(self, source_name: str, source_age: int) -> None:
        self.source_name = source_name
        self.source_age = source_age
        print('Org is running')
        pass

    def call_name(self) -> None:
        print(f'Name: {self.source_name}, age: {self.source_age}')
    
    @staticmethod
    def multiple(age: int) -> None:
        print(age * 20)

if __name__ == '__main__':
    tio = TestInheritOrg('Scott', 30)
    tio.call_name()
    tio.multiple(20)