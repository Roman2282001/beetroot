if __name__ == '__main__':
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

total_price = {}
total = 0

for product, product_qty in stock.items():
    product_price = prices.get(product, 0)
    total_price[product] = product_qty * product_price
    total = total + product_qty * product_price
print(f'Total price {total_price}: \ntotal: {total}')
