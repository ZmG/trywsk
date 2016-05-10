{% extends 'about/jobs.html' %}
{% load static %}
{% block title %}Jobs - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}


{% block copy_headline %}
# Learn more about working with the people behind the whale #
{% endblock %}

{% block copy_introduction %}

# Join the team! #

We are a team of developers, building tools for developers --and Gordon. Yes, that's the turtle.

<img src="{% static 'img/about/team_picture.jpg' %}" alt="team picture">

### Just some of the perks:

* Work on open source -- collaborate with people in and outside of the company
* Work from the greenest office you've seen - we've got a real jungle here
* <a href="http://techcrunch.com/2013/05/07/tc-cribs-dotcloud-jungle-plants/" target="_blank">Awesome office</a> downtown San Francisco
* Monthly hackday: Work on the things you'd otherwise find no time for

### We're currently hiring for the following positions:

{% endblock %}