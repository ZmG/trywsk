{% extends 'community/meetups-organize.html' %}
{% load static %}
{% block title %} Events & Meetups - {% endblock %}
{% block meta-description %}Docker is an open-source project to easily create lightweight, portable, self-sufficient containers from any application. The same container that a developer builds and tests on a laptop can run at scale, in production, on VMs, bare metal, OpenStack clusters, public clouds and more.{% endblock %}
{% block meta-keywords %}Docker, linux containers, lxc, PaaS, dotCloud, introduction, about, how it works{% endblock %}

{% block copy_headline %}
# get involved with the Docker community by creating a Docker Meetup group and Meetup events
{% endblock %}



{% block copy_sidebar %}
{% endblock %}


{% block copy_introduction %}

# Starting a Docker Meetup Group

Anyone interested in Docker can become an active member of the Docker community by becoming co-organizer of a Docker Meetup group.

<img class="float-right" src="{% static 'img/community/meetup-logo.jpg' %}" alt="Meetup logo">
If a Meetup group does not already exist in your area and you are willing to start a new one, the best way to proceed is to contact us so that we can create it for you. We will always agree to create a new Docker Meetup group as long as it makes sense geographically speaking.

If you have already created a Docker Meetup group that is fine, we will simply ask you to add us as a co-organizer so that we can ensure a consistent support to the group in terms of community and Meetup management.

Before contacting us to create a new Docker Meetup Group, take a look at our <a title="Meetup Groups page" href="{% url 'meetups' %}" target="_blank"> Meetup Groups page </a> to make sure a group does not already exist in the area

{% endblock %}


{% block copy_1 %}

## Organizing a Docker Meetup event

Now that you are co-organizer of a Docker Meetup Group, here are a few tips and suggestions to help you get started: 

*	Attend similar DevOps or Developers Meetups to gain experience and gauge interest in Docker
*	Contact other people interested in Docker to help you organize and promote future Meetups
*	Research High-Tech companies in your area willing to host a Docker Meetup event
*	Research what would be the best date(s) to schedule the Meetups based on availabilities with regard to competing events in the area and other calendar imperative
*	Research what are the topic of interest to your audience prior to set an agenda for the meetup
*	Pay attention to the Meetup page aesthetics, add logos and pictures, invite members to leave comments and reply to these comments
*	Promote the event on social media and make sure that the list of keywords is well define if you have created the Docker Meetup Group on your own

## How we can help you

We can support the co-organizers of the Docker Meetup Groups based on their specific needs. For instance, we might / will be able to:

*	Send you Docker T-shirts and stickers
*	Put you in contact with other people interested in being a co-organizer of a Docker Meetup group, and which are in the same area
*	Put you in contact with companies willing to host a Docker Meetup in your area
*	Introduce you to people willing to give a lightning talk about Docker
*	Promote your Docker Group on Docker.io, Docker Weekly and Social Media

<img src="{% static 'img/community/hackday-600px.jpg' %}" alt="Hackday Picture">

## Host a Docker Meetup

### Want to host a Docker Meetup?

We are always looking for new office space to host Docker Meetups. If your company is willing to host a Docker Meetup,
 please contact us by email at meetup@docker.io. Previous Docker Meetups have been hosted by companies such as
 Rackspace, Twitter, MongoDB, BrightCove, DigitlOcean, Viadeo and Edmodo

### How many attendees?

The company hosting the event fixes the number of attendees depending on their office size and availability. This number usually varies between 30 and 200.

### How long is a Docker Meetup?

Once again, each company hosting the event decides when does the meetup start, and how long it lasts. Usual meetups tend to last 2 hours, and start between 4pm and 6pm.

{#<img src="{% static 'img/community/Edmodo.jpg' %}">#}

{% endblock %}

