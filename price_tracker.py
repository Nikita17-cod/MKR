from datetime import datetime, timedelta

def parse_data(filename):
    """
    Зчитує дані з файлу та повертає список словників.
    """
    data = []
    with open(filename, 'r') as f:
        for line in f:
            name, date_str, price_str = line.strip().split(',')
            date = datetime.strptime(date_str, '%Y-%m-%d')
            price = float(price_str)
            data.append({'name': name, 'date': date, 'price': price})
    return data

def get_price_change(data, product_name):
    """
    Повертає зміну ціни на товар за останній місяць.
    """
    today = datetime.now()
    one_month_ago = today - timedelta(days=30)

    product_data = [item for item in data if item['name'] == product_name]
    product_data.sort(key=lambda x: x['date'])

    last_month_prices = [item['price'] for item in product_data if item['date'] >= one_month_ago]

    if not last_month_prices:
        return None

    first_price = last_month_prices[0]
    last_price = last_month_prices[-1]
    return last_price - first_price

if __name__ == '__main__':
    filename = 'product_prices.txt'
    product_name = 'Товар A'
    data = parse_data(filename)
    price_change = get_price_change(data, product_name)

    if price_change is not None:
        print(f"Зміна ціни на {product_name} за останній місяць: {price_change}")
    else:
        print(f"Немає даних про {product_name} за останній місяць.")
