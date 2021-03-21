pands-problem-sheet
Author: Gillian Kane-McLoughlin

ReadMe file for my GitHub contents for the Programming and Scripting module.

**Contents:**

1) bmi.py - task for Week 2. 

Instructions:  
"Write a program that calculates somebody's Body Mass Index (BMI) Call the file bmi.py -  
The inputs are the person's height in centimetres and weight in kilograms The output  is their weight divided by their height in metres squared." 

Notes:  
The biggest challenge with this problem was understanding how BMI is calculated and what conversions on the units of measurement I needed to use, but I found those answers quite easily.  
I made a change to my first attempt in Week 03 where I limited the result to two decimal places, as per the example provided in Moodle. 

2) secondstring.py - task for Week 3.  

Instructions:  
"Write a program that takes asks a user to input a string and outputs every second letter in reverse order." 

Notes:  
I refered to w3schools to get a better understanding of slicing strings, but had to look further afield to find a solution to this problem. Once I understood you had to set a stride of -2, writing the code was simple.

References:  
https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3  
https://www.w3schools.com/python/gloss_python_string_slice.asp

3) collatz.py - task for Week 4.

Instructions:  
"Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.  
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.  
Have the program end if the current value is one."

Notes:  
On my first attempt, I could not figure out another way of printing the value "1" as the last output of the while loop without adding a final line of code that printed out 1.  
After watching the lectures for Week 5, I reattempted this problem using a list method and felt this worked better for this problem.

4) weekday.py - task for Week 5. 

Instructions:  
"Write a program that outputs whether or not today is a weekday." 

Notes:  
I checked w3schools for help with this problem but needed more examples. I learned that I needed to import python's datetime module, and that days are stored with a number (Monday being 0) and was able to solve the problem from there. 

References:  
https://intellipaat.com/community/5576/how-do-i-get-the-day-of-week-given-a-date-in-python  
https://www.w3schools.com/sql/func_mysql_weekday.asp

5) squareroot.py - task for Week 6. 

Instructions:  
"Write a program that takes a positive floating-point number as input and outputs an approximation of its square root."

Notes:  
This was the most challenging weekly task so far.  
I researched the Newton Method of estimating square roots as suggested and found the below instructions -  
"Newton’s Method: Let N be any number, then the square root of N can be given by the formula:  
root N = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1."  
I then had to take some time to understand the logic, and eventually found a way to solve this problem by setting some acceptable parameters around the approximation and using a while loop and if statement to check the output. 

References:  
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N

6) es.py - task for Week 7. 

Instructions:  
"Write a program that reads in a text file and outputs the number of e's it contains.  
The program should take the filename from an argument on the command line."  

Notes:  
I spent quite a bit of time researching this problem before making an attempt.  
I first had to find out how to read a file name from the command line, and learned I needed to import the sys module to achieve this. I then tried finding the first lower case 'e' in the file I was using (an excerpt from The Hobbit) just to check that I was on the right track.  
Once I had the first position, I researched how I would then find the next 'e' and count the number of results. 
I ended up using the char variable and using this in a for loop which increased the counter every time it found an 'e'. 

References:  
https://realpython.com/python-command-line-arguments/  
https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162  
https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/  
https://www.tutorialspoint.com/python/python_command_line_arguments.htm

7) plottask.py - task for Week 8. 

Instructions:  
"Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.  
Some marks will be given for making the plot look nice."

Notes:  
This task required quite a bit of trial and error. Initially, I made the mistake of trying to plot the three functions all at once. When that didn't work, I thought about plotting one function as a scatter plot, and the other two as line charts, but that looked strange.  
Eventually I plotted the functions one by one and thought this looked best. I then added some colours to distinguish between the different functions and once I was happy with those, I added the labels, title and legend to make it look better.

References:  
https://matplotlib.org/stable/gallery/color/named_colors.html  
https://stackabuse.com/how-to-set-axis-range-xlim-ylim-in-matplotlib/