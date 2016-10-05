from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeFramedModel
from django.utils.translation import gettext as _

from education.constants import DAY_CHOICES


class Student(models.Model):
    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.__unicode__()


class University(models.Model):
    class Meta:
        verbose_name = _('University')
        verbose_name_plural = _('Universities')

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=6)

    def __unicode__(self):
        return self.short_name + ": " + self.name


class Faculty(models.Model):
    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=10)
    university = models.ForeignKey(University, blank=True, null=True)

    def __unicode__(self):
        return self.short_name + ": " + self.name


class Degree(models.Model):
    class Meta:
        verbose_name = _('Degree')
        verbose_name_plural = _('Degrees')

    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Semester(models.Model):
    class Meta:
        verbose_name = _('Semester')
        verbose_name_plural = _('Semesters')

    name = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, blank=True, null=True)
    short_name = models.CharField(max_length=6)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class SchoolYear(models.Model):
    class Meta:
        verbose_name = _('School Year')
        verbose_name_plural = _('School Years')

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=6)
    university = models.ForeignKey(Faculty, blank=True, null=True)
    start = models.DateField()
    end = models.DateField()
    semesters = models.ManyToManyField(Semester)

    def __unicode__(self):
        return self.name


class Subject(models.Model):
    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    degree = models.ForeignKey(Degree, blank=True, null=True)

    def __unicode__(self):
        return self.short_name + ": " + self.name


class Topic(models.Model):
    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    subject = models.ForeignKey(Subject)
    number = models.IntegerField(default=1)
    name = models.CharField(max_length=200)



class Group(models.Model):
    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, blank=True, null=True)
    semester = models.ForeignKey(Semester, blank=True, null=True)

    def __unicode__(self):
        return self.subject.short_name + ' ' + self.name + ' ' + self.semester.short_name


class Enroll(models.Model):
    class Meta:
        verbose_name = _('Enroll')
        verbose_name_plural = _('Enroll')

    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    group = models.ForeignKey(Group)


class Classroom(models.Model):
    class Meta:
        verbose_name = _('Classroom')
        verbose_name_plural = _('Classrooms')

    building = models.CharField(max_length=200)
    classroom = models.CharField(max_length=200)
    desc = models.CharField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.building + '-' + self.classroom


class ClassDay(models.Model):
    class Meta:
        verbose_name = _('Class Day')
        verbose_name_plural = _('Class Days')

    faculty = models.ForeignKey(Faculty, blank=True, null=True)
    day = models.IntegerField(default=1, choices=DAY_CHOICES)

    def __unicode__(self):
        return self.get_day_display()

    def is_today(self):
        if datetime.today().isoweekday() == self.number:
            return True
        else:
            return False

    @staticmethod
    def get_today():
        if ClassDay.objects.filter(number=datetime.today().isoweekday()).count() != 0:
            return ClassDay.objects.get(number=datetime.today().isoweekday())
        else:
            return None


class ClassUnit(models.Model):
    class Meta:
        verbose_name = _('Class Unit')
        verbose_name_plural = _('Class Units')

    faculty = models.ForeignKey(Faculty, blank=True, null=True)
    number = models.IntegerField(default=1)
    days = models.ManyToManyField(ClassDay)
    start = models.TimeField()
    end = models.TimeField()

    def __unicode__(self):
        return self.start.strftime("%H:%M") + " - " + self.end.strftime("%H:%M")

    def is_now(self):
        return self.start <= datetime.now().time() <= self.end

    def is_later(self):
        return self.start > datetime.now().time()

    def is_before(self):
        return self.end < datetime.now().time()

    def is_before_or_current(self):
        return self.start <= datetime.now().time()


class WeeklyTimetableEntry(models.Model):
    class Meta:
        verbose_name = _('Weekly Timetable Entry')
        verbose_name_plural = _('Weekly Timetable Entries')

    group = models.ForeignKey(Group, blank=True, null=True)
    subject = models.ForeignKey(Subject, blank=True, null=True)
    classroom = models.ForeignKey(Classroom, blank=True, null=True)
    day = models.ForeignKey(ClassDay)
    unit = models.ForeignKey(ClassUnit)

    def __unicode__(self):
        if self.subject is not None and self.group is not None:
            return self.subject.short_name + " - " + self.group.name + " (" + self.day.__unicode__() + " " + self.unit.__unicode__() + ")"
        else:
            return "(" + self.day.__unicode__() + " " + self.unit.__unicode__() + ")"

    def get_list(self):

        students = Student.objects.filter(enroll__classenroll__subject=self.subject, group=self.group).order_by(
            "surname", "name")

        return students

    def is_now(self):
        if self.date.is_today() and self.time.is_now():
            return True
        else:
            return False

    def is_later(self):
        return self.time.is_later()

    def is_before(self):
        return self.time.is_before()

    def is_before_or_current(self):
        return self.time.is_before_or_current()

    def class_active(self, day):
        return True  # TODO


class TimetableEntry(models.Model):
    class Meta:
        verbose_name = _('Timetable Entry')
        verbose_name_plural = _('Timetable Entry')

    weekly_timetable_entry = models.ForeignKey(WeeklyTimetableEntry, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    active = models.BooleanField(default=True)


class NonLectiveDay(models.Model):
    class Meta:
        verbose_name = _('Non Lective Day')
        verbose_name_plural = _('Non Lective Days')

    name = models.CharField(max_length=200)
    day = models.DateField()
