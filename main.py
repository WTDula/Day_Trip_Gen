<<<<<<< HEAD
import random

def main():
    destinations = ["Lexington, KY", "Chicago, IL", "Austin, TX", "Washington, D.C."]
    transportation = ["Plane", "Train", "Helicopter", "Rental Car"]
    restaurants = ["Malone's Steakhouse", "Lou Malnati's", "Franklin Barbeque", "The Capital Grille"]
    attractions = ["The Bourbon Trail", "Willis Tower (Sears Tower)", "Live Music at Sixth Street", "The National Mall"]
    trip_details = []

    def display_welcome_message():
        print("Welcome to the Day Trip Generator!  I am sure we can plan an exciting adventure for you.")

    def roll_destinations():
        destination_choice = random.choice(destinations) # random destination from destinations list
        # initial display/confirmation
        user_choice = input(f"We have selected {destination_choice} as your destination.  Does this sound fun? Enter y/n: ")
        user_choice = user_choice.lower() # make sure input is lower case y/n
        # if user does not like destination, print message and get a new random destination
        if(user_choice == "n"):
            print("Sorry you did not like this destination. We will choose a new one.")
            roll_destinations()
        else:
            # when confirmed, display affirmation message
            print("Excellent! It's a great place to visit!")
            # when confirmed, append choice to trip_details at index 0
            trip_details.append(destination_choice)
        

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
    
    # Function calls
    display_welcome_message()
    roll_destinations()
    roll_transportation()
    roll_restaurants()
    roll_attractions()
    display_final_details()

=======
import random

def main():
    destinations = ["Lexington, KY", "Chicago, IL", "Austin, TX", "Washington, D.C."]
    transportation = ["Plane", "Train", "Helicopter", "Rental Car"]
    restaurants = ["Malone's Steakhouse", "Lou Malnati's", "Franklin Barbeque", "The Capital Grille"]
    attractions = ["The Bourbon Trail", "Willis Tower (Sears Tower)", "Live Music at Sixth Street", "The National Mall"]
    trip_details = []

    def display_welcome_message():
        print("Welcome to the Day Trip Generator!  I am sure we can plan an exciting adventure for you.")

    def roll_destinations():
        destination_choice = random.choice(destinations) # random destination from destinations list
        # initial display/confirmation
        user_choice = input(f"We have selected {destination_choice} as your destination.  Does this sound fun? Enter y/n: ")
        user_choice = user_choice.lower() # make sure input is lower case y/n
        # if user does not like destination, print message and get a new random destination
        if(user_choice == "n"):
            print("Sorry you did not like this destination. We will choose a new one.")
            roll_destinations()
        else:
            # when confirmed, display affirmation message
            print("Excellent! It's a great place to visit!")
            # when confirmed, append choice to trip_details at index 0
            trip_details.append(destination_choice)
        

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
    
    # Function calls
    display_welcome_message()
    roll_destinations()
    roll_transportation()
    roll_restaurants()
    roll_attractions()
    display_final_details()


main()
>>>>>>> 39810ed8818c8532ceb65f072145e8d6eb472013
