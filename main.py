# Name:Luis Munguia Salas, ID:010535076

import package as P
import clock as C
import data as D
import wgu_hub as W
import helper_functions as H
import nearest_neighbor as N
# import clock.py


def main():
  # information to user
  print("Hi, this is the WGUPS service, we have 40 packages to deliver today!")
  print("")
  print("Note: Deliveries will be made automatically. Sit back and relax supervisor.")
  print("Beginning deliveries......deliveries are en route.... ")
  
  # to keep track of different delivery times by different trucks
  # note: truck 1 will depart at "09:05", waiting at hub for delayed packages"
  truck1_clock = C.Clock("09:05")
  truck2_clock = C.Clock()
  
  wgu_hub = W.HashTableHub()
  
  # load packages into hub. limit 40
  for info in D.package_data:
    package = P.Package(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7]) 
    wgu_hub.insert_package(package)
          
  # create status keys for all packages until 1PM
  
  H.catchup_clock(C.Clock("07:59", "AM"), C.Clock("01:00", "PM"), wgu_hub)
  
  # going to load these packages (id's) first for priority and time constraint reasons  
  packages_to_load_into_truck1 = [4,5,6,7,8,9,10,13,17,25,21,27,28,32,35,39]
  packages_to_load_into_truck2 = [1,3,14,15,16,18,19,20,29,30,31,34,36,37,38,40]
  
  
  # load packages from hub into trucks
  truck1 = wgu_hub.remove_many_packages(packages_to_load_into_truck1)
  truck2 = wgu_hub.remove_many_packages(packages_to_load_into_truck2)
    
  # deliveries_made  = N.nearest_neighbor(D.all_locations_dictionary, truck2, truck2_clock, wgu_hub)
  # deliveries_made += N.nearest_neighbor(D.all_locations_dictionary, truck1, truck1_clock, wgu_hub)
  deliveries_made = N.nearest_neighbor(D.all_locations_dictionary, truck1, truck1_clock, wgu_hub)
    
  # if deliveries still need to be made continue to load packaged into trucks
  # choose arbitrary truck that is empty
  # deliveries_made += H.continue_deliveries(D.all_locations_dictionary, truck2, truck2_clock, wgu_hub)
  
  print("....beep....boop....bop.......")
  print(".......deliveries are finished")
  print("")
  print("******************************")
  # print("Time of last delivery: ", truck2_clock.get_time())
  # print("Total miles driven:", round(wgu_hub.distance_traveled, 2))
  print("******************************")
  print("")
  
  
  # for key, value in wgu_hub.hub_package_status.items():
  #   print(key, len(value))
  
  # user interface to retrieve status of package at any time as well as status of all packages
  print("Hi user, if you'd like to know the status of all packaged at a given time, ensure that you enter 'YES' in the following prompt, or enter 'NO'")
  # print("Note: Enter time that is less than or equal to 'Time of last delivery': ", truck2_clock.get_time())
  print("Note: Enter time that is less than or equal to '01:00 PM', this is the latest for tracking packages statuses")
  print("Note: Obviously you cannot find status of packages at 7PM if all deliveries were completed by 1PM. Also, deliveries began at 08:00 AM")
  print("Note: The results are long. You may have to scroll down to view")
  
  user_answer = input("enter 'YES' or 'NO': ") # to store user input
  user_answer = H.handle_user_input(user_answer) # handles invalid input
  
  # to handle invalid input and ask again
  while user_answer is None:
    print("")
    print("Entered invalid input, try again....")
    user_answer = input("Enter 'YES' or 'NO': ")
    user_answer = H.handle_user_input(user_answer)
  
  # to handle invalid input and ask for time
  while user_answer == True:
    print("Enter the time as (HH:MM AM) or (HH:MM PM) Ex: '09:00 AM' in the following prompt")
    user_answer = input("Enter (HH:MM AM) or (HH:MM PM): ")
    
    if user_answer in wgu_hub.hub_package_status:
      wgu_hub.search_all_packages_at_time(user_answer)
      print("")
      print("Would you like to try another time?")
      user_answer = input("Enter 'YES' or 'NO': ")
      user_answer = H.handle_user_input(user_answer)
    else:
      print("Invalid input, try again...")
      print("")
      user_answer = True
  
  print("")
  print("Hi user, if you'd like to know the status of any single package, ensure that you enter 'YES' in the following prompt, or enter 'NO'")
  
  user_answer = input("Enter 'YES' or 'NO': ")
  user_answer = H.handle_user_input(user_answer)
  
  while user_answer is None:
    print("")
    print("Entered invalidn input, try again...")
    user_answer = input("Enter 'YES' or 'NO': ")
    user_answer = H.handle_user_input(user_answer)
  
  while user_answer == True:
    print("Enter the ID number of the package you would like to retrieve (1 - 40 with No Decimals!) in the following prompt")
    user_answer = input("Enter ID number: ")
    
    if user_answer.isdigit() and (1 <= int(user_answer) <= 40):
      for package in deliveries_made:
        if package.id == int(user_answer):
          package.display_all_package_info()
          print("")
      
      print("Would you like to try another package ID?")
      user_answer = input("Enter 'YES' or 'NO': ")
      user_answer = H.handle_user_input(user_answer)
          
    else:
      print("Invalid input, try a number between 1 and 40, inclusive")
      print("")
      user_answer = True

main()