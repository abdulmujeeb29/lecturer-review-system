# Lecturer Review System.

**The Lecturer Review System is a web-based application that allows students to provide anonymous feedback on their lecturers. The system provides three user roles: students, admins, and lecturers.**

# Installation

1. Clone this repository to your local machine.
2. Navigate to the root directory of the project.
3. Create a virtual environment: python -m venv env.
4. Activate the virtual environment: source env/bin/activate.
5. Install the required dependencies: pip install -r requirements.txt.
6. Run migrations: python manage.py migrate.
7. Create a superuser account: python manage.py createsuperuser.
8. Start the development server: python manage.py runserver.

# Architecture
_The Lecturer Review System is built using the Django web framework and follows the Model-View-Template (MVT) architecture pattern. The system has the following models:_

+ Student: Represents a student in the system.
+ Admin: Represents an admin in the system.
+ Lecturer: Represents a lecturer in the system.
+ Review: Represents a review submitted by a student for a lecturer.
+ 
The system has the following views:

+ Student views: Allow students to submit reviews and view their previous reviews.
+ Lecturer views: Allow lecturers to view their reviews and view their overall rating.
+ Admin views: Allow admins to view all reviews and manage users.
+ and a whole lot more views adding to the funtionalities.

The system has the following templates:

+ Base template: Defines the overall structure of the application.
+ Student templates: Display forms for students to submit reviews and display their previous reviews.
+ Lecturer templates: Display reviews for a lecturer and their overall rating.
+ Admin templates: Display all reviews and allow admins to manage users.


# User roles and functionalities
The Lecturer Review System provides three user roles with the following functionalities:

+ Student: Can submit reviews for their lecturers,view their previous reviews and also update their profiles for easy accessibility.
+ Lecturer: Can view their reviews, their overall rating and alsio update their profile.
+ Admin: Can view all reviews, manage users(both students and lecturers), activate/deactivate their accounts thereby restricting their access to login and also deleting their profile entirely

# Technologies used
The Lecturer Review System is built using the following technologies:

+ Python 3.8
+ Django 3.2.4
+ Bootstrap 5
+ Jquery
+ Mysql

# Contribution guidelines
**We welcome contributions to the Lecturer Review System. If you would like to contribute, please create a new branch for your changes and submit a pull request. We kindly ask that you follow our code style and submit tests with your changes.**

_Thank you for considering contributing to the Lecturer Review System!_
