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
    short_name = models.CharField(max_length=20, blank=True, null=True)
    code = models.CharField(max_length=20)
    degree = models.ForeignKey(Degree, blank=True, null=True)
    group = models.CharField(max_length=10, blank=True, null=True)
    semester = models.ForeignKey(Semester, blank=True, null=True)

    def __unicode__(self):
        return self.short_name + ": " + self.name


class Topic(models.Model):
    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')

    subject = models.ForeignKey(Subject)
    number = models.IntegerField(default=1)
    name = models.CharField(max_length=200)


class Classroom(models.Model):
    class Meta:
        verbose_name = _('Classroom')
        verbose_name_plural = _('Classrooms')

    building = models.CharField(max_length=200)
    classroom = models.CharField(max_length=200)
    desc = models.CharField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return self.building + '-' + self.classroom
