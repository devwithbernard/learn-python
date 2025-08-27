from present import Present


class Box:
    boxes: list[Present] = []

    def add_present(self, present: Present) -> None:
        self.boxes.append(present)

    def total_weight(self) -> float:
        weights: list[float] = []

        for present in self.boxes:
            weights.append(present.weight)

        return sum(weights)
