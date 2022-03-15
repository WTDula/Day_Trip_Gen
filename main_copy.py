import random

def main():
    destinations = ["Lexington, KY", "Chicago, IL", "Austin, TX", "Washington, D.C."]
    transportation = ["Plane", "Train", "Helicopter", "Rental Car"]
    restaurants = ["Malone's Steakhouse", "Lou Malnati's", "Franklin Barbeque", "The Capital Grille"]
    attractions = ["The Bourbon Trail", "Willis Tower (Sears Tower)", "Live Music at Sixth Street", "The National Mall"]
    trip_details = []

    

    def roll_destinations(destinations_list, initial_choice):
        split_this_list = initial_choice(destinations_list)
        if(split_this_list[1] == False):
            print("Sorry you did not like this destination. We will choose a new one.")
            roll_destinations()
        else:
            # when confirmed, display affirmation message
            print("Excellent! It's a great place to visit!")
            # when confirmed, return chosen destination
            return split_this_list[0]
        

    def roll_transportation():
        transportation_choice = random.choice(transportation) # random transportation from transportation list
        user_choice = input(f"We have selected {transportation_choice} as your mode of transportation.  Does this sound fun? Enter y/n: ")
        user_choice = user_choice.lower() # make sure input is lower case
        # if not acceptable mode of transportation, display message, reroll new transportation
        if(user_choice == "n"):
            print("Sorry you did not like this transportation.  We will choose a new one.")
            roll_transportation()
        else:
            # when confirmed, display affimation message, append choice to trip_details at index 1
            print("Excellent!")
            trip_details.append(transportation_choice)
            # return trip_details]


    def roll_restaurants():
        restaurant_choice = random.choice(restaurants) # random restaurant from restaurants list
        user_choice = input(f"We have selected {restaurant_choice} as your restaurant.  Does this sound appetizing? Enter y/n: ")
        user_choice = user_choice.lower() # make sure input is lower case
        # if not acceptable restaurant, display message, reroll new restaurant
        if(user_choice == "n"):
            print("Sorry you did not like this restaurant.  We will choose a new one.")
            roll_restaurants()
        else:
            # When confirmed, display affirmation message, append choice to trip_details at index 2
            print("Excellent! We're sure you'll have a fantastic meal!")
            trip_details.append(restaurant_choice)
            # return trip_details

    def roll_attractions():
        attraction_choice = random.choice(attractions) # random attraction from attractions list
        user_choice = input(f"We have selected {attraction_choice} as your main attraction.  Does this sound like a good time? Enter y/n: ")
        user_choice = user_choice.lower() # make sure input is lower case
        # if not acceptable attraction, display apology, reroll new attraction
        if(user_choice == "n"):
            print("Sorry that attraction does not sound fun!  We'll chooce another.")
            roll_attractions()
        else:
            # When confirmed, display affirmation message, append choice to trip_details at index 3
            print("Excellent! You're gonna have a lot of fun!")
            trip_details.append(attraction_choice)
            # return trip_details

    # destination will be at trip_details[0], transpo at [1], restaurant at [2], attraction at [3]
    def display_final_details():
        print("Awesome!  We have completed generating your trip!  Let's look at all of the details!")
        print(f"Destination:\t\t{trip_details[0]}")
        print(f"Transportation:\t\t{trip_details[1]}")
        print(f"Restaurant:\t\t{trip_details[2]}")
        print(f"Entertainment:\t\t{trip_details[3]}")
        user_choice = input("Would you like to finalize this trip? Enter y/n: ")
        user_choice = user_choice.lower() # more input validation
        # if not happy with final details, start day trip gen over
        if(user_choice == "n"):
            print("Sorry you did not like one or more of your details....restarting Day Trip Generator")
            main()
        else:
            # if user accepts all final details, display final message
            final_message()

    # destination @ trip_details[0],, transpo @ [1], restaurant @ [2], attraction @ [3]
    def final_message():
        # Combine all details into one message
        print(f"Get ready for the time of your life!  You will arrive in {trip_details[0]} via {trip_details[1]}.  You will dine at {trip_details[2]}, and go see {trip_details[3]}!  Have Fun!!")
    
    def initial_choice(category):
        return_list = []
        category_choice = random.choice(category)
        return_list.append(category_choice)
        user_choice = input(f"We have selected {category_choice}. Is this acceptable? Enter y/n: ")
        user_choice = user_choice.lower()
        if(user_choice == "n"):
            return_list.append(False)
        else:
            return_list.append(True)
        return return_list
            


    # Function calls
    print(f"Welcome to the Day Trip Generator!  I am sure we can plan an exciting adventure for you.")
    trip_details.append(roll_destinations(destinations, initial_choice))
    roll_transportation()
    roll_restaurants()
    roll_attractions()
    display_final_details()


main()