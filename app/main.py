from services import generate_users


def starting_point():
    lister = generate_users.generate_users(5)

    for i in lister:
        print(i)


if __name__ == "__main__":
    starting_point()
