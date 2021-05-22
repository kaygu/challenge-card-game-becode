class Symbol:
    def __init__(self, icon: str) -> None:
        if icon in ['♥', '♦']:
            color = 'red'
        else:
            color = 'black'
        self.icon: str = icon
        self.color: str = color

    def __str__(self) -> str:
        return f'{self.color} {self.icon}'


class Card(Symbol):
    def __init__(self, value: str, icon: str) -> None:
        Symbol.__init__(self, icon)
        self.value: str = value

    def __str__(self) -> str:
        return f'{self.value}{self.icon}'
