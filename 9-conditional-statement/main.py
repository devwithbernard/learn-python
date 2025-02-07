"""
Conditional Statement
"""


def mean_sale(sales: list[float]) -> float:
    sale: float = round(sum(sales) / len(sales), 2)
    return sale


def main() -> None:
    employees: list = [
        {
            "name": "John Doe",
            "degree": "Civil Engineer",
            "sale": 15_000
        }, {
            "name": "Roman Labrun",
            "degree": "Manager",
            "sale": 20_000
        }, {
            "name": "Jane Joe",
            "degree": "Web Developper",
            "sale": 25_000
        },
    ]

    sales: list[int] = [employee.get('sale') for employee in employees]
    m_sale: float = mean_sale(sales)

    for employee in employees:
        if employee['sale'] <= m_sale:
            print(f"{employee['name']} don't make more money")
        else:
            print(f"{employee['name']} makes sufficient money")


if __name__ == '__main__':
    main()
