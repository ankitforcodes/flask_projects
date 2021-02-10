Once Flask-Bootstrap is initialized, a base template that includes all the Bootstrap
files and general structure is available to the application. The application then takes
advantage of Jinja2’s template inheritance to extend this base template.

bootstrap = Bootstrap(app)

