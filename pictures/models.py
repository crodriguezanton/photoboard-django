from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext as _


from education.models import Subject, Group, Topic, TimetableEntry, Student


class PictureGallery(models.Model):
    class Meta:
        verbose_name = _('Picture Gallery')
        verbose_name_plural = _('Picture Galleries')


class SubjectGallery(PictureGallery):
    class Meta:
        verbose_name = _('Subject Gallery')
        verbose_name_plural = _('Subject Galleries')

    subject = models.ForeignKey(Subject)
    group = models.ForeignKey(Group)


class TopicGallery(SubjectGallery):
    class Meta:
        verbose_name = _('Topic Gallery')
        verbose_name_plural = _('Topic Galleries')

    topic = models.ForeignKey(Topic)


class TimetableEntryGallery(TopicGallery):
    class Meta:
        verbose_name = _('Timetable Entry Gallery')
        verbose_name_plural = _('Timetable Entry Galleries')

    timetable_entry = models.ForeignKey(TimetableEntry)


class Picture(TimeStampedModel):
    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Picture')

    picture = models.ImageField()
    student = models.ForeignKey(Student)
    gallery = models.ForeignKey(TimetableEntryGallery, null=True)