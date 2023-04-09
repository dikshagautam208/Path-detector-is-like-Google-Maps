## Route Detection
Objective is to find the shortest possible path from source to destination cell in the least amount of time possible.

Implemented Aldous-Broder algorithm for generating a uniform spanning maze.
A-star algorithm is simulated in pygame environment for finding the shortest route possible from source to destination cells

### How to run?
**requirements.txt** file contains the necessary python libraries to run the project
**main.py** => main file with the rendering loop and env, map, solver
**env.py** => PyGame maze rendering class
**map.py** => maze generating agent
**solver.py** => maze solving agent
**constants.py** => contains run parameters which can be tinkered with

```
$> pip install -r requirements.txt
```
This will install the necessary python libraries to run the project

```
$> python main.py
```
This will run the project. First it will generate a maze using **map.py** and solve this maze using **solver.py** file. The rendering is handled by the **env.py** file.

