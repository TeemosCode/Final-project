
# Final-Project files & Directories & Walkthrough:

We have currently finished three parts of our program for the foundation of our final web program.
But as many of our team members have final exams on 12/15. We could not muster all focus on finishing the web program. Thus, we made sure that our Monte Carlo simulation program works first to meet all requrements of our final project and its due dat of 12/14.
Right now, the three parts that are finished for foundation of our web program is:
- Monte_Carlo_termianlProgram.py  :  Contains the main workflow and function of Monte Carlo Simulation that simulates the Workflow of our web program in the terminal
- FlaskFoundation : The web framework of our web program. It's a loosely built back-bone so that we can easily take apart our Monte_Carlo_termianlProgram.py code to fit in the framwork along with the front end User Interface we created in the 'web' directory.
- web : Contains the User Interface of our web program. It is created in Reactjs. Currently to display and look at our webpage User Interface, it runs on Node.js. There will be an instruction of how to run the express web framework in Node.js in order to view the User Interface.

When finals are over, we will preceed to migrate all functionality into our flask framework to finish our web program.

## File: Monte_Carlo_termianlProgram.py
This is the main Monte Carlo simulation python file. It has been finished to meet all the requirements of our Final Project for the due date of 12/14.

This program is built to simulate the workflow of our Web program in the terminal, including the user interface but in text and along with some logic to simulate that process.

WorkFlow:
	The user would have to first type in at least three names of the Task that makes up a project lifetime linearly in sequence. Each task name would then need to choose its corresponding distribution (1 of the three choices of Normal, PERT and Uniform distribution) and then would need to input the statistical values needed by those distributions.
	After at least three tasks and their information are keyed in, the program would ask if the user wants to run simulation. Press 'r' to run simulation or simply any other keyboard inputs to keep on adding in new tasks, each time being asked by the program if the user would want to run the final simulation.
	To run the simulation, the program would then prompt the user to choose the size of simulation. (Has to be over 5000 or would be set to default value of 100000) Afterwards, the program would again prompt user to input their initial estimation of the total duration of the porject lifetime. Then simulation would run and in a short time the program would plot out the simulation distribution and the user's estimate value as a vertical red line and output all statistical summary and values and assumptions to the standard output for user to look and compare with.
	After closing the plot, the program would ask if use would like to quite the program or to start a whole new simulation process. Type in 'y' to quit program. To restart, simply press Enter, the program would initialize the program the a new starting state. 


## Directories:
web:
	Contains various files of the Node.js environment and express framework to view the Web Page user interface. It serves as a foundation for later migration to flask framework.

	Instructions on how to run the User Interface:
		1. Install dependencies: `cd Final-project`, `cd web`, then `npm install`
		2. Then make sure you have two terminals open; in one, type `npm start` to run the backend, and in the other, type `npm run dev` to run the frontend. 
		3. Open a browser and go to `http://localhost:3000/` to view the page.
		4. Press the button "get started", then go to the main page to add tasks and run Simulation


FlaskFoundation:
	- static (Directory) : This folder contains the testing frontend static files (javascript files) for the flask framework
	- templates (Directory) : This folder contains the testing frontend user interface files (html files) with the flask jinja2 template engine
	- flaskFoundation : A crude layout of the flask framework which would serve as our foundation for the web program.
As time management is a critical aspect of a professional world so we are quite keen on making an application that could simulate any kind of task in linear order so that it could show real-world scenario.

