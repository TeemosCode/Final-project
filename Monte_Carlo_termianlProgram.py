import numpy as np
import bokeh as bk
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
import math


class Simulator:
    """
    The Simulator class consists of methods and instance values that are used to take in, varify user estimate value and use different
    distribution methods to generate the Monte Carlo simulation based on the values obtained by the UI class instances.
    Methods:
        final_plotting: Plot out final simulation plt to standard oupput.
        final_statistical_summary: Generate and output statistical summary in pandas to the standard output.
        normal_distribution: Simulation based on Normal distribution
        uniform_distribution: Simulation based on Uniform distribution
        mod_pert_random: Simulation based on PERT distribution
    """

    def __init__(self):
        """
        Set the default size of simulation equal to 100000 for every variable if user inputs simulation size less than 5--
        :param:
        """
        self.total = 0  # this would be an ndarray holding the total simulated time after simulation is finished
        self.default_size = 100000
        self.sim_size = input("=====Enter the numbers of simulation you want for every variable [the more the better, at least over 500 times] (If input is invalid, it will be the default size '100000')=====")
        
        if not self.sim_size.isnumeric() or int(self.sim_size) < 500:
            self.sim_size = self.default_size
        else:
            self.sim_size = int(
                self.sim_size)  # coeric it to integer type so it won't create a bug when calling distribution methods

    def final_plotting(self,x_user_estimate: int):  # Plots out the final simulation to show its distribution with a histogram
        """
        Plot the final result of our simulation
        :param x_user_estimate: This is user estimated time in which user thinks project will be finished
        """
        fig = plt.figure()
        pd_series = pd.Series(self.total)
        plt.hist(self.total, bins=300, normed=True,label=pd_series.describe())
        fig.suptitle('Monte_Carlo_Simulation', fontsize=20)
        plt.xlabel('Time Duration ->', fontsize=18)
        plt.ylabel('Probabilities ->', fontsize=16)
        plt.axvline(x_user_estimate,color="red")  # plot vertical line to represent the value of user's estimation before the simulation
        plt.show()

    def final_box_plotting(self):
        """
        Plot the final result of our simulation (Box Plot)
        :param:
        """
        pd_series = pd.Series(self.total)
        box = plt.boxplot(pd_series, showmeans=True)
        plt.setp(box['boxes'][0], color='green')
        plt.setp(box['caps'][0], color='green')
        plt.setp(box['whiskers'][0], color='green')
        plt.grid(True, axis='y')  # let's add a grid on y-axis
        plt.title('Monte_carlo_Statistics', fontsize=30)  # chart title
        plt.ylabel('Time Duration')  # y axis title
        plt.xticks([1], ['Box Plot'])
        plt.show()

    def final_statistical_summary(self, user_estimate: int):
        """
        The function will give the final statisical summary of our similation results like mean , minimum value,maximum,1st quartile,median etc
        It will also caluclate the difference between user estimated and calcukated mean time
        :param user_estimate: This is user estimated time in which user thinks project will be finished
        """
        print("\n---\n==========Statistical Results=============---\n")
        pd_series = pd.Series(self.total)  # change the ndarray of final simulation total to pandas series for its statistical methods
        print(pd_series.describe())  # print out the statistical summary in the standard output
        # show the difference of user's estimate with mean of simulation
        print('\n---The Difference of your Estimation and the Mean of the Simulation :  {} ---'.format(user_estimate - pd_series.mean()))


        size, min_max, sim_mean, variance, skew, kurt = stats.describe(self.total) # calculating the statistical summary
        # print out another form of statistical summary in scipy
        print("---Statistical Results (More info)---")
        print(stats.describe(self.total))

        # Calculate statistical values
        std = math.sqrt(variance) # standard deviation
        z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
        pop_stdev = self.total.std()  # Get the population standard deviation
        margin_of_error = z_critical * (pop_stdev/math.sqrt(len(self.total)))
        CI = (sim_mean - margin_of_error,
                       sim_mean + margin_of_error)


        print("\n======\nConfidence Interval Range (Here we assume its in Normal distribution) of 95% is: '[{} ~ {}]'\n======= ".format(CI[0], CI[1]))
        if user_estimate < CI[1] and user_estimate > CI[0]:
            print("---Your Estimate '{}' is BETWEEN 95% confidence interval of the simulation".format(user_estimate))
        elif user_estimate > CI[1]:
            print("---Your Estimate '{}' is LARGER than 97.5% of the simulation values".format(user_estimate))
        else:
            print("---Your Estimate '{}' is SMALLER than 2.5% of the simulation values".format(user_estimate))

    def normal_distribution(self, mean: int, standard_deviation: int, size=10000):
        """
        The function run simulation on normal distribution
        :param mean: The mean corresponding to normal distribution
        :param standard_deviation: The standard deviation corresponding to normal distribution
        :param size: The size of simulation
        :return normal: It will return the random numbers from normal distribution of ndarray data structure
        """
        normal = np.random.normal(loc=mean, scale=standard_deviation, size=size)

        return normal

    def uniform_distribution(self, min: int, max: int, size=10000):
        """
        The function run simulation on uniform distribution
        :param min: The minimum value corresponding to uniform distribution
        :param max: The maximum value corresponding to uniform distribution
        :param size: The size of simulation
        :return uniform: It will return the random numbers from uniform distribution of ndarray data structure
        """

        uniform = np.random.uniform(min, max, size=size)

        return uniform

    def mod_pert_random(self, low: int, likely: int, high: int, confidence=4, size=10000):
        """Produce random numbers according to the 'Modified PERT' distribution.
        :param low: The lowest value expected as possible.
        :param likely: The 'most likely' value, statistically, the mode.
        :param high: The highest value expected as possible.
        :param confidence: This is typically called 'lambda' in literature
        about the Modified PERT distribution. The value
        4 here matches the standard PERT curve. Higher
        values indicate higher confidence in the mode.
        Formulas from "Modified Pert Simulation" by Paulo Buchsbaum.
        """

        # Check minimum & maximum confidence levels to allow:
        confidence = min(8, confidence)
        confidence = max(2, confidence)

        mean = (low + confidence * likely + high) / (confidence + 2)

        a = (mean - low) / (high - low) * (confidence + 2)
        b = ((confidence + 1) * high - low - confidence * likely) / (high - low)

        beta = np.random.beta(a, b, size)
        beta = beta * (high - low) + low
        return beta


class UI:
    """
    User Interface class. Contains instance variables that obtains user input information on the task(variable) names, corresponding distribution,
    and number of times for the simulation. Also contains methods that control the whole program flow to simulate the actual Webpage User Interface
    on the terminal.
    Methods:
        mtprint: Pretty printing of titles or prompts
        menu: Controls and displays the terminal topic, prompts and context based on different mode, task and distribution (Simulate the Webpage User Interface)
        initialize: Intializes instance variable values to initial condition when user chooses to rerun the simulation program.
        run_simulation: Runs the simulation based on all user inputs
        user_estimates: Get the user's estimation of final project process time before showing the program's simulation output and plot the user's extimate as a red vertical line on the plot for easy comparison visualization
        run_program: Main method that evokes and controls the process of the program
    >>> test=UI()
    >>> test.menu(mode=abd, dist="2", varname='')
    Traceback (most recent call last):
    ...
    NameError: name 'abd' is not defined

    """


    def __init__(self):
        """
        Setting the initial values when the object of this class is created
        """
        self.varnames = {}  # A dictionary containing all information regarding each variable names {"varName" : {"Distribution" : [values]}, }
        self.varResults = {}  # Dictionary containing the result ndarray of each variable names and final total {"varName" : [ndarray], "Total":[ndarray]}
        self.distribution_choices = {"1": "Normal Distribution", "2": "PERT Distribution", "3": "Uniform Distribution"}
        self.user_estimate = 0  # The total time of the project the user themself's estimate. They will be prompted to key in their answer near the end of run_program


    def mtprint(self, title: str, additionals=''):
        """Menu title print layout"""
        print(
            """
            =================={}===================
            {}\n
            """.format(title, additionals))

    # Define a validation method that returns boolean based on user's input
    def validInput(self, user_input: str, comparator: float) -> bool:
        """
        Validation function. Returns True if user input is numeric that could be converted to float without generating exception:
        "ValueError: could not convert string to float" and if could be converted to float, its value would have to be smaller than
        the comparator, this ensures that user's inputs (which would be used as various statistical values for different distributions)
        are valid and in the appropriate value order.

        Returns False if otherwise. When there is "ValueError", this function prevents program from crashing and instead returns False
        to keep program running for the while loop that would constantly take user's inputs and check them with this function to ensure
        the flow of the program does not break.

        :param user_input: A previously user prompted input of statistical value
        :param comparator: A number for comparison of user's input value
        :return boolean: True or False based on the input
        """
        try:
            if float(user_input) > comparator:
                return True
            else:
                return False
        except:
            return False

    def menu(self, mode=1, dist="2", varname=''):
        """
        Menu input, outputs differ based on modes.
        mode : {1 : Input tasks (Initialized for start of program), 2 : select Distribution, 3 : Input values}
        dist (distribution) : {"1": Normal Distribution, "2" : PERT Distribution, "3" :Uniform Distribution}
        """
        if mode == 1:
            self.mtprint("Please Enter Task name for simulation")
            variable = input("Name of Task {}: --> ".format(len(self.varnames) + 1))
            # set self.varnames' value to another dictionary where its key would be distributions and list of variable values as value
            self.varnames[variable] = {}  
            return variable  # return the variable name for keeping track of dictionary varnames growth according to that variable name


        elif mode == 2:
            self.mtprint("Please Enter your choice of distribution (Default would be PERT)",
                         "1. Normal Distribution  2. PERT Distribution  3. Uniform Distribution")
            invalid_input = 1  # counter for controlling how many times user can have invalid inputs before using program default value
            choice = input("Choice: --> ")
            while choice not in ['1', '2', '3'] and invalid_input < 3:
                print(
                    "NO SUCH CHOICE! Please type 1 or 2 or 3! (We will use the default if you input invalid choice more than 3 times)")
                invalid_input += 1
                choice = input("Choice: --> ")
            if invalid_input == 3:
                choice = "2"  # set to default PERT distribution
            self.varnames[varname][self.distribution_choices[choice]] = []  # Nested dict value set to empty list
            return choice

        elif mode == 3:
            dist_values = []  # for holding distribution values
            if dist == "1":  # Normal dist
                self.mtprint("Please enter Mean and Standard_deviation of Normal Distribution (In the Same Unit)")
                mean = input("Mean : --> ")

                while not self.validInput(mean, 0): # validate user input
                    print("Invalid mean input. Please type in a numeric number that is larger than 0!")
                    mean = input("Mean : --> ")
                
                mean = float(mean)
                dist_values.append(mean)

                std = input("Standard Deviation : --> ")
                while not self.validInput(std, 0): # validate user input
                    print("Invalid mean input. Please type in a numeric number that is larger than 0!")
                    std = input("Standard Deviation : --> ")

                std = float(std)
                dist_values.append(std)

            elif dist == "2":  # PERT dist
                self.mtprint("Please enter BEST, MOST LIKELY and WORST case of PERT Distribution (In the Same Unit)")

                best = input("BEST case : --> ")
                while not self.validInput(best, 0): # validate user input
                    print("Invalid mean input. Please type in a numeric number that is larger than 0!!")
                    best = input("BEST case : --> ")

                best = float(best)
               

                likely = input("MOST LIKELY : --> ")
                while not self.validInput(likely, best): # validate user input
                    print("Invalid mean input. Please type in a numeric number that is larger than BEST case!")
                    likely = input("MOST LIKELY : --> ")

                likely = float(likely)
                

                worst = input("WORST case: --> ")
                while not self.validInput(worst, likely): # validate user input
                    print("Invalid mean input. Please type in a numeric number that is larger than WORST case!")
                    worst = input("WORST case: --> ")

                worst = float(worst)

                # Append it in order
                dist_values.append(best)
                dist_values.append(likely)
                dist_values.append(worst)


            elif dist == "3":  # Uniform dist
                self.mtprint("Please enter MIN and MAX value of Uniform Distribution (In the Same Unit)")

                Min = input("MIN : --> ")
                while not self.validInput(Min, 0): # validate user input
                    print("Invalid mean input. Please type in a numeric number that is larger than 0!")
                    Min = input("MIN : --> ")

                Min = float(Min)
                dist_values.append(Min)

                Max = input("MAX : --> ")
                while not self.validInput(Max, Min): # validate user input
                    print("Invalid mean input. Please type in a numeric number that is larger than Min!")
                    Max = input("MAX : --> ")

                Max = float(Max)
                dist_values.append(Max)

            # set nested distribution dictionary value to dist_values
            self.varnames[varname][self.distribution_choices[dist]] = dist_values


    def initialize(self):
        """
        Used to initialize all instance values of the UI class if users want to rerun the program without restarting the program
        """
        self.varnames = {}  # A dictionary containing all information regarding each variable names {"varName" : {"Distribution" : [values]}, }
        self.varResults = {}  # Dictionary containing the result ndarray of each variable names and final total {"varName" : [ndarray], "Total":[ndarray]}


    def run_simulation(self):
        """
        The function will run the simulation and will be calling the other useful functions created aboce this class for final plotting of the results
        """
        simulator = Simulator()  # create the object instance of Simulator class
        first_count = 0  # for ease of initializing a variable to add up the rest of the calculated ndarray results
        simulated = 0
        for var_name in self.varnames:

            if list(self.varnames[var_name].keys())[0] == "Normal Distribution":
                simulated = simulator.normal_distribution(self.varnames[var_name]["Normal Distribution"][0],
                                                          self.varnames[var_name]["Normal Distribution"][1],
                                                          size=simulator.sim_size)  # simulate and return ndarray
                self.varResults[var_name] = simulated


            elif list(self.varnames[var_name].keys())[0] == "PERT Distribution":
                simulated = simulator.mod_pert_random(self.varnames[var_name]["PERT Distribution"][0],
                                                      self.varnames[var_name]["PERT Distribution"][1],
                                                      self.varnames[var_name]["PERT Distribution"][2],
                                                      size=simulator.sim_size)  # simulate and return ndarray
                self.varResults[var_name] = simulated

            elif list(self.varnames[var_name].keys())[0] == "Uniform Distribution":
                simulated = simulator.uniform_distribution(self.varnames[var_name]["Uniform Distribution"][0],
                                                           self.varnames[var_name]["Uniform Distribution"][1],
                                                           size=simulator.sim_size)  # simulate and return ndarray
                self.varResults[var_name] = simulated

            # Calculation of total simulation time
            if first_count == 0:
                total = simulated
                first_count += 1
            else:
                total += simulated

        self.varResults["Total"] = total

        simulator.total = total
        simulator.final_statistical_summary(self.user_estimate)  # print out the statistical summary
        simulator.final_plotting(self.user_estimate)  # plot out the result
        simulator.final_box_plotting()


    def user_estimates(self):
        """
        The function used for taking input from the user for estimated total outcome of the program
        """
        self.mtprint("What is you're estimated outcome of total time for your project duration?? (It would be displayed as a RED Vertical line in the simulation plot)")
        estimate = input(":--> ")
        while not self.validInput(estimate, 0):
            print("Invalid input. Please type in numbers larger than 0!")
            estimate = input(":--> ")
        self.user_estimate = float(estimate)  # save the user estimate value to instance variable user_estimate


    def run_program(self):
        """
        The starting engine of the simulation terminal program
        """
        quit = False  # flag for keeping track if user wants to end program or not
        while True and not quit:
            # Three consecutive calls of menu with differenct modes that changes displays and takes in different inputs based on user's interaction
            varname = self.menu()
            dist_choice = self.menu(mode=2, varname=varname)
            dist_values_list = self.menu(mode=3, dist=dist_choice, varname=varname)

            if len(self.varnames) > 2:  # if there are more than two variables prompt user to choose to run simulation or not
                self.mtprint("Would you like to run Simulation? (Press 'r' to run simulation, else keep adding in variables)")
                simu_answer = input("Answer : --> ")
                if simu_answer == "r":
                    # If user wants to run simulation, first let them enter their estimate value
                    self.user_estimates()
                    print("Running Simulation....\n....\n....")

                    self.run_simulation()  # Run simulation
                    # After simulation is done and statistical outputs are shown, prompt if user wants to continue or not
                    self.mtprint("Do you want to exit the program? (Press 'y' to quit, else program restarts)")
                    quit_answer = input("Answer : --> ")
                    if quit_answer == 'y':
                        quit = True  # set flag to quit program
                    else:
                        self.initialize()  # initialize all dictionarys back to empty start state
                        self.mtprint("program RESTART!", "Initializing .....")


if __name__ == "__main__":
    userInterface = UI()
    userInterface.run_program()
