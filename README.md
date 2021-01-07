# tau-python-programming

- [Web UI Python Path](https://testautomationu.applitools.com/learningpaths.html?id=web-ui-python-path)  
- [Python Programming with Jess Ingrassellino](https://testautomationu.applitools.com/python-tutorial/)

## Requirements for this course

- Python must be installed 3.8.1 - [Python can be downloaded from here](https://www.python.org/downloads/)
- Pycharm community editon - [Can be downloaded here](https://www.jetbrains.com/pycharm/download/#section=windows)

### Chapter 1 - Variables, Data and Basics

To see the out the file for chapter 1, you can click the play button towards the top right of the vs code window, this will output it in the output window.

To open and close the Terminal you can use the keys `Ctrl + '`

### Chapter 2 - Functions

When writing a function it has to be in this format with the addition() at end of the function

```bash

def addition():
    #Hard coded variables
    a = 10
    b = 30
    print(a + b)

addition()
```

### Chapter 3 Args, Kwargs, *args

This would fail as it is missing a positional arugment.

```bash
def user_info(name, age, city):
    '''This function prints name, age and city
    fron an argument provided to the function'''

    print ("{} is {} years old, from {}".format(name, age, city))

# Uses positional arguments
user_info(58, "Oklahoma City")
```

In the above instance, it gives an error in the output of `TypeError: user_info() missing 1 required positional argument: 'city'`, this is because it has a missing argument.

#### Defaults

You can make use of defaults so that you don't have to define them later on.
`def user_info(name, age=0, city="Tucson"):`

#### Uses default arguements in this scenario

Then when you set user infor using this method, it user then name and passed in the defaults too.
`user_info("Micah")`

#### Using defaults and overriding

Defaults can be overriden, they don't need to be in the same order when overriding.
`user_info(age=56, name="Trevor")`

#### *arg and **kwargs

```bash
*args
Allows for unlimited varaibles to be passed into a function without defining them ahead
of time

def add (*args):
    print(sum(args))
    add(2,3,4)
    add(2,3,4,8,184

**Kwargs 
Allows for unlimited keyword arguments to be passed into a function without defining them ahead 
of time

def applications(**kwargs):
    print(**kwargs)
applications(name = "Jess", email = "mail@mail.com")
application(name = "Susan", surname = "Johnson", age = 42)
```

### Chapter 4 - Conditionals

This code for this chapter can be run in the terminal which I found enables you to provide input to test the code paths.

```bash
- if, elif, else are controll stuctures in python
- if used by itself will only run if certain conditions are present
- elif, runs when pre-conditions are not met, and many conditons might be met
- else, is used to close out if, elif code block, and should cover anything else
```

