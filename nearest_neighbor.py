import clock as C
import helper_functions as H

def nearest_neighbor(locat_map, truck, clock, hub):
  current_truck_location_address = "HUB" # start of truck trip, start from hub
  temp_clock = C.Clock(str(clock.get_time()[:5]))
  
  # update status of all packages because they are now in route
  truck = H.update_pack_status_en_route(truck, clock, hub)
  
  # put package 9 on hold until after address has been updated.
  waiting = []
  index_of_package = H.find_package_to_remove(truck, 9)
  
  if index_of_package is not None:
    waiting.append(truck.pop(index_of_package))
  
  # while there is still packages to deliver, choose minimum distance to drive relative to current_truck_location_address
  while len(truck) > 0:
    
    minimum_distance = 100 # variable to hold minimum_distance choice
    minimum_address = "" # to hold minimum distance choice address
    minimum_index = 0 # to hold index of to quickly locate within location dictionary
    package_id = None # to hold package id, to know which package to remove
    temp_distance = 0 # to hold temp distance travel from A to B.
    
    # get all package distances relative to the current_truck_location 
    for package in truck:
      target_address = package.address + " (" + package.zipcode + ")" # to hold address of package
      target_address_index = locat_map[target_address][-1] # to hold index of location for easy lookup in location dictionary
      
      # to hold distance of package location relative to current truck location
      dist_frm_truck_to_target = locat_map[current_truck_location_address][target_address_index]
      
      # if distance is less than minimum distance, then a new minimum distance has been found
      if dist_frm_truck_to_target < minimum_distance:
        # assign target location data to variables below for later use. truck will drive to minimum distance only
        minimum_distance = dist_frm_truck_to_target
        minimum_address = target_address
        minimum_index = target_address_index
        package_id = package.id
        temp_distance = dist_frm_truck_to_target
        
    # find index of package to delete
    index_of_package_to_remove = H.find_package_to_remove(truck, package_id)
    
    # update clock
    clock.update_clock(temp_distance)
    
    # do not deliver packages until address has been updated at "10:20"AM
    if clock.get_time() >= "10:20 AM" and len(waiting) > 0:
      waiting[0].update_package_address("410 S State St", "Salt Lake City", "UT","84111")
      truck.append(waiting.pop())
    
    
    # update statuses for each package every minute
    H.catchup_clock(temp_clock, clock, hub)  
    
    hub.update_distance_traveled(temp_distance)
    
    # update package status to delivered
    truck = H.update_pack_status_delivered(truck, index_of_package_to_remove, clock, hub)
    
    # truck has now drove to min distance location, assign it to current
    current_truck_location_address = minimum_address
  
  # update clock after returning to Hub
  clock.update_clock(locat_map[current_truck_location_address][0])
  
  # update statuses for each package every minute up  until 1 PM
  H.catchup_clock(temp_clock, C.Clock("01:00","PM"), hub)
  
  # track deliveries made by trucks
  deliveries_made = hub.packages_en_route_or_delivered
  
  # reset the status of packages delivered/en route after truck is done
  hub.packages_en_route_or_delivered = []
  
  return deliveries_made