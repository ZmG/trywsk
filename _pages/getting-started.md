{% extends 'getting-started.html' %}
{% load static %}
{% block meta-description %} OpenWhisk, an IBM product. &trade; {% endblock %}
{% block meta-keywords %}IBM, OpenWhisk, Installation{% endblock %}
{% block title %}Getting Started - {% endblock %}


{% block copy_introduction %}

# Start using OpenWhisk
We try to make using OpenWhisk easy.

{% endblock %}

{% block copy_interactive_tutorial %}
<h2 id="tutSectionHeader" style="padding-top: 14px;"> <a id="h_tutorial"></a>Interactive commandline tutorials</h2>

The best way to learn how OpenWhisk works is to use it!

This hands-on tutorial is 100% online, so you don't need to install a thing. In about 20-25 minutes you'll be familiar with the basic OpenWhisk commands.
<div id="interactive">
    {% include 'tutorial/snippet.html' %}
</div>

<div id="tutorialLinks">
    <div id="basic">
        <center><h3>wsk Actions(JavaScript) Tutorial</h3></center>
        <div class="row tuts" >
            <div class="span6">
                <img id="titleLogo" src="{% static 'img/blueTut.png' %}" alt="wsk tutorial">
            </div>

            <div class="span6">
                <h4>Learn the first steps of using the wsk CLI, such as:</h4>
                <ul>
                    <li>Create an action</li>
                    <li>Invoke a blocking action</li>
                    <li>Invoke a non-blocking action</li> 
                    <li>Get result of a non-blocking action</li>
                </ul>
                <a class="btn btn-primary secondary-action-button" onclick="switchToBasic(); goFullScreen(0);">Start the Actions tutorial.</a>
            </div>
        </div>
    </div>

    <div id="advanced">
        <center><h3>wsk Actions(JavaScript) Advanced Tutorial</h3></center>
        <div class="row tuts" >
            <div class="span6">
                <img id="titleLogo" src="{% static 'img/redTut.png' %}" alt="wsk tutorial">
            </div>

            <div class="span6">
                <h4>Learn the steps of using the wsk CLI, such as:</h4>
                <ul>
                    <li>Create chain of actions</li>
                </ul>
                <a class="btn btn-primary secondary-action-button" onclick="switchToAdvanced(); goFullScreen(0);">Start the Actions Advanced tutorial.</a>
            </div>
        </div>
    </div>

    <div id="triggers">
        <center><h3>wsk Triggers Tutorial</h3></center>

        <div class="row tuts">
            
            <div class="span6">
                <h4>Learn to use triggers</h4>
                <ul>
                    <li>Create a trigger</li>
                </ul>
                <a class="btn btn-primary secondary-action-button" onclick="switchToTriggers(); goFullScreen(0);"> Start the Triggers tutorial</a>
            </div>
            <div class="span6">
                <img id="titleLogo" src="{% static 'img/blueTut.png' %}" alt="Triggers Tutorial">
            </div>
        </div>
    </div>

    <div id="rules">
        <center><h3>wsk Rules Tutorial</h3></center>

        <div class="row tuts">
            <div class="span6">
                <img id="titleLogo" src="{% static 'img/blueTut.png' %}" alt="wsk tutorial">
            </div>
            <div class="span6">
                <h4>Learn to use rules</h4>
                <ul>
                    <li>Create a rule</li>
                </ul>
                <a class="btn btn-primary secondary-action-button" onclick="switchToRules(); goFullScreen(0);"> Start the Rules tutorial</a>
            </div>
        </div>
    </div>

    <div id="packages">
        <center><h3>wsk Packages Tutorial</h3></center>

        <div class="row tuts">
            
            <div class="span6">
                <h4>Learn to use packages</h4>
                <ul>
                    <li>Create a packages</li>
                </ul>
                <a class="btn btn-primary secondary-action-button" onclick="switchToPackages(); goFullScreen(0);"> Start the Packages tutorial</a>
            </div>
            <div class="span6">
                <img id="titleLogo" src="{% static 'img/blueTut.png' %}" alt="Packages Tutorial">
            </div>
        </div>
    </div>

    <div id="mobilesdk">
        <center><h3>wsk Mobile SDK Tutorial</h3></center>

        <div class="row tuts">
            
            <div class="span6">
                <img id="titleLogo" src="{% static 'img/blueTut.png' %}" alt="wsk tutorial">
            </div>
            <div class="span6">
                <h4>Learn to use Mobile SDK</h4>
                <ul>
                    <li>Mobile SDK Placeholder</li>
                </ul>
                <a class="btn btn-primary secondary-action-button" onclick="switchToMobileSDK(); goFullScreen(0);"> Start the Mobile SDK tutorial</a>
            </div>
        </div>
    </div>
</div>
<hr>
{% endblock %}

{% block dockerfile_tutorial %}
<!--
## <a id="h_dockerfile_tutorial"></a>Dockerfile Tutorial

Dockerfiles provide a simple syntax for building images and they are a great way to automate and script the images creation. If you are really serious about Docker, you should master the Dockerfile syntax.

<a href="/learn/dockerfile" class="btn btn-primary secondary-action-button">Start the Dockerfile Tutorial.</a>
-->
<hr>
{% endblock %}

{% block copy_hello_world %}
## Run 'hello world'

Now let's do some magic! Try these commands out in the interactive tutorials.

    ice --local run ubuntu /bin/echo hello world

This should output 'hello world'. Just one line? Yes, but a lot has happened..

Docker did all of the following

* It downloaded the base image from the [docker index](https://index.docker.io)
* it created a new LXC container
* It allocated a filesystem for it
* Mounted a read-write layer
* Allocated a network interface
* Setup an IP for it, with network address translation
* And then executed a process in there
* Captured its output and printed it to you

#### Run an interactive shell

You can also run an interactive shell session inside the container

    docker run -i -t ubuntu /bin/bash

This command creates an interactive shell in a minimal ubuntu container. You will be able to use this shell just like
    you would any other linux machine or virtual machine. Press Ctrl-D to exit the shell.

{% endblock %}

{% block copy_user_guides %}

## What can you build?

Here's a small sample of things being done with IBM Containers.

* #### [TBD](http://www.example.com/)
    Lorem Impsum squared.

* #### [More TBD](http://www.example.com)
    Art of the possible is food for thought.


{% endblock %}
