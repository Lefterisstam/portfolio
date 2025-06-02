# Lefteris' Blog
This is a portfolio website built with Django, where you can post your projects, upload your CV. Visitors are able to download your CV, read your projects and store them to read later.

## Technologies Used
- Python (Django Framework)
- PostgreSQL
- HTML, CSS

## Installation
1. Clone the repository(in terminal):
   git clone https://github.com/Lefterisstam/portfolio.git
   cd portfolio 

2. Install dependencies:
    pip install -r requirements.txt

3. Set up the `.env` file:
   Create a `.env` file in the root directory and add the following:
   SECRET_KEY=your-secret-key
   DB_NAME=your-database-name
   DB_USER=your-database-user
   DB_PASSWORD=your-database-password
   DB_HOST=localhost
   DB_PORT=5432

4. Apply migrations(in terminal):
    python manage.py makemigrations
    python manage.py migrate

5. Run the development server(in terminal):
   python manage.py runserver

6. Upload your photo in home page(if you want):
    1) Add a photo in blog/static/blog/images
    2) In blog/templates/blog/index change this line:
        <img src="{% static "blog/images/evoia-6.jpg" %}
        To this:
        <img src="{% static "blog/images/name-of-your-photo" %}

## Contact
Name: Lefteris Stamoulopoulos
Github: Lefterisstam


