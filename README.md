# string-tsp
A set of gurobi models for creating string-based tsp art.

These use the python gurobi interface and some sort of visual outputter to solve string-based tsp lps and plot a visual approximation of them. It is modular such that a number of different types of tsps can be solved.

Uses gurobi to create graph configuration files and then networkx/matplotlib to render them.

The three models are:

grid1:
Uses the darkness of squares inbetween the nails (as judged by the number of strings going through them) to generate the image. Allows for nodes of any even degree, and only edges which are 1 diagonal space or a knight move away.

grid2:
Same, but only allows for nodes of degree 2 or 0.

grid3:
Averages pixel darknesses along the line created by the edge, and tries to maximize overall closeness to these values. Allows for nodes of any even degree, and any edges.
