
class DomainError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class LogicError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)