from data.products import get_products
from analysis import statistics
from utils.formatter import format_output

def main():
    products = get_products()

    category_averages = statistics.compute_category_averages(products)
    expensive_item = statistics.get_most_expensive(products)

    print("Category Averages:")
    for cat, avg in category_averages.items():
        print(f"{cat}: {avg}")

    print("\nMost Expensive Product:")
    print(format_output(expensive_item))

if __name__ == "__main__":
    main()
