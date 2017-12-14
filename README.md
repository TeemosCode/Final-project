
# Title: Time Management

## Team Member(s):
Roger Ho, Tejveer Singh, Yan Xu

# Monte Carlo Simulation Scenario & Purpose:
As time management is a critical aspect of a professional world so we are quite keen on making an application that could simulate any kind of task in linear order so that it could show real-world scenario.

In hopes of learning something new and applying all the python programming, soft skills and concepts regarding software engineering and development we learned this semester through this final project, we wanted to create a program that would be different than our usual assignments that can have a user interface to interact with users and could also be displayed to show our work, thus we came up with an idea to try learn full stack development and create a application in python based on a MonteCarlo scenario as our topic. To be more creative, our program is not about simulating any certain datasets or situation for the sake of analysis. We wanted to be more general, to use one certain Monte Carlo simulation scenario to simulation different kind of data judging on the inputs of users.


### Hypothesis before running the simulation:
Does the user's initial conjecture of total duration of the project land within a certain Confidence Interval of the simulation.

### Simulation's variables of uncertainty
It depends on the user's input and the distribution of their choice the program provides. (PERT, Normal & Uniform)

# Instructions on how to use the program:
Input the variable names, choose the distribution model for each variable and input the values according to the chosen distribution.
- (Brief simple example:
- EX.
- Simulate the total Process time of going to school.
     - Variables: Get out of bed, tie shoelace, Walk to school
     - Distribution:  Normal,     uniform,       PERT
     - input values: (Mean, SD), (low, high), (Best, most likely, Worst)
- )

#### Terminal Program:
- First the program would prompt users to input Task names, then it would prompt the users to enter the choice of the task distribution ( choosing between 1[Normal Distribution], 2[PERT Distribution] and 3[Uniform] ), if users' input is invalid over 3 times, the program would set the default distribution to PERT distribution for that task. Lastly, the program would prompt users to input the statistical values corresponding with the distribution.
- Then the above process would be repeated at least three times before the program prompts user if they want to run the simulation or not. If user does not choose to run the simulation yet, the program would keep repeating the above process to keep adding in more tasks and its information until the user chooses to run the simulation.
- When the user wants to run the simulation, the program would prompt user to input their estimated duration of unit time of the whole project process, then simulation would run and output a plot of the final simulation with user's estimate as a vertical red line for clear visualization of their estimation in the simulation.
- After closing off the plot, the program would display the statistical summary of the simulation, and further prompt the user if they want to keep using the simulation to resimulate a different project.

#### Web Program (Under Construction):
- Intuitive and neat looking user interface for user's to click, choose and typein the task names, distribution and statistical values to run the simulation and generate output plots and statistical summary on the webpage.

## Sources Used:
- Programming language: Python3
- Web Framework: Flask
- Frontend language: HTML, CSS, Javascript

Delivering visual plots to the web browser in web apps:
- https://summerofhpc.prace-ri.eu/bringing-visualisation-to-the-web-with-python-and-bokeh/
- https://blog.modeanalytics.com/python-interactive-plot-libraries/
- https://www.reddit.com/r/Python/comments/21feci/any_good_ways_of_making_charts_in_web_apps/

Flask Usage:
- https://www.tutorialspoint.com/flask/
- https://stackoverflow.com/questions/37754079/python-flask-processing-input-obtained-from-front-end-in-the-back-end
- https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
- https://pythonspot.com/en/flask-web-app-with-python/

Frontend based on: React.js

Frontend codes based on(Changes has been made in file "frontend"):
- https://github.com/bluedrops/passport_demo

Frontend UI design:
- Semantic UI React: https://react.semantic-ui.com/introduction

## To start the web:
1. Install dependencies: `cd Final-project`, `cd web`, then `npm install`
2. Then make sure you have two terminals open; in one, type `npm start` to run the backend, and in the other, type `npm run dev` to run the frontend. 
3. Open a browser and go to `http://localhost:3000/` to view the page.
4. Press the button "get started", then go to the main page to add tasks and run simulation

##### Web framework(flask):
We have currently finished the backend program of the Monte Carlo Simulation as well as the web User Interface. All we need now is to combine them together to form a working web framework. However, with our current situation (Finals creeping up on us), we are still trying and working on migrating code and combining front-end(React) and back-end(flask)
