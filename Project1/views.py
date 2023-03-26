from django.http import HttpResponse
import datetime
from datetime import datetime
from django.template import Template, Context
from django.template import loader


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


def say_hello(request): # first view
    return HttpResponse('Say Hello from Python & Django!')

def say_goodbye(request): # second view
    return HttpResponse('Goodbye Django')

def get_date(request):
    p1 = Person('Engineer Rafael', 'Ortiz')
    course_themes = ['Templates', 'Models', 'Forms', 'Views', 'Deploy']
    now = datetime.now()
    # external_doc = open('/home/rortiz/devRafael/Django/Project1/Project1/templates/get_date.html')
    # template = Template(external_doc.read())
    # external_doc.close()
    external_doc = loader.get_template('get_date.html')
    # context = Context({'name': p1.name, 'last_name': p1.last_name, 'current_date': now, 'course_themes': course_themes})
    document = external_doc.render({'name': p1.name, 'last_name': p1.last_name, 'current_date': now, 'course_themes': course_themes})
    return HttpResponse(document)

def calc_age(request, age, year):
    period = year - 2023
    future_age = age + period
    html_content = f"""
    <html>
        <head>
            <title>Django Age</title>
        </head>
        <body>
            <h1>In {year} I will be {future_age} years old</h1>
        </body>
    </html>
    """
    return HttpResponse(html_content)