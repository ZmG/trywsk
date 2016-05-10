from django.db import models
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
import os
# Create your models here.

class TeamMember(models.Model):

    full_name = models.CharField(max_length=80, blank=True)
    bio = models.TextField()
    email = models.EmailField(blank=True,
                              help_text="This address will not be shown")
    gravatar_email = models.EmailField(_('gravatar email'), blank=True,
        help_text="This address will define which picture of you is shown, but the address itself will be hidden. <br>"
        "Change the picture at <a href='http://www.gravatar.com'>www.gravatar.com</a><br>")
    index_name = models.CharField(max_length=80, blank=True)
    github_handle = models.CharField(max_length=80, blank=True)
    sort_weight = models.IntegerField(default=10)
    show_as_team = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{}".format(self.full_name)

def get_file_path(instance, filename):
    return os.path.join('assets/img/', str(instance.alt), filename)  # the category name indicates the subdirectory

class Image(models.Model):

    alt = models.CharField(max_length=80)
    image_caption = models.CharField(max_length=80, blank=True)
    image = models.FileField(upload_to=get_file_path, blank=True, null=True)

    def uri(self):
        return "https://s3.amazonaws.com/www.docker.io-media/{}".format(str(self.image))

    def __unicode__(self):
        return u"{}".format(self.alt)

class Tag(models.Model):

    name = models.CharField(max_length=80)
    added_date = models.DateField(default=datetime.now())
    description = models.TextField(blank=True, help_text="Markdown format accepted")

    def __unicode__(self):
        return u"{}".format(self.name)

class NewsItem(models.Model):

    title = models.CharField(max_length=80, blank=False)
    text = models.TextField(blank=True, help_text="Markdown format accepted")
    link = models.URLField(blank=True)
    publication_date = models.DateField(default=datetime.now())
    show = models.BooleanField(default=False)
    author = models.ForeignKey(TeamMember)
    creation_date = models.DateTimeField(default=datetime.now(), editable=False)
    # images = models.ManyToManyField(Image, blank=True)  # Images not included yet

    def __unicode__(self):
        return u"{}".format(self.title)

class Event(models.Model):

    title = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=80, blank=True)
    date_and_time = models.DateTimeField(default=datetime.utcnow(), help_text="Time local to the event")
    text = models.TextField(blank=True, help_text="Markdown format accepted")
    link = models.URLField(blank=True)
    # images = models.ManyToManyField(Image, blank=True) ## image not included yet

    def __unicode__(self):
        return u"{}".format(self.title)

class PostCategory(models.Model):

    name = models.CharField(max_length=80, blank=True)  # eg. press, community, etc.
    added_date = models.DateField(default=datetime.now())
    description = models.TextField(blank=True, help_text="Markdown format accepted")

    def __unicode__(self):
        return u"{}".format(self.name)

class GenericPost(models.Model):

    title = models.CharField(max_length=80, blank=True)
    publication_date = models.DateField(default=datetime.now())
    text = models.TextField(blank=True, help_text="Markdown format accepted")
    link = models.URLField(blank=True)
    category = models.ForeignKey(PostCategory)
    images = models.ManyToManyField(Image, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return u"{}".format(self.title)
