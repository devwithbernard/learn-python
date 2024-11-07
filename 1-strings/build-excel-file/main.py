from data import fetch
from writeExcelFile import write_file
def main() -> None:
    """
    Entry Point Of Program
    """
    comments: list[dict] = fetch()
    write_file(comments, 'comments.xlsx')


if __name__ == '__main__':
    main()