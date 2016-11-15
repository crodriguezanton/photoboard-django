# coding=utf-8
import requests
from BeautifulSoup import BeautifulSoup
from datetime import datetime, time, date
from icalendar import Calendar, Event


def login(username, password):
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


def checkLogin():
    r = login()

    return r.url == 'http://atenea.upc.edu/moodle/'


def getCourses():
    r = login()
    soup = BeautifulSoup(r.content)
    courses = soup.findAll('h3', {'class': 'coursename'})

    return courses
