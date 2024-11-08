"""
Casting in python
"""


def format_article() -> None:
	article: str = "Louis Vuitton Trowser"
	price: float = 32.5

	formatted_article: dict = {
		"article": article,
		"price": str(price)
	}

	print(formatted_article)


def main() -> None:
	format_article()


if __name__ == '__main__':
	main()
