from collections import defaultdict

def add_course(graph, course, prerequisites):
    for prereq in prerequisites:
        graph[prereq].append(course)

def dfs(graph, visited, stack, course):
    visited.add(course)
    for neighbor in graph[course]:
        if neighbor not in visited:
            dfs(graph, visited, stack, neighbor)
    stack.append(course)

def topological_sort(graph):
    visited = set()
    stack = []
    for course in list(graph.keys()):  # Iterate over a copy of keys
        if course not in visited:
            dfs(graph, visited, stack, course)
    return stack[::-1]


if __name__ == "__main__":
    graph = defaultdict(list)
    
    num_courses = int(input("Enter the number of courses: "))                                     #5
    for _ in range(num_courses):                                                                  #1        2      3       4     5
        course_name = input("Enter the course name: ")                                            #Intro    DS    AdvDS   Algo   ML
        num_prerequisites = int(input(f"Enter the number of prerequisites for {course_name}: "))  #0        1       1      1     2
        prerequisites = []
        for _ in range(num_prerequisites):                                                        #         1       1      1    1       2
            prerequisite = input("Enter the prerequisite: ")                                      #        Intro    DS    DS    AdvDS  Algo
            prerequisites.append(prerequisite)
        add_course(graph, course_name, prerequisites)
    
    topological_order = topological_sort(graph)
    print("Topological sorting order of courses:")                                                # Intro,DS,AdvDS,Algo,ML
    print(topological_order)
