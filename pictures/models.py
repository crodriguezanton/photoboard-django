from __future__ import unicode_literals

import uuid as uuid
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext as _


from education.models import Subject, Topic, Student


class PictureGallery(models.Model):
    class Meta:
        verbose_name = _('Picture Gallery')
        verbose_name_plural = _('Picture Galleries')


class SubjectGallery(PictureGallery):
    class Meta:
        verbose_name = _('Subject Gallery')
        verbose_name_plural = _('Subject Galleries')

    subject = models.OneToOneField(Subject, related_name='subject_gallery')


class TopicGallery(SubjectGallery):
    class Meta:
        verbose_name = _('Topic Gallery')
        verbose_name_plural = _('Topic Galleries')

    topic = models.ForeignKey(Topic)


class Picture(TimeStampedModel):
    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Picture')

    picture = models.ImageField(null=True, blank=True)
    depth = models.ImageField(null=True, blank=True)

    student = models.ForeignKey(Student, null=True, blank=True)
    gallery = models.ForeignKey(SubjectGallery, null=True, blank=True, related_name='pictures')


class PictureRequest(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    ready = models.BooleanField(default=False)
    picture = models.ForeignKey(Picture, null=True, blank=True)
    subject = models.ForeignKey(Subject, null=True, blank=True)
