# string-tsp
A set of gurobi models for creating string-based tsp art.

These use the python gurobi interface and some sort of visual outputter to solve string-based tsp lps and plot a visual approximation of them. It is modular such that a number of different types of tsps can be solved.

Uses gurobi to create graph configuration files and then a simple processing script to render them.

Graphs are notated with a list of point x,y values on the first line in some order, then the following lines have (i,j) values indicating connections between points i and j, with an optional third value indicating a color
