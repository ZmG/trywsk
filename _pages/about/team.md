{% extends 'about/team.html' %}
{% load static %}
{% block title %}The team - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}


{% block copy_headline %}
# The guys behind the whale #
{% endblock %}

{% block copy_introduction %}

# Team

Docker is an open source project that relies on the support of a great community of contributors worldwide.

{% endblock %}

{% block top_contributors %}
## Top community contributors

Already over 100 people have contributed to to the project with contributions big and small. The top contributors over
    the last 30 days are:

{% endblock top_contributors %}




{% block teammembers %}

## Core team

The core team - employed by Docker, Inc., the company behind Docker. This team not only contributes to the Docker core,
    but also to the tooling around it, website, marketing, support, legal and everything else.


{% endblock teammembers %}
