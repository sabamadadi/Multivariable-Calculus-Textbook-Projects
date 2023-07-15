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

[Link to Maple Code](https://github.com/sabamadadi/Multivariable-Calculus-Textbook-Projects/tree/main/Project%201/14.93)

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
9. Upon exiting the loop, the value of x represents the approximation of the root. Report the obtained root value.

#### Results
The Newton's method iteration converged to a root approximation of x ≈ 0.5493061443340548 for
the given function f(x) = arctan(x) - 1/3.

#### Conclusion
By utilizing Newton's method, we successfully approximated the root of the function f(x) = arctan(x)
- 1/3. Newton's method is an effective iterative algorithm for finding roots of functions when the
initial guess is close enough to the true root.


### 14.94 

[Link to Maple Code](https://github.com/sabamadadi/Multivariable-Calculus-Textbook-Projects/tree/main/Project%201/14.93)

#### Introduction
This report presents the surface and contour plots of the ID function, which is defined as f(x) = x^4 -
4x^2 + 1. The plots provide insights into the behavior and characteristics of the ID function.

#### Methodology
1. Define the ID function as ID(x) = x^4 - 4x^2 + 1.
2. Generate a meshgrid of x and y values in the desired range.
3. Calculate the corresponding z values using the ID function.
4. Create surface plots with different views to visualize the function in a three-dimensional space.
5. Create contour plots with different windows to visualize the function's contours and level curves.

#### Results
Surface Plots
The surface plots provide a three-dimensional representation of the ID function.
- Surface Plot - View 1: The plot shows the ID function from a default viewpoint.
- Surface Plot - View 2: The plot shows the ID function from an elevated viewpoint.
- Surface Plot - View 3: The plot shows the ID function from a different elevated viewpoint.
Contour Plots
The contour plots display the ID function's contours and level curves.
- Contour Plot - Window 1: The plot shows the contours of the ID function within the range [-2, 2] for
both x and y.
- Contour Plot - Window 2: The plot zooms in on the range [-1, 1] for both x and y, providing a closer
view of the contours.
- Contour Plot - Window 3: The plot further zooms in on the range [-0.5, 0.5] for both x and y.
- Contour Plot - Window 4: The plot focuses on a small range of [-0.1, 0.1] for both x and y, revealing
detailed contours.

#### Conclusion
The surface and contour plots of the ID function provide a visual representation of its behavior and
characteristics. The surface plots demonstrate the overall shape of the function, while the contour
plots illustrate the contours and level curves at different zoom levels. These plots help in
understanding the critical points, curvature, and overall behavior of the ID function.

## Project 2. The Volume of the Unit Ball in n-Dimensions

## Project 3. The Area of Heart

[Download Textbook](https://skim.math.msstate.edu/LectureNotes/Calculus_Multivariable.pdf)

[Lectures on YouTube](https://www.youtube.com/channel/UCmRbK4vlGDht-joOQ5g0J2Q)

[Seongjai Kim](https://www.linkedin.com/in/seongjai-kim-51435b263/)

