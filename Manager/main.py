from Restaurant.restaurant import Restaurant


def main():
    restaurants = [
        Restaurant("Kafe-bar Oksana", 10, 23, 20),
        Restaurant(),
        Restaurant.get_instance(),
        Restaurant.get_instance()
    ]

    for restaurant in restaurants:
        print(restaurant)


main()
