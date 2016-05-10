{% extends 'homepage.html' %}
{% load static %}

{% block title %}Homepage - {% endblock %}
{% block meta-description %}IBM Containers: A cloud infrastructure to run your Docker containers on IBM Bluemix&trade; {% endblock %}
{% block meta-keywords %}IBM, Docker, linux containers, lxc, PaaS, Bluemix{% endblock %}

{% block copy_headline %}

# A cloud infrastructure to run your Docker containers on IBM Bluemix#

{% endblock %}


{% block copy_introduction %}
IBM® Containers are used to run Docker containers in a hosted cloud environment on IBM Bluemix™. IBM Containers helps you build and deploy containers where you can package your applications and services. Each container is based on an image format, includes a set of standard operations, and is an execution environment in itself.
    Containers are virtual software objects that include all the elements that an application needs to run. 
    Each container includes just the app and its dependencies, running as an isolated process on the host 
    operating system. Therefore, it has the benefits of resource isolation and allocation, but is more 
    portable and efficient. Containers help you build high-quality apps, fast.<span class="read-more"><a href="{% url 'learn_more' %}" title="About IBM Containers">Read more -></a></span>
{% endblock %}


{% block copy_news %}
### Latest updates
{% endblock %}



{% block copy_community %}
### Events & meetups

{% endblock %}


{% block press %}

[<img src="{% static 'img/press-logos/hackernews_logo.png' %}" title="Hacker News, Y-combinator" class="press-img">](https://www.hnsearch.com/search#request/all&q=docker/)
[<img src="{% static 'img/press-logos/linux.com_150.png' %}" title="Linux.com: Docker: A 'Shipping Container' for Linux Code" class="press-img">](http://www.linux.com/news/enterprise/cloud-computing/731454-docker-a-shipping-container-for-linux-code/)
[<img src="{% static 'img/press-logos/techcrunch_wide_150.png' %}" title="Techcrunch" class="press-img">](http://techcrunch.com/2013/07/28/the-matrix-of-hell-and-two-open-source-projects-for-the-emerging-agnostic-cloud/)
[<img src="{% static 'img/press-logos/admin_magazine_150.png' %}" title="Admin Magazine" class="press-img">](http://www.admin-magazine.com/Archive/2013/16)
{% endblock %}

{% block index_introduction %}
{% endblock %}
