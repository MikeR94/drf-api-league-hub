# **_League Hub - Django REST Framework API_**

This repository is the back-end REST API which is used by my front-end project, [League Hub](https://ci-league-hub.herokuapp.com/).

You can view the live site here - <a href="https://ci-league-hub.herokuapp.com/" target="_blank" rel="noopener">League Hub</a>

# Contents

- [**Objective**](#objective)
- [**Entity Relationship Diagram**](#entity-relationship-diagram)
- [**Database**](#database)
- [**Models**](#models)
- [**Testing**](#testing)
  - [**Manual Testing**](#manual-testing)
  - [**PEP8 Validation**](#pep8-validation)
  - [**Bugs Fixed**](#bugs-fixed)
  - [**Bugs Unresolved**](#bugs-unresolved)
- [**Technologies Used**](#technologies-used)
- [**Deployment To Heroku**](#deployment-to-heroku)
- [**Cloning This Project**](#cloning-and-setting-up-this-project)
- [**Credits**](#credits)
  - [**Content**](#content)
  - [**Media**](#media)
- [**Acknowledgments**](#acknowledgements)

# Objective

The objective of creating this API is to provide a fast, reliable and secure means of providing data to be used in my [League Hub](https://ci-league-hub.herokuapp.com/) front-end project. I aim to create simple, intuitive and purposeful models that will be used to represent the data required for the project. All API endpoints will serve a specific purpose and will be tested thoroughly to prevent any attempt to create/edit/delete any data without the correct permissions.

[Back to top](#contents)

# Entity Relationship Diagram

To create the entity relationship diagram, I used a graph modelling tool [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) which I used on my fourth project. It shows the entire relationship between all models in the database. After following the steps required to install Graph Models, I then used [dreampuf](https://dreampuf.github.io/GraphvizOnline/) to present the data in a clear and professional way. <br /><br />

![Entity Relationship Diagram](documentation/readme_images/erd-image.png)

[Back to top](#contents)

# Database

For this project, I implemented two databases.

The first one was the [SQLite](https://www.sqlite.org/index.html). This was used for the development side of the project and allows you to have a small, fast, self-contained SQL database engine.

The second database, which is a PostgreSQL database hosted by [ElephantSQL](https://www.elephantsql.com/) was used for the production database.

To visually see the data within both databases, I used an excellent, lightweight tool called [TablePlus](https://tableplus.com/) which allows me to see all the data instantly and modify the data if needed through UI if I ever need to.

### Production Database - Table Plus

![Table Plus Prod](documentation/readme_images/table-plus-prod.png)

### Development Database - Table Plus

![Table Plus Dev](documentation/readme_images/table-plus-dev.png)

[Back to top](#contents)

# Models

### Champions

The champions model is designed to contain all the relevant information regarding a League of Legends champion.

| Database Value               | Field Type    | Field Argument                                                |
| ---------------------------- | ------------- | ------------------------------------------------------------- |
| owner                        | ForeignKey    | User, on_delete=models.CASCADE                                |
| created_at                   | DateTimeField | auto_now_add=True                                             |
| updated_at                   | DateTimeField | auto_now=True                                                 |
| name                         | CharField     | max_length=255                                                |
| alias                        | CharField     | max_length=255                                                |
| champ_image                  | ImageField    | upload_to="images/", default="../Ivern_0_iumwtm", blank=False |
| lore                         | TextField     | blank=False                                                   |
| role                         | CharField     | max_length=32, choices=role_choices, blank=False              |
| champ_class                  | CharField     | max_length=32, choices=champ_class_choices, blank=False       |
| range                        | CharField     | max_length=32, choices=range_choices, blank=False             |
| difficulty                   | CharField     | max_length=32, choices=difficulty_choices, blank=False        |
| passive_ability              | CharField     | max_length=255                                                |
| passive_ability_description  | TextField     | blank=False                                                   |
| passive_ability_image        | ImageField    | upload_to="images/", default="../IvernW_muxhxj", blank=False  |
| ability_1                    | CharField     | max_length=255                                                |
| ability_1_description        | TextField     | blank=False                                                   |
| ability_1_image              | ImageField    | upload_to="images/", default="../IvernW_muxhxj", blank=False  |
| ability_2                    | CharField     | max_length=255                                                |
| ability_2_description        | TextField     | blank=False                                                   |
| ability_2_image              | ImageField    | upload_to="images/", default="../IvernW_muxhxj", blank=False  |
| ability_3                    | CharField     | max_length=255                                                |
| ability_3_description        | TextField     | blank=False                                                   |
| ability_3_image              | ImageField    | upload_to="images/", default="../IvernW_muxhxj", blank=False  |
| ultimate_ability             | CharField     | max_length=255                                                |
| ultimate_ability_description | TextField     | blank=False                                                   |
| ultimate_ability_image       | ImageField    | upload_to="images/", default="../IvernW_muxhxj", blank=False  |

```Python
role_choices = [
    ("top", "Top"),
    ("mid", "Mid"),
    ("jungle", "Jungle"),
    ("adc", "ADC"),
    ("support", "Support"),
]

champ_class_choices = [
    ("controller", "Controller"),
    ("fighter", "Fighter"),
    ("mage", "Mage"),
    ("marksman", "Marksman"),
    ("slayer", "Slayer"),
    ("tank", "Tank"),
    ("specialist", "Specialist"),
]

range_choices = [
    ("melee", "Melee"),
    ("ranged", "Ranged"),
]

difficulty_choices = [
    ("low", "Low"),
    ("moderate", "Moderate"),
    ("high", "High"),
]
```

### Comment

The comment model allows the user to create a comment on a champion. If a comment is deleted, it is deleted from both the User and Champion models

| Database Value | Field Type    | Field Argument                     |
| -------------- | ------------- | ---------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE     |
| champion       | ForeignKey    | Champion, on_delete=models.CASCADE |
| created_at     | DateTimeField | auto_now_add=True                  |
| updated_at     | DateTimeField | auto_now=True                      |
| comment        | TextField     |                                    |

### Profile

The profile model has a one-to-one relationship with the Django User model. This means that for every User that signs up to the website, there will be a corresponding Profile model which is used to define some additional values relative to the user. I've added a boolean field which will be used to determine if that user is a staff member or not. If this value is set to True then they will have staff permissions and will be able to perform all functionality of that of a staff member.

| Database Value | Field Type    | Field Argument                                       |
| -------------- | ------------- | ---------------------------------------------------- |
| owner          | OneToOneField | User, on_delete=models.CASCADE                       |
| created_at     | DateTimeField | auto_now_add=True                                    |
| updated_at     | DateTimeField | auto_now=True                                        |
| first_name     | CharField     | max_length=255, blank=True                           |
| last_name      | CharField     | max_length=255, blank=True                           |
| is_staff       | BooleanField  | default=False                                        |
| avatar_image   | ImageField    | upload_to="images/", default="../Amumu_0_wzmdhw.jpg" |

### Upvote

The upvote model is a small model that is used to store the upvotes for a champion. An upvote is a foreign key of both the User and Champion model and if the User or the Champion is ever deleted then any Upvotes related to either the User or the Champion will be deleted.

| Database Value | Field Type    | Field Argument                                             |
| -------------- | ------------- | ---------------------------------------------------------- |
| owner          | ForeignKey    | User, on_delete=models.CASCADE                             |
| champion       | ForeignKey    | Champion, on_delete=models.CASCADE, related_name="upvotes" |
| created_at     | DateTimeField | auto_now_add=True                                          |

[Back to top](#contents)

# Testing

- ## Manual Testing

| Application | Endpoint                  | Expected Result                                                                                                                                            | Pass/Fail |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Champions   | champions/                | Return a list of all the champions in the database ordered by name                                                                                         | Pass      |
| Champions   | champions/                | Searching for a champion by alphanumeric characters returns a list of matches                                                                              | Pass      |
| Champions   | champions/                | Applying a Top role filter returns only champions that have the role value of Top                                                                          | Pass      |
| Champions   | champions/                | Applying a Mid role filter returns only champions that have the role value of Mid                                                                          | Pass      |
| Champions   | champions/                | Applying a Jungle role filter returns only champions that have the role value of Jungle                                                                    | Pass      |
| Champions   | champions/                | Applying a ADC role filter returns only champions that have the role value of ADC                                                                          | Pass      |
| Champions   | champions/                | Applying a Support role filter returns only champions that have the role value of Support                                                                  | Pass      |
| Champions   | champions/<int:pk>/       | Returns a single champion with a correct ID and a list of all it's values                                                                                  | Pass      |
| Champions   | champions/<int:pk>/edit   | Returns a single champion with a correct ID and a list of all it's values and a staff member can edit the champion                                         | Pass      |
| Champions   | champions/<int:pk>/edit   | Returns a single champion with a correct ID and a list of all it's values and the owner can edit the champion                                              | Pass      |
| Champions   | champions/<int:pk>/edit   | Returns a single champion with a correct ID and a list of all it's values and a non-staff member can't edit the champion                                   | Pass      |
| Champions   | champions/<int:pk>/delete | Returns a single champion with a correct ID and a list of all it's values and a staff member can delete the champion                                       | Pass      |
| Champions   | champions/<int:pk>/delete | Returns a single champion with a correct ID and a list of all it's values and the owner can delete the champion                                            | Pass      |
| Champions   | champions/<int:pk>/delete | Returns a single champion with a correct ID and a list of all it's values and a non-staff member can't delete the champion                                 | Pass      |
| Champions   | champions/create          | Return a list of all the champions a staff member can create a new champion                                                                                | Pass      |
| Champions   | champions/create          | Return a list of all the champions a non-staff member can't create a champion                                                                              | Pass      |
| Comments    | comments/                 | Return a list of all the comments in order of creation date                                                                                                | Pass      |
| Comments    | comments/                 | Applying a Champion filter will return all the comments relating to that specific champion only                                                            | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values                                                                                   | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values and the owner can edit the comment                                                | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values and if the user isn't the owner of the comment, they can't edit it                | Pass      |
| Comments    | comments/<int:pk>/        | Returns a single comment with a correct ID and a list of all it's values and even if the user is a staff member, they can't edit it                        | Pass      |
| Comments    | comments/delete/<int:pk>/ | Returns a single comment with a correct ID and a list of all it's values and if the owner of the comment can delete the comment                            | Pass      |
| Comments    | comments/delete/<int:pk>/ | Returns a single comment with a correct ID and a list of all it's values and if the user is a staff member, they can delete the comment                    | Pass      |
| Comments    | comments/delete/<int:pk>/ | Returns a single comment with a correct ID and a list of all it's values and if the user is not the owner of the comment, they can't delete it             | Pass      |
| Profiles    | profiles/                 | Returns a list of all the profiles in the database ordered by creation date                                                                                | Pass      |
| Profiles    | profiles/<int:pk>/        | Returns a single profile with a correct ID and a list of all it's values and if the user isn't the owner of the profile, they can't edit it                | Pass      |
| Profiles    | profiles/<int:pk>/        | Returns a single profile with a correct ID and a list of all it's values and if the user is the owner of the profile, they can edit it                     | Pass      |
| Profiles    | profiles/<int:pk>/        | Returns a single profile with a correct ID and a list of all it's values and if the user is a staff member, they can't edit it                             | Pass      |
| Upvotes     | upvotes/                  | Returns a list of all the current upvotes in the database                                                                                                  | Pass      |
| Upvotes     | upvotes/                  | If a user is logged in, they can make a post request to create an upvote for a champion                                                                    | Pass      |
| Upvotes     | upvotes/                  | If a user is logged in and they have already upvoted a champion and make a second post request to upvote it again, it fails with "Possible duplicate vote" | Pass      |
| Upvotes     | upvotes/                  | If a user is logged in and they have not already upvoted a champion and make a post request to upvote it, it succeeds and increases the upvote_count by 1  | Pass      |
| Upvotes     | upvotes/                  | If a user is logged out they are not able to upvote a champion                                                                                             | Pass      |
| Upvotes     | upvotes/<int:pk>/         | Returns a single upvote with a correct ID and a list of all it's values                                                                                    | Pass      |
| Upvotes     | upvotes/<int:pk>/         | If the user is the owner of the upvote, they can delete the upvote and it will delete it from the champion and decrease the upvote_count by 1              | Pass      |
| Upvotes     | upvotes/<int:pk>/         | If the user is not the owner of the upvote, they are unable to delete the upvote                                                                           | Pass      |
| Upvotes     | upvotes/<int:pk>/         | If the user is not the owner of the upvote but is a staff member, they are unable to delete the upvote                                                     | Pass      |

- ## PEP8 Validation

  - Code Validation Here

- ## Bugs Fixed

  ### Authenticated users deleting comments

  When conducting manual tests for the API endpoints, I encountered a small bug which allowed users to delete comments that were not theirs. Although I had handled this issue in the front end, locking down the back-end is the most suitable solution to prevent any malicious attempt to delete comments by directly targeting the API.

  The main problem was due to permissions. The comments/delete/<int:pk>/ endpoint was only checking if the user making the request was authenticated only.

  To fix this, I created a new permission which would check if the user making the request was either a staff member or the owner of the comment<br />

  ![IsStaffOrOwnerOrReadOnly](documentation/readme_images/isstafforownerorreadonly-image.png)

- ## Bugs Unresolved

  - As far as I'm aware, after extensive manual testing, I'm not aware of any unresolved bugs<br />

# Technologies Used

## Languages

- [Python](https://www.python.org/) - A programming language that lets you work quickly
  and integrate systems more effectively

## Libraries and Frameworks

- [Django](https://pypi.org/project/Django/) - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
- [Django REST Framework](https://pypi.org/project/djangorestframework/) - A powerful and flexible toolkit for building Web APIs

## Packages

- [asgiref](https://pypi.org/project/asgiref/) - A standard for Python asynchronous web apps and servers to communicate with each other,
- [black](https://pypi.org/project/black/) - A Python code formatter
- [certifi](https://pypi.org/project/certifi/) - For validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts
- [charset-normalizer](https://pypi.org/project/charset-normalizer/) - A library that helps you read text from an unknown charset encoding
- [cloudinary](https://pypi.org/project/cloudinary/) - Easily integrate your application with Cloudinary
- [dj-database-url](https://pypi.org/project/dj-database-url/) - Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
- [dj-rest-auth](https://pypi.org/project/dj-rest-auth/) - API endpoints for handling authentication securely in Django Rest Framework
- [django-allauth](https://pypi.org/project/django-allauth/) - Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/) - package that facilitates integration with Cloudinary by implementing Django Storage API
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) - Adds Cross-Origin Resource Sharing (CORS) headers to responses.
- [django-extensions](https://pypi.org/project/django-extensions/) - Collection of global custom management extensions for the Django Framework.
- [django-filter](https://pypi.org/project/django-filter/) - Declaratively add dynamic QuerySet filtering from URL parameters.
- [django-rest-auth](https://pypi.org/project/django-rest-auth/) - Provides a set of REST API endpoints for Authentication and Registration
- [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/) - JSON Web Token authentication plugin for the Django REST Framework.
- [gunicorn](https://pypi.org/project/gunicorn/) - A Python WSGI HTTP Server for UNIX.
- [idna](https://pypi.org/project/idna/) - Support for the Internationalized Domain Names in Applications (IDNA) protocol
- [mypy-extensions](https://pypi.org/project/mypy-extensions/) - Defines extensions to the standard “typing” module that are supported by the mypy type checker and the mypyc compiler.
- [oauthlib](https://pypi.org/project/oauthlib/) - Implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.
- [pathspec](https://pypi.org/project/pathspec/) - Utility library for pattern matching of file paths
- [Pillow](https://pypi.org/project/Pillow/) - Adds image processing capabilities to your Python interpreter
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python
- [pycodestyle](https://pypi.org/project/pycodestyle/) - A tool to check your Python code against some of the style conventions in PEP 8.
- [pydot](https://pypi.org/project/pydot/) - Library to generate .dot files which can be used to show ERD's
- [PyJWT](https://pypi.org/project/PyJWT/) - Library for encoding and decoding JSON Web Tokens (JWT)
- [pyparsing](https://pypi.org/project/pyparsing/) - Python parsing module
- [pytz](https://pypi.org/project/pytz/) - Allows accurate and cross platform timezone calculations
- [requests](https://pypi.org/project/requests/) - Allows you to send HTTP/1.1 requests
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - OAuthlib authentication support for Requests
- [six](https://pypi.org/project/six/) - A Python 2 and 3 compatibility library
- [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.
- [urllib3](https://pypi.org/project/urllib3/) - A powerful, user-friendly HTTP client for Python

## Other Tools

- [VSCode](https://code.visualstudio.com/) - Used to create and edit the website.
- [GitHub](https://github.com/) - Used to host and deploy the website as well as manage the project.
- [GitBash](<https://en.wikipedia.org/wiki/Bash_(Unix_shell)>) - Terminal used to push changes to the GitHub repository.
- [Heroku](https://dashboard.heroku.com) - Used to deploy the website
- [SQLite](https://www.sqlite.org/index.html) - An open-source, zero-configuration, self-contained, stand-alone, transaction relational database engine designed to be embedded into an application.
- [ElephantSQL](https://www.elephantsql.com/) - Provides a browser tool for SQL queries where you can create, read, update and delete data directly from your web browser.
- [Cloudinary](https://cloudinary.com/) - Used to host all static files .
- [TablePlus](https://tableplus.com/) - Used to view databases in a clean, simple way.
- [Virutal Environment](https://docs.python.org/3/library/venv.html) - Used to create a virtual environment
- [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) - Used to generate a .dot file for all apps and models
- [dreampuf](https://dreampuf.github.io/GraphvizOnline/) - Used to present the .dot file in the form of a database diagram

[Back to top](#contents)

# Deployment To Heroku

The project was deployed to [Heroku](https://www.heroku.com). The deployment process is as follows:

The live link to the Github repository can be found here - https://github.com/MikeR94/CI-Project-Portfolio-5

[Back to top](#contents)

# Cloning and setting up this project

If you wish to clone and setup this project locally then the process is as follows:

[Back to top](#contents)

# Credits

### Content

- Content 1

[Back to top](#contents)

# Acknowledgments

Acknowledgements

Mike Ralph 2023.

[Back to top](#contents)
