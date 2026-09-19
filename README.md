# POV: If you see this repo, you remember my stupidity in python coding.

## An overview about myself
I'm a physics student. When I was at middle school, I won on many physics olympiad in Indonesia. 
Also, I have learned Python programming since I was at middle school. 
Now, I have published more than 10 repositories on my first GitHub account @jovan-AIcoder (link: https://github.com/jovan-AIcoder). Two of them are python packages (for signal analysis using Neural Network), they are lived on PyPI.
All repositories are AI TensorFlow projects for science, especially physics.

## The story behind
On 16th of September, 2026, I was on the Computational Thinking lecture class on my university. 
The lecturer taught the course about the fundamentals of python programming and computational thinking.
At first, everything is alright, I could understand the code given by the lecturer, which was about the implementation of Python code in many problems.
But, that happiness did not last long. The lecturer give me (and all participants in the class) a quiz. In that quiz, we must make a Python program (or a pseudocode) to show a Pascal triangle in bottom right-angled triangle (`number_1a.py`), upper right-angled triangle (`number_1b.py`), isosceles triangle (`number_1c.py`), and inverted isosceles triangle (`number_1d.py`). 
Also, we must make another Python programs to show the Pascal triangle in the forms of lower triangular matrix (`number_2a.py`) and upper triangular matrix (`number_2b.py`).
I thought that all of them were easy to code. But the lecturer said,

**"Do not import other libraries. If you use arrays, do not use `append()`, `pop()`, `clear()`, `split()`, `join()` and so on. Do not use `abs()`, `max()`, `min()`, or other built-in mathematical functions"**

Also, we must make all of that Python code in approximately 30 minutes! What a pressure! When I make a Python code for my repo, I always import another libraries and use functions for array modification! Okay, I made the first one, because it was easy to code and implement the loopings. I thought it was easy, but I experienced several moments of debungging, because the triangle did not appear properly. Okay, python code 1a is finished. Because the useful functions for array was prohibited, I made it without usage of arrays.
I always use `append()` for adding elements into a stack or `pop()` to remove the elements one by one, but that time, I could not use it.
When I made the second code, I was VERY CONFUSED! Because the lecturer says, "You can use arrays, but all of useful built-in functions are prohibited."
So I was trapped on confusion, infinite loop of debugging, and the time was up!
I haven't finished all of code, and I WAS FAILED! 
And after the class,

> **I think I'm a stupid Python coder. I always import useful libraries, but I can't code without library! I have made more than 10 GitHub repositories and 2 PyPI packages, but I can't show isosceles Pascal triangle! What a cry! All of my repositories and PyPI packages are MEANINGLESS AND USELESS!**

For your information, I can make a GitHub repository for 2 hours without distraction. I have long attention span. But that ability is no longer useful.


## 19th of September, 2026: I make this repo
For some reason, while I was asleep, **this syntax suddenly crossed my mind!**

```python
def stack(old, new):
    new_arr = old + new
    return new_arr
def create_zero_vector(N):
    return [0]*N
def create_zero_matrix(N):
    matrix = create_zero_vector(N)
    for i in range(N):
        matrix[i] = create_zero_vector(N)
    return matrix

```

WHAT?!! IS THAT A SOLUTION FOR `append()`?? Let I test it out. And it... WORKS!
Then, I make this repository, and I try it. And the result is (after some debugging)... ALL OF THEM WORKS!

> **WHAT?!?!?!? ALL OF THEM WORKS PROPERLY?!?! OH MY GOODNESS!!!!!**

But, there is a something that I must think.
> **"WHY DID THIS HAPPENS WHEN I WAS SLEEP?!?! WHY NOT ON THAT QUIZ????"**

I almost gave up, but if I'm trying to forget the code, My mind wandered to that code during other lectures.

For closing statement, answer this question. You can use AI to answer that.

**Why is it that when I sleep, the code I need automatically comes to mind, yet that doesn't happen when I'm taking a quiz?**