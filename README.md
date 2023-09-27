Python code which uses DEAP library for finding the most optimal solution with the use of genetic algorithm.

In this code, problem is finding the shortest path from point A to point B while avoiding obstacles.

Problem is written as a set of numbers such as starting point and middle point/points coordinates.

Each solution is rated seperatly based on their performance (length). Running into obstacles is punshied by decreased performance. Solutions can be composed out of multiple points, and that is controlled by changing a variable.

Best solutions have the highest chance to survive and produce offspring. Offspring is a mix of both parents (meaning point coordinates may be mixed). There is also a chance of gaussian mutation (change in one of the coordinates by set amount).

Starting population is set to 500 but can be increased based on the performance. Upon reaching set amount of generations, the best solution is presented. Mutation and crossing parameters are changed based on whether alogirthm converges towards optimal solution.

Problem with 1 point solution:

![image](https://github.com/Lonceg/Genetic-algorithm-shortest-path/assets/92753179/d59695df-c13e-4b1e-aa09-d25d52fe6bd8)

The harder problem with 2 point solution

![image](https://github.com/Lonceg/Genetic-algorithm-shortest-path/assets/92753179/358e7666-ffd2-4b6b-9277-9af89b436256)
