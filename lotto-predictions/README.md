# 🔹 Description
__Predicting__ the time of __hitting a six__. In addition, we will get the __number of 3, 4 and 5 hits during the simulation__ and the __amount spent on draws__.

## 🔹 Information
The __exact day__ of the simulation __may vary slightly__ because __leap years__ and __days of the week__ on which draws are made __are not taken into account__.

The __simulation__ expects __6 different numbers greater than 0__ and __less than 50__.

## 🔹 Fun fact
The __probability__ of hit __6__ is __1:13 983 816__\
The __probability__ of hit __5__ is __1:54 201__\
The __probability__ of hit __4__ is __1:1 032__\
The __probability__ of hit __3__ is __1:57__

## 🔹 Example excerpt from the terminal
```
WELCOME TO THE LOTTO PREDICTIONS. WE WILL SIMULATE HITTING A SIX IN THE LOTTO.
REMEMBER! YOU CAN ONLY SELECT NUMBERS BETWEEN 1 AND 49, BUT THEY CAN'T REPEAT.

Enter how much money do you want to invest per week: 3
Enter the currency in which you want to invest (You can choose: EUR, USD or PLN): PLN
Enter how many times a week do you want to draw (you can only 1 to 3 times): 2
Enter the 1st number: 26
Enter the 2nd number: 1
Enter the 3rd number: 32
Enter the 4th number: 49
Enter the 5th number: 17
Enter the 6th number: 9

Your numbers: 32, 1, 9, 17, 49, 26
Calculations...

The six fell out after 21493 years and 361 days
You spent 6724548.0 PLN

During the draw:
three was drawn 39372 times
four was drawn 2214 times
five was drawn 44 times
```

## 🔹 Run locally
Clone the project
```bash
  git clone -b lotto-predictions-refactoring https://github.com/BOOMBERT/my-old-refactored-selected-projects.git
```

Go to the project directory
```bash
  cd my-old-refactored-selected-projects/lotto-predictions
```

Start the application
```bash
  python main.py
```
