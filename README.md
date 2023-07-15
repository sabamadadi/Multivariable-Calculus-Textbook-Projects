# Multivariable Calculus Textbook Projects

## Project 1. Linear and Quadratic Approximations 

<p align="center"> <img src="Project 1/1.png" /> </p>
<p align="center"> <img src="Project 1/2.png" /> </p>
<p align="center"> <img src="Project 1/3.png" /> </p>
<p align="center"> <img src="Project 1/4.png" /> </p>
<p align="center"> <img src="Project 1/5.png" /> </p>
<p align="center"> <img src="Project 1/6.png" /> </p>
<p align="center"> <img src="Project 1/7.png" /> </p>

### 14.93
#### Introduction
This report presents the application of Newton's method to find the root of the function f(x) =
arctan(x) - 1/3. Newton's method is an iterative root-finding algorithm that utilizes the derivative of
a function to approximate its roots.

#### Methodology
1. Define the function f(x) = arctan(x) - 1/3.
2. Calculate the derivative of f(x) with respect to x, denoted as df(x).
3. Set the initial guess x0 = 0.5.
4. Set the tolerance (tol) to 0.1e-9 to determine the convergence criteria.
5. Set the maximum number of iterations (maxIter) to 100 as a safeguard against infinite loops.
6. Initialize the current and previous values of x as x and xPrev, respectively.
7. Initialize the iteration counter iter to 0.
8. Execute a while loop until the difference between x and xPrev is greater than the tolerance and
the maximum number of iterations has not been reached:
- Update xPrev to store the previous value of x.
- Compute df_value as the value of df(x) using the derivative function.
- Compute f_value as the value of f(x) using the function f.
- Update x by subtracting f_value divided by df_value.
- Increment the iteration counter iter.
9. Upon exiting the loop, the value of x represents the approximation of the root.
 10. Report the obtained root value.

#### Results
The Newton's method iteration converged to a root approximation of x ≈ 0.5493061443340548 for
the given function f(x) = arctan(x) - 1/3.

#### Conclusion
By utilizing Newton's method, we successfully approximated the root of the function f(x) = arctan(x)
- 1/3. Newton's method is an effective iterative algorithm for finding roots of functions when the
initial guess is close enough to the true root.


## Project 2. The Volume of the Unit Ball in n-Dimensions

## Project 3. The Area of Heart

[Download Textbook](https://skim.math.msstate.edu/LectureNotes/Calculus_Multivariable.pdf)

[Lectures on YouTube](https://www.youtube.com/channel/UCmRbK4vlGDht-joOQ5g0J2Q)

[Seongjai Kim](https://www.linkedin.com/in/seongjai-kim-51435b263/)

