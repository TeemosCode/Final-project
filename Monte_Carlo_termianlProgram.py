import numpy as np
import bokeh as bk 
import matplotlib.pyplot as plt


class Simulator:

	def __init__(self):
		self.default_dist = mod_pert_random
		self.default_size = 10000

	def normal_distribution(self, mean, standard_deviation, size = 10000):
		normal =np.random.normal(loc=mean, scale=standard_deviation, size=size)
		return normal

	def uniform_distribution(self, min, max, size = 10000):
		uniform =np.random.uniform(min,max, size = size)
		return uniform

	def mod_pert_random(self, low, likely, high, confidence=4, samples=10000):
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

		beta = np.random.beta(a, b, samples = samples)
		beta = beta * (high - low) + low
		return beta

	def final_plotting(self):
		pass


class UI:
	def __init__(self):
		self.varnames = {}
	def menu(self, mode = 1, dist = "2"):
		"""
		Menu input, outputs differ based on modes. 
		mode : {1 : Input tasks (Initialized for start of program), 2 : select Distribution, 3 : Input values}
		dist (distribution) : {"1": Normal Distribution, "2" : PERT Distribution, "3" :Uniform Distribution}
		"""
		def mtprint(title, additionals=''):
			"""Menu title print"""
			print(
			"""
			=================={}===================
			{}\n
			""".format(title, additionals))


		if mode == 1:
			# mtprint("Please Enter more than 2 variable names for simulation (Press 's' to stop input)")
			# varnames = []
			# while len(varnames) <= 2:
			# 	variable = input("Name of variable {}: --> ".format(len(varnames + 1)))
			# 	varnames.append(variable)
			# 	if len(varnames) <= 2:
			# 		print("Please input MORE THAN 2 variables for simulation")
			# 	if variable == 's':
			# 		return varnames
			mtprint("Please Enter variable name for simulation")
			variable = input("Name of variable {}: --> ".format(len(self.varnames + 1)))
			self.varnames[variable] = 0 # set it to zero first, will later save its distribution choice and variable values


		elif mode == 2:
			mtprint("Please Enter your choice of distribution (Default would be PERT)", 
				"1. Normal Distribution\n2. PERT Distribution\n3. Uniform Distribution")
			invalid_input = 0
			choice = input("Choice: --> ")
			while choice not in ['1', '2', '3'] and invalid_input < 3:
				print("NO SUCH CHOICE! Please try again! (We will use the default if you input invalid choice more than 3 times)")
				invalid_input += 1
				choice = input("Choice: --> ")
			return choice

		elif mode == 3:
			dist_values = [] # for holding distribution values 
			if dist == 1: # Normal dist
				mtprint("Please enter Mean and Standard_deviation of Normal Distribution")
				mean = input("Mean : --> ")
				while not mean.isnumeric() and float(mean) > 0:
					print("Invalid mean input, Again!")
					mean = input("Mean : --> ")

				dist_values.append(mean)

				std = input("Standard Deviation : --> ")
				while not std.isnumeric() and float(std) < 0:
					print("Invalid mean input, Again!")
					std = input("Standard Deviation : --> ")

				dist_values.append(std)

			elif dist == 2: # PERT dist
				mtprint("Please enter WORST, MOST LIKELY and BEST case of PERT Distribution")
				worst = input("WORST : --> ")
				while not worst.isnumeric() and float(worst) > 0:
					print("Invalid mean input, Again!")
					worst = input("WORST : --> ")

				dist_values.append(worst)

				likely = input("MOST LIKELY : --> ")
				while not likely.isnumeric() and float(likely) <= worst:
					print("Invalid mean input, Again!")
					likely = input("MOST LIKELY : --> ")

				dist_values.append(likely)

				best = input("BEST LIKELY : --> ")
				while not best.isnumeric() and float(best) <= likely:
					print("Invalid mean input, Again!")
					best = input("BEST LIKELY : --> ")

				dist_values.append(best)

			elif dist == 3: # Uniform dist
				mtprint("Please enter MIN and MAX value of Uniform Distribution")

				Min = input("MIN : --> ")
				while not Min.isnumeric() and float(Min) > 0:
					print("Invalid mean input, Again!")
					Min = input("MIN : --> ")

				dist_values.append(Min)

				Max = input("MAX : --> ")
				while not Max.isnumeric() and float(Max) <= Min:
					print("Invalid mean input, Again!")
					Max = input("MAX : --> ")

				dist_values.append(Max)

			return dist_values


		def run_program(self):
			while True:
				varname_list = self.menu()
				dist_choice = self.menu(mode = 2)
				dist_values_list = self.menu(mode=3, dist=dist_choice)










