import data
from data import Rectangle, Duration
from typing import Optional

# Write your functions for each part in the space below.

# Part 1
#input is 2 points
#output is a rectangle
#find the most left x coord, highest y coord, put this into new top left coord
#find the most right x coord, lowest y coord, put this into nwe bottom right coord
#use top left and bottom right coord to make a rectangle
def create_rectangle(point1: data.Point, point2: data.Point)->data.Rectangle:
    bottom_right = data.Point(0,0)
    top_left = data.Point(0,0)
    if point1.x > point2.x:
        bottom_right.x = point1.x
        top_left.x = point2.x
    else:
        bottom_right.x = point2.x
        top_left.x = point1.x
    if point1.y < point2.y:
        bottom_right.y = point1.y
        top_left.y = point2.y
    else:
        bottom_right.y = point2.y
        top_left.y = point1.y
    rectangle1 = data.Rectangle(top_left, bottom_right)
    return rectangle1
# Part 2
#input is 2 durations
#output is True or False
#compare time one and two, if time 1 is shorter than time 2 return true, else false
def shorter_duration_than(time1:data.Duration,time2:data.Duration)->bool:
    if time1.minutes > time2.minutes:
        return False
    if time1.minutes < time2.minutes:
        return True
    if time1.minutes == time2.minutes:
        if time1.seconds>time2.seconds:
            return False
        if time1.seconds<time2.seconds:
            return True

# Part 3
# input is list of songs, a duration
#output is a list of songs
#list all the songs that are shorter than the inputted duration
def song_shorter_than(songs: list[data.Song], length:data.Duration)->list[data.Song]:
    list1 = []
    for i in songs:
        if shorter_duration_than(i.duration,length):
            list1.append(i)
    return list1

# Part 4
#inputs are list of songs, a list of song indexes
#output is the duration
#for each index add the corresponding song's length to a variable, then if there are more than 60 seconds in the attribute seconds fix it
def running_time(songs: list[data.Song], playlist: list[int])->data.Duration:
    length = data.Duration(0,0)
    for i in playlist:
        length.minutes += songs[i].duration.minutes
        length.seconds += songs[i].duration.seconds
    while length.seconds > 59:
        length.seconds -= 60
        length.minutes += 1
    return length
# Part 5
#input is a list of pairs of cities, also a list of names of cities in order to represent a route
#output is True or False
#for the length of the route list and for each pair of cities check if the route city and the next city are found in the pair
#if they are found add to a counter, by the end of all the comparisons if the counter and the number of cities in the route are equal then the route is valid
def validate_route(links: list[list[str]],names:list[str])->bool:
    yes = 1
    for i in range(len(names)-1):
        yn = False
        for j in links:
            if yn != True:
                if (names[i] == j[0] or names[i] == j[1]) and (names[i+1] == j[0] or names[i+1] == j[1]):
                    yn = True
                    yes += 1
                else:
                    yn = False
    if len(names) == 0 or len(names) == 1:
        return True
    if yes < len(names):
        return False
    if yes == len(names):
        return True
# Part 6
#input is list of integers
#output is none or integer
#for each value check if it is the same as the next and if it is, add how many times the same number is in a row.
#do this for each value in the list and compare which had the highest sequence
def longest_repetition(values: list[int])->Optional[int]:
    highest = 0
    counter = 1
    for i in range(len(values)):
        a = 1
        if i < len(values)-1:
            while values[i] == values[i+a]:
                counter += 1
                a += 1
            if counter > highest:
                highest = counter
                counter = 1
                index = i
            else:
                counter = 1
    return index