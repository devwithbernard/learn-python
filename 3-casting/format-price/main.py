import requests as r
import statistics
from collections import defaultdict


def get_products() -> list:
	products_url: str = 'https://fakestoreapi.com/products'
	try:
		response: r.Response = r.get(products_url)
		if response.status_code == 200:
			products: list = response.json()
			return products
	except r.exceptions.HTTPError as error:
		print(f"Fetch products failed!\n{error.message}")
		raise r.HTTPError()


def mean_price_of_product(products: list[dict]) -> float:
	prices: list = [product['price'] for product in products]
	return statistics.fmean(prices)


def group_by_category(products):
	grouped_products = defaultdict(list)

	# Iterate through the list of products
	for product in products:
		# Add each product to its respective category
		category = product["category"]
		grouped_products[category].append(product)

	return dict(grouped_products)


def entry() -> None:
	products: list = get_products()

	mean_price_of_a_product: str = str(mean_price_of_product(products))
	print(f"Mean price of a product ${mean_price_of_a_product}")

	products_by_category = group_by_category(products)
	for index, category in enumerate(products_by_category):
		print(f"{category}: ")
		for product in products_by_category[category]:
			print(f"  ${product['price']}, {product['title']}")

		if index == len(products_by_category) - 1:
			break
		print("\t" + "-" * 40)


def main() -> None:
	entry()


if __name__ == '__main__':
	main()
