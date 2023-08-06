from services import generate_users
from services import astronauts_manager
from services import common_ground


def starting_point():
    print("Generated Users:\n")
    user_info = generate_users.generate_users(5)

    for i in user_info:
        print(i)

    print("\nUsernames:\n")

    user_names = generate_users.generate_users(5)

    for n in user_names:
        print(n.username)


def json_decoder():
    print(f"\n Amount of json austronauts: {astronauts_manager.read_web_json_file()}")


def csv_decoder():
    common_ground.read_web_csv_file()


if __name__ == "__main__":
    starting_point()
    json_decoder()
    csv_decoder()
