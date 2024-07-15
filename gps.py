"""Create routes between cities on a map."""
from dis import Instruction
import sys
import argparse

# Your implementation of City, Map, bfs, and main go here.
class City:
    """ A class to hold data representing a city
    Attributes:
        name(str): The name of the city 
        neighbors(dict): A dictionary that will hold a city object and the other city objects it is connected to ex.(distances)  
    """
  
class City:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def __repr__(self):
        return self.name
    def add_neighbor(self, neighbor, distance, interstate):
        self.neighbors[neighbor] = (distance, interstate)
        

   
  
    def __init__(self, name) -> None:
        """ This method initlizes the city object
        Args:
            Name(str): allows one to see class documentation
        """
        self.name = name
        self.neighbors = {}
 
        
 
 
    def __repr__(self) -> str:
        """
        Returns a string represrentation of Class Object
        Returns:
            City Name
        """
        return self.name 
    
  
  
  
    def add_neighbor(self, neighbor, distance, interstate):
        """
        Adds a neighbor to dict
        Args:
            neighbor(City): A city object
            distance(str): Shows the distance between the two different cities
            interstate(str): Shows the interstate number that connects two cities ex.95 
        """
        city_tuple = (distance, interstate)
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = city_tuple
            
        

        if self not in neighbor.neighbors:
            neighbor.neighbors[self] = city_tuple
            



class Map:
    """ A class that stores data in a graph to represent 
    Attributes:
    citites: A list of city objects
    
    """
    def __init__(self, relationships) -> None:
        """ Initilizing the Map class
        relationships(dict): A dictionary where the keys are individual cities and values are list of tuples that shows
        distances between cities and which interstate conncects them 
        """
        self.cities = []


        for key in relationships:
          

            if key not in [n.name for n in self.cities]:
                city = City(key)
                self.cities.append(city)


            big_city_index = [n.name for n in self.cities].index(key)
                

            for name_val in relationships[key]:
                neighbor, dist, interstate = name_val
                
                if neighbor not in [n.name for n in self.cities]:
                    second_city = City(neighbor)
                    self.cities.append(second_city)


                neighbor_city_index = [n.name for n in self.cities].index(neighbor)
                self.cities[big_city_index].add_neighbor(self.cities[neighbor_city_index], dist, interstate)
                     
            
    def __repr__(self) -> str:
        """
        returns a string reperesentation of the list of cities 
        """
        return str(self.cities)



def bfs(Graph, start, goal):
    """ This method is to find shortest path to final city destination
    Args:
        Graph(Map): a Map object
        start(str): city at which gps is starting from 
        goal(str): city at which is the goal and final destination
    Returns:
        a list of cities for the gps path or None
    """
   
    explored = []
    queue = [[start]]
    
    while queue:
        first_path = queue.pop(0)
        last_node = first_path[-1]
        if last_node not in explored:
             index_pos = [n.name for n in Graph.cities].index(str(last_node))     
             saved_neighbors = Graph.cities[index_pos].neighbors
         
             for key in saved_neighbors:
                new_path = list(first_path)
                new_path.append(key)
                queue.append(new_path)
                
              
              
                if key.name == goal:
                    
                  
                    return [str(n) for n in new_path]
             explored.append(last_node)
                
   
   
    return None
    
        
    
       
        
def main(start, destination, Graph):
    output = ""
    """
    The functions will create a map object, use bfs() to find a path and will
    direct the driver on which cities and interstates they should drive through to get final destination
    
    Args:
        start(str): start city
        destination(str): desitnation city
        Graph(dict): A dictionary representing an adjacency list of cities
    Returns:
        String of instuctions 
    """
    map = Map(Graph)
    instructions = bfs(map, start, destination)
    first_output = ""        
    
    for index, elem in enumerate(instructions):


        if elem == instructions[0]:
            second_output = f"Starting at {elem}"
            print(second_output)
            first_output += second_output

        if elem is not instructions[-1]:
            next_city = instructions[index+1]
            for city in map.cities:
               
                if city.name == elem:
                    saved_neighbors = city.neighbors
                  
                    for key in saved_neighbors:
                        distance_to_drive, interstate = saved_neighbors[key]
                      
                        if str(key) == next_city:
                            third_output = f"Drive {distance_to_drive} miles on {interstate} towards {next_city}, then"
                            print(third_output)
                            output += third_output

        elif elem == instructions[-1]:
            fourth_output = "You will arrive at your destination"
            print(fourth_output)
            first_output += fourth_output
   
   
   
    return first_output
   



def parse_args(args_list):
    """Passes a list of strings from the command prompt as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """





def parse_args(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('--starting_city', type=str, help='The starting city in the route.')
    parser.add_argument('--destination_city', type=str, help='The destination city in a route.')
    args = parser.parse_args(args_list)
    return args

   
    
    return args

if __name__ == "__main__":
    
    connections = {  
        "Baltimore": [("Washington", 39, "95"), ("Philadelphia", 106, "95")],
        "Washington": [("Baltimore", 39, "95"), ("Fredericksburg", 53, "95"), ("Bedford", 137, "70")], 
        "Fredericksburg": [("Washington", 53, "95"), ("Richmond", 60, "95")],
        "Richmond": [("Charlottesville", 71, "64"), ("Williamsburg", 51, "64"), ("Durham", 151, "85")],
        "Durham": [("Richmond", 151, "85"), ("Raleigh", 29, "40"), ("Greensboro", 54, "40")],
        "Raleigh": [("Durham", 29, "40"), ("Wilmington", 129, "40"), ("Richmond", 171, "95")],
        "Greensboro": [("Charlotte", 92, "85"), ("Durham", 54, "40"), ("Ashville", 173, "40")],
        "Ashville": [("Greensboro", 173, "40"), ("Charlotte", 130, "40"), ("Knoxville", 116, "40"), ("Atlanta", 208, "85")],
        "Charlotte": [("Atlanta", 245, "85"), ("Ashville", 130, "40"), ("Greensboro", 92, "85")],
        "Jacksonville": [("Atlanta", 346, "75"), ("Tallahassee", 164, "10"), ("Daytona Beach", 86, "95")],
        "Daytona Beach": [("Orlando", 56, "4"), ("Miami", 95, "268")],
        "Orlando": [("Tampa", 94, "4"), ("Daytona Beach", 56, "4")],
        "Tampa": [("Miami", 281, "75"), ("Orlando", 94, "4"), ("Atlanta", 456, "75"), ("Tallahassee", 243, "98")],
        "Atlanta": [("Charlotte", 245, "85"), ("Ashville", 208, "85"), ("Chattanooga", 118, "75"), ("Macon", 83, "75"), ("Tampa", 456, "75"), ("Jacksonville", 346, "75"), ("Tallahassee", 273, "27") ],
        "Chattanooga": [("Atlanta", 118, "75"), ("Knoxville", 112, "75"), ("Nashville", 134, "24"), ("Birmingham", 148, "59")],
        "Knoxville": [("Chattanooga", 112,"75"), ("Lexington", 172, "75"), ("Nashville", 180, "40"), ("Ashville", 116, "40")],
        "Nashville": [("Knoxville", 180, "40"), ("Chattanooga", 134, "24"), ("Birmingam", 191, "65"), ("Memphis", 212, "40"), ("Louisville", 176, "65")],
        "Louisville": [("Nashville", 176, "65"), ("Cincinnati", 100, "71"), ("Indianapolis", 114, "65"), ("St. Louis", 260, "64"), ("Lexington", 78, "64") ],
        "Cincinnati": [("Louisville", 100, "71"), ("Indianapolis,", 112, "74"), ("Columbus", 107, "71"), ("Lexington", 83, "75"), ("Detroit", 263, "75")],
        "Columbus": [("Cincinnati", 107, "71"), ("Indianapolis", 176, "70"), ("Cleveland", 143, "71"), ("Pittsburgh", 185, "70")],
        "Detroit": [("Cincinnati", 263, "75"), ("Chicago", 283, "94"), ("Mississauga", 218, "401")],
        "Cleveland":[("Chicago", 344, "80"), ("Columbus", 143, "71"), ("Youngstown", 75, "80"), ("Buffalo", 194, "90")],
        "Youngstown":[("Pittsburgh", 67, "76")],
        "Indianapolis": [("Columbus", 175, "70"), ("Cincinnati", 112, "74"), ("St. Louis", 242, "70"), ("Chicago", 183, "65"), ("Louisville", 114, "65"), ("Mississauga", 498, "401")],
        "Pittsburg": [("Columbus", 185, "70"), ("Youngstown", 67, "76"), ("Philadelphia", 304, "76"), ("New York", 391, "76"), ("Bedford", 107, "76")],
        "Bedford": [("Pittsburg", 107, "76")], #COMEBACK
        "Chicago": [("Indianapolis", 182, "65"), ("St. Louis", 297, "55"), ("Milwaukee", 92, "94"), ("Detroit", 282, "94"), ("Cleveland", 344, "90")],
        "New York": [("Philadelphia", 95, "95"), ("Albany", 156, "87"), ("Scranton", 121, "80"), ("Providence,", 95, "181"), ("Pittsburgh", 389, "76")],
        "Scranton": [("Syracuse", 130, "81")],
        "Philadelphia": [("Washington", 139, "95"), ("Pittsburgh", 305, "76"), ("Baltimore", 101, "95"), ("New York", 95, "95")]
    }
    
    args = parse_args(sys.argv[1:])
    main(args.starting_city, args.destination_city, connections)
