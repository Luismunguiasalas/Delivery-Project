import copy

# class to represent the WGU HUB
class HashTableHub:
  def __init__(self, initial_capacity = 40):
    
    # required capacity of Hub
    self.initial_capacity = initial_capacity
    # track distance traveled for 3 trucks
    self.distance_traveled = 0
    
    # initialize all the buckets to None
    self.hub = [None] * initial_capacity
    
    # list to hold all en_roue or packages delivered
    self.packages_en_route_or_delivered = []
    
    # dictionary to hold all package status at any time
    self.hub_package_status = {}
  
  # insert_package: takes a package object as input and inserts it into a bucket index (hub)
  def insert_package(self, package):
    
    bucket = package.id % self.initial_capacity # get bucket index
    buckets_probed = 0 # to track buckets probed
    
    while buckets_probed < self.initial_capacity:
      if self.hub[bucket] is None:
        self.hub[bucket] = package
        return True
      
      # if the bucket was occupied, then calculate new bucket to insert into (bucket + 1)
      bucket = (bucket + 1) % self.initial_capacity 
      buckets_probed += 1
      
    # if the table is full (entire hub is full) then the pacakfge could not be stored
    return False
  
  def remove_many_packages(self, package_list):
    list_of_packages_removed_from_hub = []
    
    for package_id in package_list:
      bucket = package_id % self.initial_capacity
      buckets_probed = 0
      
      while (self.hub[bucket] is not None) and (buckets_probed < self.initial_capacity):
        if self.hub[bucket].id == package_id:
          temp = self.hub[bucket]
          self.hub[bucket] = None
          list_of_packages_removed_from_hub.append(temp)
          break
        
        # the bucket was occupied and not hte correct package id, look up the next bucket (bucket + 1)
        bucket = (bucket + 1) % self.initial_capacity
        buckets_probed += 1
    
    # print(list_of_packages_removed_from_hub)
    return list_of_packages_removed_from_hub
        
  # remove_single_package: will take package id as input and search for it in the hub and remove it return True, else None if not found
  def remove_single_package(self):
    
    package_id = self.user_input_package_id() # to hold user input
    bucket = package_id % self.initial_capacity # get bucket index
    buckets_probed = 0  # to track buckets probed
    
    while (self.hub[bucket] is not None) and (buckets_probed < self.initial_capacity):
      if self.hub[bucket].id == package_id:
        temp = self.hub[bucket]
        self.hub[bucket] = None
        return temp
        
      # the bucket was occupied and not the correct pacakge id, look up the next bucket (bucket + 1)
      bucket = (bucket + 1) % self.initial_capacity
      buckets_probed += 1
    
    # the entire table (hub) was searched and no such package was found.
    return None
  
  # the look up function for hub
  # search_single_package: takes user input through "user_input_package_id" then search all buckets until found and return package, else None is returned
  def search_single_package(self):   
    
      package_id_to_lookup = self.user_input_package_id() # to hold user input
      bucket = package_id_to_lookup % self.initial_capacity # get bucket index
      buckets_probed = 0 # to track buckets to probed
      
      while (self.hub[bucket] is not None) and (buckets_probed < self.initial_capacity):
        if self.hub[bucket].id == package_id_to_lookup: # if package id matched id_to_lookup
          return self.hub[bucket] # return package
        
        # the bucket was occupied, then calculatte the new bucket to search into (bucket + 1)
        bucket = (bucket + 1) % self.initial_capacity
        buckets_probed += 1
      
      # if not in hub, then in hub_package_status
      for package in self.packages_en_route_or_delivered:
        if package.id == package_id_to_lookup:
          return package
        
      # the entire table (hub) and tracking storage (packages en route or delivered) was searched and no such package was found.
      return None
  
  # search_all_packages at given time: provides status of all packages by returning a list of all packages to the calling function, 
  # as well as the sum of distance traveled by all trucks, and distance traveled at given time
  def search_all_packages_at_time(self, time):
    print("")
    print("Total distance traveled: ", round(self.distance_traveled, 2), " Miles")
    print("")
    print("All package info:  ")
    print("")
    for package in self.hub_package_status[time].values():
      if not(isinstance(package, float)) and not(isinstance(package, int)):
      # if type(package) != float():
        package.display_all_package_info()
      else:
        print("*****")
        print("Total Distance Traveled: ", round(package,2), " miles")
        print("At time: ", time)
        print("*****")
        print("")
      
  
  # user_input_package_id: will take in user input and handle if incorrect packaged id's are entered. for this case only 1 - 40 are valid package id's
  # will return package id to calling function
  def user_input_package_id(self):
    # handle user input for package id
    correct_input = True
    package_id_to_lookup = None
    
    while correct_input:
      # get user input
      package_id_to_lookup = input("Enter package 'id' number you would like to get (1 - " + self.initial_capacity + ":  ")
      print("")
      # requirements for user input
      if package_id_to_lookup.isdigit() and (1 <= int(package_id_to_lookup) <= self.initial_capacity):
        correct_input = False
        package_id_to_lookup = int(package_id_to_lookup)
      else:
        print("Enter a valid package id number")
        print("")
        
    return package_id_to_lookup
  
  # create_status_of_all_packages_at_time: will take in a time, create a key with time and a nested dictionary that contains distance_traveled,
  # then loop through hub and packaged_en_route_or_delivered and create/store/update package statuses at given time
  # it also updates distance traveled by trucks at that given time.
  def create_status_of_all_packages_at_time(self, time):
    if time not in self.hub_package_status:
      self.hub_package_status[time] = {"Distance Traveled": self.distance_traveled}

    for package in self.hub:
      if package is not None:
        self.hub_package_status[time][package.id] = copy.deepcopy(package)
        
    for package in self.packages_en_route_or_delivered:
      if package is not None:
        self.hub_package_status[time][package.id] = copy.deepcopy(package)
    
    self.hub_package_status[time]["Distance Traveled"] = self.distance_traveled
  
  def update_distance_traveled(self, distance):
    self.distance_traveled += distance