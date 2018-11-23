##import functions###
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList


##GOAL:To retrieve a list of restaurants given a single input of what food type user enters
##

####variables###
#copy existing data

food_types = types
restaurants_list = restaurant_data


###functions####


##create a list of dictionary keys for array
##O(N)
def char_keys(lists):
    char_keys = []
    for item in lists:
        
        if item[0] not in char_keys:
            char_keys.append(item[0])
        else:
            pass
    return char_keys



##create a list of values for keys starting with the first letter
#if there is more than one value, it is added to the values list
O(N)
def find_values(key,value_list):
     
    key_value_list = []
        
    for item in value_list:
        if item[0] == key:
            key_value_list.append(item)
            
    return key_value_list



##create hashmap {first letter: food_types}, runtime = O (N^2) during map generation
##Runtime = O(1) when searching

food_types_keys = char_keys(food_types)
food_types_hashmap = HashMap(len(food_types_keys))
for i in food_types_keys:
    values_list = find_values(i,food_types)
    food_types_hashmap.assign(i,values_list)

"""
###TEST CHECK 
for i in food_types_keys:
    values = food_types_hashmap.retrieve(i)
    print("values at {0} are {1}".format(i,values))
"""

##return list of food_types for user_input
def food_type_output(user_input):
    return food_types_hashmap.retrieve(user_input)



#search_food_types(input_char)
#takes user_input and result from food_type_output
#check char match at each list position
#return search_food_type
#O(N)runtime
##not working like I want it to....
##assumes input of >1 char

def search_food_types(input_char, food_list):
    
    word_list = food_list
    len_list = len(word_list)
    list_idx = 0
    word_idx = len(input_char)
    
    while len_list > 0:

        if word_list[list_idx][0:word_idx] == input_char:
            return word_list[list_idx]
            break
        else:
            len_list -= 1
            list_idx += 1

    return("Option not found, please try again.")

        
         
        
##GENERATE restaurant_data_hashmap, runtime O(N^2)
##runtime for hashmap is O(1)

restaurant_data_hashmap = HashMap(  len(food_types) )

for i in food_types:
   
    restaurant_values_list = find_values(i,restaurants_list)
    restaurant_data_hashmap.assign(i,restaurant_values_list)

"""
##TEST
for i in food_types:
    shop_values = restaurant_data_hashmap.retrieve(i)
    print("values at {0} are {1}".format(i,shop_values))
"""


def get_restaurant_data(search_food_types):
    return restaurant_data_hashmap.retrieve(search_food_types)

"""
##TEST##
italian = get_restaurant_data('italian')
print (italian)
"""

def restaurants_sort_print(restaurants):
    separator = "*******=======*******"

    print("\n\nThe following restaurants found are:\n")

    for item in restaurants:
        print (separator)
        
        print("\nName: {0}\n"
              "Price: {1}/5\n"
              "Rating: {2}/5\n"
              "Address: {3}\n".format(item[1],item[2],item[3],item[4]))

"""
##TEST##
pizza = get_restaurant_data('pizza')           
print (restaurants_sort_print(pizza))
"""







#Printing the Welcome Message
print_welcome()

##user interaction
while True:
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    #Search for user_input in food types data structure here


##CONDITIONS
##must be valid string input, string length
##
    
    
    if user_input not in food_types_keys:
        print("Sorry, there's no food type beginning with '{0}'.\nPlease try another letter.".format(user_input))

    else:  #user_input in food_types_keys

        food_output = food_type_output(user_input)

        ##for condition when there is only one type for the char
        if len(food_output) == 1:
            print ("The food choice beginning with '{0}' is: {1}".format(user_input,food_output[0]))
            yn_input = str(input("\nWould you like to see the list of restaurants? y/n \n"))


            if yn_input == 'y':

                data = food_output[0]         
                print_data = restaurant_data_hashmap.retrieve(data)
                restaurants_sort_print(print_data)

            else:
                pass

        ##for when there is a need to search the list through
        else:
            print ("The food choice beginning with '{0}' are: {1}".format(user_input,food_output))


       
            user_input2 = (str(input("Please enter the first letters of the food you want. \n\n")))

            data = search_food_types(user_input2, food_output)
            print (data)
            print ("The food choice beginning with '{0}' is: {1}".format(user_input2,data))

            yn_input = str(input("\nWould you like to see the list of restaurants? y/n \n"))


            if yn_input == 'y':

                  
                print_data = restaurant_data_hashmap.retrieve(data)
                restaurants_sort_print(print_data)

            else:
                pass
                                  

    

