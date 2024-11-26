from Types import DataType

class AcademicDebts:
    def __init__(self, data: DataType) -> None:
        self.data = data

    def count_debts(self) -> int:
        return sum(
            1 for student, grades in self.data.items()
            if any(score < 61 for _, score in grades)
        )