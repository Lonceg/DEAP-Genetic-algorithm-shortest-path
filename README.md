Python code which uses DEAP library for finding the most optimal solution with the use of genetic algorithm.

In this code, problem is finding the shortest path from point A to point B while avoiding obstacles.

Problem is written as a set of numbers such as starting point and middle point/points coordinates.

Each solution is rated seperatly based on their performance (length). Running into obstacles is punshied by decreased performance.

By changing one variable it is decided from how many points solution can be made out of.

Best solutions have the highest chance to survive and produce offspring. Offspring is a mix of both parents (meaning point coordinates may be mixed)

There is also a chance of mutation. Starting population is set to 500. Upon reaching set amount of generations, the best solution is presented.

Problem with 1 point solution, 

![image](https://github.com/Lonceg/Genetic-algorithm-shortest-path/assets/92753179/d59695df-c13e-4b1e-aa09-d25d52fe6bd8)

The harder problem with 2 point solution

![image](https://github.com/Lonceg/Genetic-algorithm-shortest-path/assets/92753179/345ab52b-bb60-48e6-b55e-20f9458a0615)

Even harder problem with 2 point solution (algorith with this many points cannot find solution, and as such finds that the best solution is with the penalty)

