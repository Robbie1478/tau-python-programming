def user_info(name, age, city):
    '''This function prints name, age and city
    fron an argument provided to the function'''

    print ("{} is {} years old, from {}".format(name, age, city))

# Uses positional arguments
user_info("Janet", 58, "Oklahoma City")

# user_info(58, "Oklahoma City")

#This makes use of default arguments
def user_info(name, age=0, city="Tucson"):
    
    print("{} is {} years old, from {}".format(name, age, city))


# Uses default arguements in this scenario
user_info("Micah")

# Defaults can be overridden in the below example, note, they don't necessarilly need to be in the same order when using default overrides. 
user_info(age=56, name="Trevor")

#*arg - Allows the function to take any number of positional arguements

#**kwargs - Key word arguments - Allows the function to take any number of positional keyword 


# Uses default arguements in this scenario
user_info("Robert")
# Defaults can be overridden in the below example
user_info(age=56, name="Trevor")

# *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. The email address is {}, her salary is {} {} and hire date is {hire_date} adding additional {kwargs}.".format(fname, lname, company, email, *args, **kwargs))


application("Jess", "Ingrass", "mail@mail.com", "TeachCode.org", 75000, "adding additional *args", hire_date ="September 2010", kwargs="kwargs")
