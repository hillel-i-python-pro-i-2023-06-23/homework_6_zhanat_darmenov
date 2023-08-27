# homework_6_zhanat_darmenov

HW6 repo for Edu purposes

Use: "make d-homework-i-run" to RUN App in Docker Compose


Routes:

Basic start Page: (Will trigger DB Creation)
"/"
"/hello/"

Will read and print a file:
"/get-content/"

User generation:
"/generate-users/<int:user_amount>"
"/generate-users/"

Will count Astronauts:
"/space/"

Will return average stats:
"/mean/"


HW9 Routes:

Add a User in DB:
"/<string:contact_name>/<string:phone_value>/"

Remove User from DB:
"/rmv/<string:contact_name>/<string:phone_value>/"

Show all Users:
"/readall/"
