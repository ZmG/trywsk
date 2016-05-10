from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView



urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'base.views.home', name='home'),
    url(r'^$', TemplateView.as_view(template_name='getting-started.md'), name="home"),
    # Learn more section
    url(r'^learn_more/$', TemplateView.as_view(template_name='learn-more.md'), name="learn_more"),
    url(r'^about/$', RedirectView.as_view(url=reverse_lazy('learn_more')), name='about'),  # this is a redirect
    url(r'^the_whole_story/$', TemplateView.as_view(template_name='the-whole-story.md'), name="the_whole_story"),
    url(r'^the-whole-story/$', RedirectView.as_view(url=reverse_lazy('the_whole_story'))),

    # Get Started
    url(r'^gettingstarted/$', TemplateView.as_view(template_name='getting-started.md'), name="getting_started"),
    url(r'^tutorial/', include('wsk_tutorial.urls')),

    # Community section
    url(r'^community/$', TemplateView.as_view(template_name='community/community.md'), name="community"),
    url(r'^events/$', 'base.views.events', name="events"),
    url(r'^meetups/$', TemplateView.as_view(template_name='community/meetups.md'), name="meetups"),
    url(r'^meetups/organize/$', TemplateView.as_view(template_name='community/meetups-organize.md'), name="meetups-organize"),
    url(r'^live/$', TemplateView.as_view(template_name='live.md'), name="live"),

    # About section
    url(r'^news/$', 'base.views.news', name="news"),
    url(r'^team/$', 'base.views.team', name="team"),
    url(r'^jobs/$', TemplateView.as_view(template_name='about/jobs.md'), name="jobs"),
    url(r'^press/$', 'base.views.press', name="press"),

    # Special purpose pages
    url(r'^news_signup/$', 'base.views.email_thanks', name='email_thanks'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
