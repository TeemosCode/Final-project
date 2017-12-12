import numpy as np
import bokeh as bk
import pandas as pd
import matplotlib.pyplot as plt


class Simulator:
        def __init__(self):
            """
            Set the default size of simulation equal to 1000 for every variable if user inputs simulation size less than 1000
            :param:
            :return:
            """

            self.total = 0  # this would be an ndarray holding the total simulated time after simulation is finished
            self.default_size = 1000
            self.sim_size = input("=====Enter the numbers of simulation you want for every variable [the more the better, at least over 500 times] \
                            (If input is invalid, it will be the default size '1000')=====")
            if not self.sim_size.isnumeric() or int(self.sim_size) < 500:
                    self.sim_size = self.default_size
            else:
                    self.sim_size = int(self.sim_size)  # coeric it to integer type so it won't create a bug when calling distribution methods

        def final_plotting(self,x_user_estimate):  # Plots out the final simulation to show its distribution with a histogram
            """
            Plot the final result of our simulation
            :param x_user_estimate: This is user estimated time in which user thinks project will be finished
            :return:
            """
            plt.hist(self.total, bins=300, normed=True)
            plt.axvline(x_user_estimate,color="red")  # plot vertical line to represent the value of user's estimation before the simulation
            plt.show()

        def final_statistical_summary(self, user_estimate):
            """
            The function will give the final statisical summary of our similation results like mean , minimum value,maximum,1st quartile,median etc
            It will also caluclate the difference between user estimated and calcukated mean time
            :param user_estimate: This is user estimated time in which user thinks project will be finished
            :return:
            """
            print("\n==========Statistical Results=============")
            pd_series = pd.Series(
                self.total)  # change the ndarray of final simulation total to pandas series for its statistical methods
            print(pd_series.describe())  # print out the statistical summary in the standard output

            # show the difference of user's estimate with mean of simulation
            print('\n---The Difference of your Estimation and the Mean of the Simulation :  {} ---'.format(
                user_estimate - pd_series.mean()))

        def normal_distribution(self, mean, standard_deviation, size=10000):
            """
            The function run simulation on normal distribution
            :return: It will return the random numbers from normal distribution

            :param mean: The mean corresponding to normal distribution
            :param standard_deviation: The standard deviation corresponding to normal distribution
            :param size: The size of simulation
            """
            normal = np.random.normal(loc=mean, scale=standard_deviation, size=size)
            return normal

        def uniform_distribution(self, min, max, size=10000):
            """
            The function run simulation on uniform distribution
            :return: It will return the random numbers from uniform distribution
            :param min: The minimum value corresponding to uniform distribution
            :param max: The maximum value corresponding to uniform distribution
            :param size: The size of simulation
            """
            uniform = np.random.uniform(min, max, size=size)
            return uniform

        def mod_pert_random(self, low, likely, high, confidence=4, size=10000):
            """Produce random numbers according to the 'Modified PERT'
            distribution.
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
        def __init__(self):
            """
            Setting the initial values when the object of this class is created
            """
            self.varnames = {}  # A dictionary containing all information regarding each variable names {"varName" : {"Distribution" : [values]}, }
            self.varResults = {}  # Dictionary containing the result ndarray of each variable names and final total {"varName" : [ndarray], "Total":[ndarray]}
            self.distribution_choices = {"1": "Normal Distribution", "2": "PERT Distribution", "3": "Uniform Distribution"}
            self.user_estimate = 0  # The total time of the project the user themself estimate. They will be prompted to key in their answer near the end of run_program

        def mtprint(self, title, additionals=''):
            """Menu title print"""
            print(
                """
                =================={}===================
                {}\n
                """.format(title, additionals))

        def menu(self, mode=1, dist="2", varname=''):
            """
            Menu input, outputs differ based on modes.
            mode : {1 : Input tasks (Initialized for start of program), 2 : select Distribution, 3 : Input values}
            dist (distribution) : {"1": Normal Distribution, "2" : PERT Distribution, "3" :Uniform Distribution}
            """
            if mode == 1:
                self.mtprint("Please Enter variable name for simulation")
                variable = input("Name of variable {}: --> ".format(len(self.varnames) + 1))
                self.varnames[
                    variable] = {}  # set it to another dictionary where its key would be distributions and list of variable values as value
                return variable  # return the variable name for keeping track of dictionary varnames growth according to that variable name


            elif mode == 2:
                self.mtprint("Please Enter your choice of distribution (Default would be PERT)",
                             "1. Normal Distribution  2. PERT Distribution  3. Uniform Distribution")
                invalid_input = 0
                choice = input("Choice: --> ")
                while choice not in ['1', '2', '3'] and invalid_input < 3:
                    print(
                        "NO SUCH CHOICE! Please try again! (We will use the default if you input invalid choice more than 3 times)")
                    invalid_input += 1
                    choice = input("Choice: --> ")
                if invalid_input == 3:
                    choice = "2"  # set to default PERT distribution
                self.varnames[varname][self.distribution_choices[choice]] = []  # Nested dict value set to empty list
                return choice

            elif mode == 3:
                dist_values = []  # for holding distribution values
                if dist == "1":  # Normal dist
                    self.mtprint("Please enter Mean and Standard_deviation of Normal Distribution (Inte the Same Unit)")
                    mean = input("Mean : --> ")
                    while not mean.isnumeric() and float(mean) > 0:
                        print("Invalid mean input, Again!")
                        mean = input("Mean : --> ")

                    dist_values.append(float(mean))

                    std = input("Standard Deviation : --> ")
                    while not std.isnumeric() and float(std) < 0:
                        print("Invalid mean input, Again!")
                        std = input("Standard Deviation : --> ")

                    dist_values.append(float(std))

                elif dist == "2":  # PERT dist
                    self.mtprint("Please enter WORST, MOST LIKELY and BEST case of PERT Distribution (In the Same Unit)")
                    worst = input("WORST : --> ")
                    while not worst.isnumeric() and float(worst) > 0:
                        print("Invalid mean input, Again!")
                        worst = input("WORST : --> ")

                    dist_values.append(float(worst))

                    likely = input("MOST LIKELY : --> ")
                    while not likely.isnumeric() and float(likely) <= worst:
                        print("Invalid mean input, Again!")
                        likely = input("MOST LIKELY : --> ")

                    dist_values.append(float(likely))

                    best = input("BEST LIKELY : --> ")
                    while not best.isnumeric() and float(best) <= likely:
                        print("Invalid mean input, Again!")
                        best = input("BEST LIKELY : --> ")

                    dist_values.append(float(best))

                elif dist == "3":  # Uniform dist
                    self.mtprint("Please enter MIN and MAX value of Uniform Distribution (In the Same Unit)")

                    Min = input("MIN : --> ")
                    while not Min.isnumeric() and float(Min) > 0:
                        print("Invalid mean input, Again!")
                        Min = input("MIN : --> ")

                    dist_values.append(float(Min))

                    Max = input("MAX : --> ")
                    while not Max.isnumeric() and float(Max) <= Min:
                        print("Invalid mean input, Again!")
                        Max = input("MAX : --> ")

                    dist_values.append(float(Max))

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
            :return:
            """
            simulator = Simulator()  # create the object instance of Simulator
            first_count = 0  # for ease of initializing a variable to add up the rest of the calculated ndarray results
            simulated = 0
            for var_name in self.varnames:

                if list(self.varnames[var_name].keys())[0] == "Normal Distribution":
                    simulated = simulator.normal_distribution(self.varnames[var_name]["Normal Distribution"][0],
                                                              self.varnames[var_name]["Normal Distribution"][1],
                                                              size=simulator.sim_size)  # simulate and return ndarray
                    self.varResults[var_name] = simulated
                    print(self.varResults[var_name])
                    print("========IN NORMAL DIST======")

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
                # Calculate total simulation time
                if first_count == 0:
                    total = simulated
                    first_count += 1
                else:
                    total += simulated

            self.varResults["Total"] = total
            print(self.varnames)
            print(self.varResults)
            print(total)
            simulator.total = total
            simulator.final_plotting(self.user_estimate)  # plot out the result
            simulator.final_statistical_summary(self.user_estimate)  # print out the statistical summary

        def user_estimates(self):
            """
            The function used for taking input from the user for estimated total outcome of the program
            :return:
            """
            self.mtprint("What is you're estimated outcome of total time for your project duration??")
            estimate = input(":--> ")
            while not estimate.isnumeric():
                print("Invalid input. Please type in numbers!")
                estimate = input(":--> ")
            self.user_estimate = int(estimate)  # save the user estimate value to instance variable user_estimate

        def run_program(self):

            quit = False  # flag for keeping track if user wants to end program or not
            while True and not quit:
                varname = self.menu()
                dist_choice = self.menu(mode=2, varname=varname)
                dist_values_list = self.menu(mode=3, dist=dist_choice, varname=varname)

                if len(
                        self.varnames) > 2:  # if there are more than two variables prompt user to choose to run simulation or not
                    self.mtprint(
                        "Would you like to run Simulation? (Press 'r' to run simulation, else keep adding in variables)")
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







