class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
    

    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
  


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else: 
            print(f"{name} is already in the network.")
    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]
            person1.add_friend(person2)
            person2.add_friend(person1)
        else: 
            print("One or both persons not found in the network")  

    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name} is friends with: {', '.join(friend_names)}")

        
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
  




# Now build the full social network
network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")
network.add_person("Alex")  #  error
# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")  # error
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Print the final network
print("\nSocial Network:")
network.print_network()

#Why is a graph the right structure to represent a social network?
#the graph is the perfect structure to represent a social network because it allows efficient representation for relationships between people, where each person is a node and the friendships are the edges between them. these allows for easy lookups of friends, mutual connections, and network traversal
#Why wouldn’t a list or tree work as well for this?
#A list would not work because it cant represent effectively the relationships between people, it would just be a list of names without any connectoins. on the other hand, a tree structure would have to have a hierarchical relationships, which does not fit social networks where relationshiops are bidirectional and without any hierarchy
#What performance or structural trade-offs did you notice when adding friends or printing the network?
#when adding friends, the performance is generally efficient as it involves only lookups and appending, which are O(1) operations on average. however, as the networks keep growing the memory usage increases due to the storage of the connections. on the other hand printing the network invovles going trhough each person and their friends which would be (i think in the worse case) O(n+e)where n is the number of people annd e is the number of friendships. this will become very slow if we are managing networks with a very large number of users and connections
