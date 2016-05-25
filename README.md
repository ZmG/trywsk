#Setting up the application:
1. Clone trywsk repository to your local machine
2. Navigate to the trywsk folder 
3. Deploy to bluemix: cf push 

#trywsk:
This is the project containing the base page that serves as a catalog for the tutorials/trails. It builds on Django 1.5. This project uses a simplified Django structure, and has the notable feature that all major text contained on this website can be maintained by changing the markdown files contained in /_pages/. There is a good chance this will be the only part you need to touch.

#Dependencies:
Dependencies are listed in the requirements.txt file. One of the most important dependencies is the wsk_tutorial project which contains the wsk interpreter logic.
1. wsk_tutorial project 

#Deployment:
   `cf push` 
   
#Delete app from bluemix:
   `cf delete learnwhisk`
   
#Adding Tutorial/Trails links
1. Locate getting-started.md in the _pages directory(i.e. trywsk/_pages/getting_started.md)
2. Add a new div tag to the tutorial links div
