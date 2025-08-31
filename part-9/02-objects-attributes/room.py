class Person:
    def __init__(self, name: str, height: float) -> None:
        self.name = name
        self.height = height

    def __str__(self) -> str:
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons: list[Person] = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self) -> bool:
        return len(self.persons) == 0

    def shortest(self) -> Person | None:
        if self.is_empty():
            return None

        return min(self.persons, key=lambda person: person.height)

    def remove_shortest(self) -> Person | None:
        shortest_person = self.shortest()

        if shortest_person is not None:
            self.persons.remove(shortest_person)

        return shortest_person


    def print_contents(self) -> None:
        total_height = sum([person.height for person in self.persons])

        print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")

        for person in self.persons:
            print(person)



room = Room()
print("Is the room empty?", room.is_empty())
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 155))
print("Is the room empty?", room.is_empty())
room.print_contents()

print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())

room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Nina", 162))
room.add(Person("Ally", 166))

print()

print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())

print()

room.print_contents()

print("\nRemoving shortest...")
removed = room.remove_shortest()
print("Removed:", removed)

room.print_contents()