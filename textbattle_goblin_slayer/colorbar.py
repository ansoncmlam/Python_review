import os
os.system("")


class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red" : "\033[91m",
                    "purple": "\033[95m",
                    "cyan": "\033[96m",
                    "green": "\033[92m",
                    "yellow": "\033[93m",
                    "blue": "\033[94m",
                    "white": "\033[97m",
                    "black": "\033[90m",
                    "default": "\033[0m"}
    


    def __init__(self, entity, 
                 length: int =20, 
                 is_colored: bool = True, 
                 color: str = "")-> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"] ## give keys to change color of health bar

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self) -> None:
        remaining_bars = round(self.current_value/self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s Health: {self.entity.health}/{self.entity.health_max}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}"
              )
