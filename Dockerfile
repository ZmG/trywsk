# Dockerfile to (test) build the www.docker.io website
# This dockerfile was created for the docker hackday #6 
# and should (obviously) not be used outside.
# Right is granted to use this file and the website for 
# testing purposes, but copyright is owned by dotcloud.


maintainer Thatcher Peskens

from ubuntu:12.10
 
run apt-get install -y python-setuptools
run easy_install pip
add . /website
run pip install -r /website/requirements.txt
 
expose 8000
 
cmd ["python", "/website/manage.py", "runserver", "0.0.0.0:8000"]
