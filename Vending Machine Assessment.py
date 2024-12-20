# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:27:20 2024

@author: Seanp
"""

import sys
import time

#'categories' is a library accessing three lists called drinks, snacks, and candy
categories = { 
    "drinks" : [ #all three lists access five different libraries with product names and prices
         {
             0 : "Back"
         },
         {
            "Name" : "Coke",
            "Price" : 3.0
        },
        
        {
            "Name" : "Pepsi",
            "Price" : 3.0
        },
        
        {
            "Name" : "Fanta",
            "Price" : 3.0
        },
        {
            "Name" : "Water",
            "Price" : 1.0
        },
        {
            "Name" : "Iced Coffee",
            "Price" : 4.0
        }
    ],
    "snacks" : [
        {
            0 : "Back"
        },
        {
            "Name" : "Potato Chips",
            "Price" : 1.5
        },
        {
            "Name" : "Popcorn",
            "Price" : 2.5
        },
        {
            "Name" : "Crackers",
            "Price" : 1.0
        },
        {
            "Name" : "Cookie Sandwiches",
            "Price" : 1.5
        },
        {
            "Name" : "Protein Bar",
            "Price" : 1.25
        }
    ],
    "candy" : [
        {
            0 : "Back"
        },
        {
            "Name" : "Kitkat Bar",
            "Price" : 2.5
        },
        {
            "Name" : "Twix Bar",
            "Price" : 2.5
        },
        {
            "Name" : "Maltesers",
            "Price" : 2.75
        },
        {
            "Name" : "Reese's Cups",
            "Price" : 2.0
        },
        {
            "Name" : "M&Ms",
            "Price" : 2.25
        }
    ]
}

payment = 0.0 #declaring default payment variable
change = 0.0 #declaring default change variable
yes = "yes" #yes for choices
no = "no" #no for choices

def drinksPick (): #custom function for drinks category
    time.sleep(1) #delays the execution by one second
    repeatloop = True
    print ("""
           [1] Coke (3.0)
           [2] Pepsi (3.0)
           [3] Fanta (3.0)
           [4] Water (1.0)
           [5] Iced Coffee (4.0)
           [0] Back
           """)
    while repeatloop:
        drinksInput = int(input("Please select at your leisure: ")) #looking for what the user wants
        if drinksInput != 0 and drinksInput >= 1 and drinksInput <=5: #if statement for user's choice
            choice = input("You will purchase this product, are you sure? ") #making sure they want the chosen product
            if choice.casefold() == yes.casefold():
                while True:
                    payment = float(input(f"The price is {categories['drinks'][drinksInput]['Price']}, please input your payment: ")) #asks for the payment of the product they selected
                    if payment >= categories['drinks'][drinksInput]['Price']: #the arithmetics of the product price and inserted payment
                        change = payment - categories['drinks'][drinksInput]['Price'] #the change they'd get if they put an excess amount
                        print (f"You have purchased {categories['drinks'][drinksInput]['Name']}. Your change is :", change) #declares to the user what they bought, as well as their change
                        sys.exit() #exits the system
                    else:
                        print ("You don't have enough cash for this item.") #will loop this if they dont have enough money until they input the right amount
            elif choice.casefold() == no.casefold(): #if they choose no, it will loop back to picking which item they want
                repeatloop = True
            else:
                print ("Invalid input, please answer with yes or no.") #making sure they answer yes or no
        elif drinksInput == 0: #if they input 0, they will go back to main menu with other categories
            categoryinterface()
        else:
            print ("Please enter a valid product ID.")
        
def snacksPick(): #same principles with different content
    time.sleep(1)
    repeatloop = True
    print ("""
           [1] Potato Chips (1.5)
           [2] Popcorn  (2.5)
           [3] Crackers (1.0)
           [4] Cookie Sandwiches (1.5)
           [5] Protein Bar (1.25)
           [0] Back
           """)
    while repeatloop:
        snacksInput = int(input("Please select at your leisure: "))
        if snacksInput != 0 and snacksInput >= 1 and snacksInput <=5:
            choice = input("You will purchase this product, are you sure? ")
            if choice.casefold() == yes.casefold():
                while True:
                    payment = float(input(f"The price is {categories['snacks'][snacksInput]['Price']}, please input your payment: "))
                    if payment >= categories['snacks'][snacksInput]['Price']:
                        change = payment - categories['snacks'][snacksInput]['Price']
                        print (f"You have purchased {categories['snacks'][snacksInput]['Name']}. Your change is :", change)
                        sys.exit()
                    else:
                        print ("You don't have enough cash for this item.")
            elif choice.casefold() == no.casefold():
                repeatloop = True
            else:
                print ("Invalid input, please answer with yes or no.")
        elif snacksInput == 0:
            categoryinterface()
        else:
            print ("Please enter a valid product ID.")
    
def candyPick(): #same principles with different content
    time.sleep(1)
    repeatloop = True
    print ("""
           [1] Kitkat Bar (2.5)
           [2] Twix Bar (2.5)
           [3] Maltesers (2.75)
           [4] Reese's Cups (2.0)
           [5] M&Ms (2.25)
           [0] Back
           """)
    while repeatloop:
        candyInput = int(input("Please select at your leisure: "))
        if candyInput != 0 and candyInput >= 1 and candyInput <=5:
            choice = input("You will purchase this product, are you sure? ")
            if choice.casefold() == yes.casefold():
                while True:
                    payment = float(input(f"The price is {categories['candy'][candyInput]['Price']}, please input your payment: "))
                    if payment >= categories['candy'][candyInput]['Price']:
                        change = payment - categories['candy'][candyInput]['Price']
                        print (f"You have purchased {categories['candy'][candyInput]['Name']}. Your change is :", change)
                        sys.exit()
                    else:
                        print ("You don't have enough cash for this item.")
            elif choice.casefold() == no.casefold():
                repeatloop = True
            else:
                print ("Invalid input, please answer with yes or no.")
        elif candyInput == 0:
            categoryinterface()
        else:
            print ("Please input a valid product ID.")


def categoryinterface (): #category picking for the user
    while True:
        userCategory = input("""
                Drinks
                Snacks
                Candy
                Exit
                Please select a category: 
                            """) 
        if userCategory == "drinks".casefold() or userCategory == "snacks".casefold() or userCategory == "candy".casefold() or userCategory == "exit".casefold():
            break
        print ("Please choose a valid category.")
    if userCategory == "drinks".casefold():
        drinksPick()
    elif userCategory == "snacks".casefold():
        snacksPick()
    elif userCategory == "candy".casefold():
        candyPick()
    elif userCategory == "Exit".casefold():
        sys.exit()

categoryinterface() #executes the entire code for the user