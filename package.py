# class to represent the package
class Package:
  def __init__(self, pack_id, address, city, state, zipcode, delivery_deadline, pack_weight, special_instructions, status = "At Hub"):
    # required attributes for package object
    self.id = pack_id
    self.address = address
    self.city = city
    self.state = state
    self.zipcode = zipcode
    self.pack_weight = pack_weight
    self.delivery_deadline = delivery_deadline
    self.special_instructions = special_instructions
    self.en_route_time = "None"
    self.delivered_time = "None"
    self.status = status    
    
  # update_package_status: will take user input to update package status(H,R, or D)
  # will update to: At hub, en route, delivered
  # Enter 'H' - at hub, 'R' - en route, 'D' - delivery 
  def update_package_status(self, package_status_input):
    
    if package_status_input.lower() == "h":
      self.status = "At Hub"
    elif package_status_input.lower() == "r":
      self.status = "En Route"
    elif package_status_input.lower() == "d":
      self.status = "Delivered"
    else:
      print("Please enter a valid entry")
      print("")
      self.update_status()
  
  # update_package_address: will take in new address information and update package information  
  def update_package_address(self, address, city, state, zipcode):
    self.address = address
    self.city = city
    self.state = state
    self.zipcode = zipcode
  
  # update_package_weight: will take in new weight information and update package information
  def update_package_weight(self, weight):
    self.pack_weight = weight
  
  # update_delivery_deadline: will take in new delivery deadline information and update package information
  def update_delivery_deadline(self, deadline):
    self.delivery_deadline = deadline
  
  # update_special_instructions: will take in new special instructions and update package information
  def update_special_instructions(self, instructions):
    self.special_instructions = instructions
  
  # set_en_route_time: will take in time (provided by the clock class in the algorithm) and set the time package left the hub
  def set_en_route_time(self, time):
    self.en_route_time = time
  
  # set_delivered_time: will take in time (provided by the clock class in the algorithm) and set the time package was delivered
  def set_delivered_time(self, time):
    self.delivered_time = time
  
  # this function will print out all of the package information when printing the package object    
  def display_all_package_info(self):    
    all_package_information = "Package ID: " + str(self.id)  + "\n" + "Address: " + self.address + "\n" + "City: " + self.city + "\n" + "State: " + self.state + "\n" + "Zipcode: " + self.zipcode + "\n" + "Pack weight: " + str(self.pack_weight) + "\n" + "Delivery deadline: " + self.delivery_deadline + "\n"+  "Special instructions: " + str(self.special_instructions) + "\n" + "en route time: " + str(self.en_route_time) + "\n" + "Delivered time: " + str(self.delivered_time) + "\n" + "Status: " + self.status
    print(all_package_information)
    print("")