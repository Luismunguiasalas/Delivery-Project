import nearest_neighbor as N

# helper functions for nearest neighbor

# this function will iterate over all packages and update en route status and time
def update_pack_status_en_route(truck, clock, hub):
  
  for package in truck:
    package.update_package_status("r")
    package.set_en_route_time(clock.get_time())
    hub.packages_en_route_or_delivered.append(package)
    hub.create_status_of_all_packages_at_time(clock.get_time())
    
  return truck

# update_pack_status: will update status of package delivered, including time, and will remove from truck
def update_pack_status_delivered(truck, index_of_package_to_remove, clock, hub):
  truck[index_of_package_to_remove].update_package_status("d") # update package status to delivered
  truck[index_of_package_to_remove].set_delivered_time(clock.get_time()) # set time of delivery
  hub.packages_en_route_or_delivered.append(truck.pop(index_of_package_to_remove)) # remove package from truck
  hub.create_status_of_all_packages_at_time(clock.get_time())
  
  return truck

# find_package_to_remove: will loop through each package in the truck to find 
# correct package to deliver and return an index
def find_package_to_remove(truck, package_id_to_remove):
  index_of_package_to_remove = 0
  
  while index_of_package_to_remove < len(truck):
    if truck[index_of_package_to_remove].id ==  package_id_to_remove:
      return index_of_package_to_remove
    else:
      index_of_package_to_remove += 1
      
  return None

# it takes in a start_clock, that will iterate every minute until the time is equal to end_clock
# at every iteration, it creates a status of all packages
def catchup_clock(start_clock, end_clock, hub):
  while start_clock.get_time() != end_clock.get_time():
    start_clock.update_clock(0.3)
    hub.create_status_of_all_packages_at_time(start_clock.get_time())
        
# ----------------------------------------------------------------  
# helper functions for main()

# continue_deliveries: if Hub is not empty; will continue to get packages from hub and load them to the truck and perform nearest_neighbor()
# will do this until all packages are delivered, i.e. hub is empty. returns list of deliveries made
def continue_deliveries(locat_map, truck, clock, hub, temp_list = None):
  hub_not_empty = True
  while hub_not_empty:
    more_packages = False
    packages_to_load_into_truck2 = []
    
    # find packages in hub
    for package in hub.hub:
      if package is not None:
        packages_to_load_into_truck2.append(package.id)
        more_packages = True
    # load packages into truck
    truck = hub.remove_many_packages(packages_to_load_into_truck2)
    
    # deliver packages
    if more_packages:
      deliveries_made =  N.nearest_neighbor(locat_map, truck, clock, hub)
    
    # is hub empty?
    hub_not_empty = more_packages
  
  return deliveries_made

# handle_user_input(): will ensure yes or no are the only valid inputs
def handle_user_input(user_input):
  if user_input.isalpha() and user_input.lower() == "yes":
    return True
  elif user_input.isalpha() and user_input.lower() == "no":
    return False
  else:
    return None
    