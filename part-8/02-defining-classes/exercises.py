"""
Define classes: Exercises
"""

# TODO: Book

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int) -> None:
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    def describe(self) -> None:
        description = f"{self.author}: {self.name}({self.year})"
        return description

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(python.describe())
print(everest.describe())

# TODO: Design user
import urllib.request
import urllib.error
import json
import logging
import pprint


def get_users(url: str) -> list[dict]:
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,  # INFO or DEBUG depending on verbosity
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    try:
        logging.info(f"Fetching data from {url}")

        with urllib.request.urlopen(url, timeout=10) as response:
            status_code = response.getcode()

            if status_code == 200:
                logging.info("Data fetched successfully")
                data = json.loads(response.read())
                logging.debug(f"Response content: {data}")
                return data
            else:
                logging.warning(f"Request failed with status code: {status_code}")
    except urllib.error.HTTPError as e:
        logging.error(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        logging.error(f"URL Error: {e.reason}")
    except TimeoutError as e:
        logging.error("The request timed out")
    except Exception as e:
        logging.exception(f"Unexpected error: {e}")


# User Model
class GeoCode:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        return f"{self.latitude}, {self.longitude}"

    def __repr__(self) -> str:
        return f"GeoCode(latitude={self.latitude}, longitude={self.longitude})"

    def format(self) -> dict:
        return {
            "lat": self.latitude,
            "lng": self.longitude
        }

class Address:
    def __init__(self,
                 user_id: int,
                 street: str,
                 suite: str,
                 city: str,
                 zipcode: str,
                 geo: GeoCode):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode,
        self.geo = geo
        self.user_id = user_id

    def __str__(self) -> str:
        return f"{self.street}, {self.suite}, {self.city}"

    def __repr__(self) -> str:
        return (f"Address(street={self.street}, suite={self.suite}, "
                f"city={self.city}, zipcode={self.zipcode}, geo={self.geo})")

    def format(self) -> dict:
        return {
            f"{self.suite}": {
                "street": self.street,
                "city": self.city,
                "zipcode": self.zipcode,
                "geo": self.geo.format(),
                "user_id": self.user_id
            }
        }

class Company:
    def __init__(self, name: str, catchPhrase: str, bs: str, employee_id: int | None):
        self.name = name
        self.catchPhrase = catchPhrase
        self.bs = bs
        if employee_id:
            self.employee_id = employee_id

    def format(self) -> dict:
        return {
            f"{self.name}": {
                "catchPhrase": self.catchPhrase,
                "bs": self.bs,
                "employee_id": self.employee_id
            }
        }

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Company(name={self.name}, catchPhrase={self.catchPhrase}, bs={self.bs})"


class User:
    def __init__(self,
                 user_id: int,
                 name: str,
                 username: str,
                 email: str,
                 phone: str,
                 website: str):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return (f"User(name={self.name}, username={self.username}, email={self.email}, "
                f"phone={self.phone}, website={self.website})")

    def format(self) -> dict:
        return {
            f"{self.user_id}": {
                "name": self.name,
                "username": self.username,
                "email": self.email,
                "phone": self.phone,
                "website": self.website
            }
        }

def format_user(user: dict) -> tuple[User, Address, Company]:
    user_address = user['address']
    user_company = user['company']

    address: Address = Address(
        user['id'], user_address['street'], user_address['suite'], user_address['city'],
        user_address['zipcode'], GeoCode(float(user_address['geo']['lat']), float(user_address['geo']['lng'])))

    company: Company = Company(user_company['name'],
                               user_company['catchPhrase'],
                               user_company['bs'], user['id'])

    user = User(user['id'], user['name'], user['username'],
                user['email'], user['phone'], user['website'])

    return user, address, company


def main() -> None:
    users = get_users("https://jsonplaceholder.typicode.com/users")

    format_users = []
    companies = []
    addresses = []

    for user in users:
        f_user, format_address, format_company = format_user(user)

        format_users.append(f_user.format())
        companies.append(format_company.format())
        addresses.append(format_address.format())

    with open("files/companies.json", mode="w") as file:
        json_companies = json.dumps(companies, indent=4)
        file.write(json_companies)
        logging.info("Companies saved successfully")


    with open("files/users.json", mode="w") as file:
        json_users = json.dumps(format_users, indent=4)
        file.write(json_users)
        logging.info("Users saved successfully")

    with open("files/addresses.json", mode="w") as file:
        json_addresses = json.dumps(addresses, indent=4)
        file.write(json_addresses)
        logging.info("Addresses saved successfully")

if __name__ == "__main__":
    main()