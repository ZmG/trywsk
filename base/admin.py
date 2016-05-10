__author__ = 'thatcher'

from django.contrib import admin

# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.sessions.
from django.contrib.sessions.models import Session
from .models import *
from base.forms import *


def images_thubmnail(self):
  return '<img style="max-height: 80px; width: auto;" src="{}" alt="{}" >'.format(self.uri(), self.alt)
  # return self.uri()

images_thubmnail.short_description = 'Thumbnail'
images_thubmnail.allow_tags = True


class TeamMemberAdmin(admin.ModelAdmin):
    model = TeamMember
    list_display = ['full_name', 'sort_weight', 'show_as_team']
admin.site.register(TeamMember, TeamMemberAdmin)


class NewsItemAdmin(admin.ModelAdmin):
    model = NewsItem
    list_display = ['id', 'title', 'publication_date', 'show', 'author']
admin.site.register(NewsItem, NewsItemAdmin)


class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ['title', 'location', 'date_and_time']
admin.site.register(Event, EventAdmin)

class PostAdmin(admin.ModelAdmin):
    model = GenericPost
    list_display = ['title', 'category', 'publication_date']
admin.site.register(GenericPost, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    model = PostCategory
    list_display = ['name', 'added_date']
admin.site.register(PostCategory, CategoryAdmin)

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = [images_thubmnail, 'alt', 'image_caption', 'image', ]
admin.site.register(Image, ImageAdmin)

class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['name', 'added_date']
admin.site.register(Tag, TagAdmin)
