import numpy as np
import matplotlib.pyplot as plt


def task():
    variables = []
    for i in range(int(input("How may tasks are there in the project? "))):
      variables.append(input("Enter the name of Task in a Project: "))
    Y1=0
    X1=0
    Z1=0
    for i in range(len(variables)):

            print("What kind of distribution you want to simulate for",variables[i],"? ")
            option=let_user_pick(["Normal Distribution", "PERT distribution", "Uniform Distribution"])
            if option==1:
                mean=int(input("Enter the mean: "))
                SD=int(input("Enter the standard deviation: "))
                x=normal_distribution(mean,SD)
                X1=X1+x
            elif option==2:
                best_time = int(input("Enter the best time: "))
                most_likely=int(input("Enter the most likely time: "))
                worst_time=int(input("Enter the worse case time: "))
                y=mod_pert_random(best_time,most_likely,worst_time, confidence=4, samples=10000)
                Y1=Y1+y
            elif option==3:
                min=int(input("Enter the minimum Value: "))
                max=int(input("Enter the maximum valuw: "))
                z=uniform_distribution(min, max)
                Z1=Z1+z


    total=(X1+Y1+Z1)/3
    print(total)
    plt.plot(total)
    plt.show()








def let_user_pick(options):
    print("Please choose:")
    for idx, element in enumerate(options):
        print("{}. {}".format(idx+1,element))
    while True:
        i = input("Enter number: ")
        try:
            if 0 < int(i) <= len(options):
                return int(i)

        except:
            print("Wrong Choice")

    return None

def normal_distribution(mean,standard_deviation):
    normal =np.random.normal(loc=mean, scale=standard_deviation, size=10000)
    return normal



def mod_pert_random(low, likely, high, confidence=4, samples=10000):
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

    beta = np.random.beta(a, b, samples)
    beta = beta * (high - low) + low
    return beta




def uniform_distribution(min,max):

    uniform =np.random.uniform(min,max,10000)
    return uniform


task()