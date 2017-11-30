
# Title: Time Management

## Team Member(s):
Roger Ho, Tejveer Singh, Yan Xu

# Monte Carlo Simulation Scenario & Purpose:
Help user's simulate total time it takes to finish a project based on individual tasks inputs.

### Hypothesis before running the simulation:
Does the user's initial conjecture of total duration of the project land within a certain Confidence Interval of the simulation.

### Simulation's variables of uncertainty
It depends on the user's input and the distribution of their choice the program provides. (PERT, Normal & Uniform)

## Instructions on how to use the program:
Input the variable names, choose the distribution model for each variable and input the values according to the chosen distribution.
(Brief simple example:
EX.
Simulate the total Process time of going to school.
     Variables: Get out of bed, tie shoelace, Walk to school
     Distribution:  Normal,     uniform,       PERT
     input values: (Mean, SD), (low, high), (Best, most likely, Worst)
)

## Sources Used:
Programming language: Python3
Web Framework: Flask

Delivering visual plots to the web browser in web apps:\n
https://summerofhpc.prace-ri.eu/bringing-visualisation-to-the-web-with-python-and-bokeh/
https://blog.modeanalytics.com/python-interactive-plot-libraries/
https://www.reddit.com/r/Python/comments/21feci/any_good_ways_of_making_charts_in_web_apps/

Flask Usage:\n
https://www.tutorialspoint.com/flask/
https://stackoverflow.com/questions/37754079/python-flask-processing-input-obtained-from-front-end-in-the-back-end
https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
https://pythonspot.com/en/flask-web-app-with-python/
