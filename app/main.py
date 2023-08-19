import os
from services import generate_users, astronauts_manager, common_ground
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/hello/", methods=["GET", "POST"])
def hello():
    print("Hello")
    return "Hello"


@app.route("/get-content/", methods=["GET", "POST"])
def lorem_reader():
    file_path = os.path.join(os.path.dirname(__file__), "..", "files_input", "lorem_ipsum.txt")
    with open(file_path) as lr:
        local_var = lr.read()
        return f"<pre>{local_var}<pre>"


@app.route("/generate-users/<int:user_amount>/", methods=["GET", "POST"])
@app.route("/generate-users/", methods=["GET", "POST"])
def starting_point(user_amount: int = 5):
    generated_content = ["Generated Users:<br>"]

    user_info = generate_users.generate_users(user_amount)
    for i in user_info:
        generated_content.append(str(i))

    generated_content.append("<br>Usernames:<br>")
    user_names = generate_users.generate_users(user_amount)

    temp = []

    for n in user_names:
        generated_content.append(n.username)
        temp.append(n.username)  # Append the username to the list

    return "<br>".join(generated_content)


@app.route("/space/", methods=["GET", "POST"])
def json_decoder():
    astronaut_count = astronauts_manager.read_web_json_file()
    return f"\n Amount of json astronauts: {astronaut_count}"


# This function takes some time to process:
@app.route("/mean/", methods=["GET", "POST"])
def csv_decoder():
    av_height, av_weight = common_ground.read_web_csv_file()

    return f"Data:<br>Average Height (centimeters): {av_height}<br>" f"Average Weight (kilograms): {av_weight}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)
