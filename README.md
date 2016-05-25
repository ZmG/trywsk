#Setting up the application:
1. Clone trywsk repository to your local machine
2. Navigate to the trywsk folder 
3. Deploy to bluemix: cf push 

#trywsk:
This is the project containing the base page that serves as a catalog for the tutorials/trails. It builds on Django 1.5. This project uses a simplified Django structure, and has the notable feature that all major text contained on this website can be maintained by changing the markdown files contained in /_pages/. There is a good chance this will be the only part you need to touch.

#Dependancies:
1. wsk_tutorial project 

#Deployment:
   `cf push` 
   
#Delete app from bluemix:
   `cf delete learnwhisk`

#wsk_tutorial:
1. Adding steps to trails:
    1. Open the steps.coffee file that is located in wsk_tutorial/static/js directory.
    2. Locate the corresponding queue to which you'd like add a step to. For example, trigger_q holds all the step items for the trigger tutorial. 
    3. Push a new item to the corresponding q. You can reuse the structure from previous steps. Example: trigger_q.push({...})

2. Updating the wsk interpreter: 
    1. Open the terminal.coffee file that is located in the wsk_tutorial/static/js directory.
    2. Adding a new command to the interpreter: 
 		a. Locate "WSK Interpreter" comment block 
 		b. Add a new if clause to the wsk if-else code block and echo to the corresponding variable holding the content for the output.
 	3. Adding content for the output of a command:
 		a. Locate "WSK Content" comment block. 
 		b. Create a new variable holding the output content for the command to be added. 
