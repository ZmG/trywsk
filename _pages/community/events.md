{% extends 'community/events.html' %}
{% load static %}
{% block title %}Events and Meetups - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}

{% block copy_headline %}
# get involved with the Docker community by contributing and sharing
{% endblock %}

{% block copy_introduction %}

# Events

We have a ton of events going on (see below), in many places around the world, in some occasions also via live streaming. Here
    is an overview of the events we know that are going on.

Many of our events happen in the form of a <a href="{% url 'meetups' %}">meetup</a>. These meetups are organized by people from the community to learn
    more about Docker and to share their experiences.

{% endblock %}