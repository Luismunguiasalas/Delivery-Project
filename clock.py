import math

# class to represent the clock, that drivers will use to keep time as they deliver packages
class Clock:
  def __init__(self, time = "08:00", ante_or_post_meridiem = "AM"):
    self.time = time
    self.ante_or_post_meridiem = ante_or_post_meridiem
    self.minutes_in_hour = 60
    self.hours_in_a_day = 24
    
  def get_time(self):
    return self.time + " " + self.ante_or_post_meridiem
    
  def update_clock(self, distance_traveled):
    # use this variable to store the mph of truck
    mph_speed_of_truck = 18
    
    # get the slice current time property
    current_hours = int(self.time[:2])
    current_minutes = int(self.time[3:])
    
    # calculate time it took to get from point A to point B by using distance_traveled / 18mph * 60
    travel_in_minutes = (distance_traveled / mph_speed_of_truck) * self.minutes_in_hour
    
    # if travel_in_minutes has greater than 55 seconds it will round up to nearest min, or round down if less than .55 seconds
    if travel_in_minutes - math.floor(travel_in_minutes) > .55:
      travel_in_minutes = math.ceil(travel_in_minutes)
    else:
      travel_in_minutes = math.floor(travel_in_minutes)
    
    # add travel_in_minutes to current_minutes clock
    current_minutes += travel_in_minutes  
    current_hours += int(current_minutes // self.minutes_in_hour)  # add to current_hours using floor
      
    # if current_minutes >= 60,
    if current_minutes >= self.minutes_in_hour:
      current_minutes = int(current_minutes % self.minutes_in_hour)  # set current_minutes to remainder using modulo
    
    # if current_hours >= 13  
    if current_hours >= (self.hours_in_a_day // 2) + 1:
      
      # update from AM to PM, vice versa
      if self.ante_or_post_meridiem == "AM":
        self.ante_or_post_meridiem = "PM"
      else:
        self.ante_or_post_meridiem = "AM"
      
      # if current_hours == 13, then current_hours should = 1. Else, assign current_hours = current_hours % 12
      if current_hours == (self.hours_in_a_day // 2) + 1:
        current_hours = 1
      else:
        current_hours = (current_hours % (self.hours_in_a_day // 2))
    
    # if length = 1, then add additional digit to keep HH:MM format
    if len(str(current_hours)) == 1:
      current_hours = "0"+ str(current_hours)
    
    # if length = 1, then add additional digit to keep HH:MM format
    if len(str(current_minutes)) == 1:
      current_minutes = "0"+ str(current_minutes)
    
    # assign recently calculated time to time variable
    self.time = str(current_hours) + ":" + str(current_minutes)
    
    # call get_time function to return the recently calculated time
    # return self.get_time()