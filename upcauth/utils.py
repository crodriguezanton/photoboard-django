# coding=utf-8
import requests
from BeautifulSoup import BeautifulSoup

from education.models import Subject
from pictures.models import SubjectGallery


def login(username, password):
    """ Fake request to atenea.upc.edu in order to check login credentials """
    r = requests.post('https://atenea.upc.edu/moodle/login/index.php?authCAS=CAS', data={'submit': 'Iniciar Sessió'})
    soup = BeautifulSoup(r.content)

    action = "https://cas.upc.edu" + soup.findAll('form')[0].get('action')
    lt = soup.find('input', {'name': 'lt'}).get('value')
    execution = soup.find('input', {'name': 'execution'}).get('value')
    _eventId = soup.find('input', {'name': '_eventId'}).get('value')
    username = username
    password = password
    submit = 'Entra'
    warn = 'true'

    data = {
        'lt':        lt,
        'execution': execution,
        '_eventId':  _eventId,
        'username':  username,
        'password':  password,
        'submit':    submit,
        'warn':      warn
    }

    return requests.post(action, data=data)


def checkLogin(username, password):
    """ If the url of the page obtained after performing login method equals atenea.upc.edu/moodle, login was ok. """
    
    r = login(username, password)

    return r.url == 'http://atenea.upc.edu/moodle/'


def getCourses(username, password):
    """ Gets courses that the student is enrolled to by finding the <h3 class="coursename"> tag. """
    
    r = login(username, password)
    soup = BeautifulSoup(r.content)
    coursesraw = soup.findAll('h3', {'class': 'coursename'})

    courses = []
    for course in coursesraw:
        text = course.find('a').text
        if len(text.split(" - ")) > 1 and "Metacurs" not in text:
            id = text.split(" - ")[0]
            name = text.split(" - ")[1].split(" (")[0]

            courses.append(id)

            s, created = Subject.objects.get_or_create(code=id, name=name)

            if created:
                SubjectGallery.objects.get_or_create(subject=s)

    return Subject.objects.filter(code__in=courses)
