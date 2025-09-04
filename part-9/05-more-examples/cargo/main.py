from funcs import item
from funcs import suitcase
from funcs import cargo_hold

book = item.Item("ABC Book", 2)
phone = item.Item("Nokia 3210", 1)
brick = item.Item("Brick", 4)

adas_suitcase = suitcase.Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = suitcase.Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = cargo_hold.CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
cargo_hold.print_items()