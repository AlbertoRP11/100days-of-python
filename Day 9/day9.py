# Day 9
# Dictionaries, Nesting and the Secret Auction

# Exercício Final 
# Secret Auction
from art import logo

print(logo)
print("Welcome to the secret auction program!")

bids_list = []
end_bidding = False

def find_highest_bid(bidlist):
    highest_bid = 0
    for bid in bidlist:
        if bid["bid_value"] > highest_bid:
            highest_bid = bid["bid_value"]
            winner = bid["name"]

    print(f"The winner is {winner} with a bid of R${highest_bid}")

while not end_bidding:
    name = input("What's your name?\n")
    bid = int(input("What's your bid?\n"))
    bids_list.append({"name": name, "bid_value": bid})
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if should_continue == "no":
        find_highest_bid(bids_list)
        end_bidding = True



programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item n a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Exercicio 1
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     grade = "Outstanding"
#   elif score > 80:
#     grade = "Exceeds Expectations"
#   elif score > 70:
#     grade = "Acceptable"
#   else:
#     grade = "Fail"

#   student_grades[student] = grade

# print(student_grades)

# Nesting 
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting a dictionary in a list
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]

# Exercício 2
# country = input("Add country name")
# visits = int(input("Number of visits"))
# list_of_cities = eval(input()) # create list from formatted string

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]

# def add_new_country(country, total_visits, visited_cities):
#   travel_log.append({
#     "country": country,
#     "visits": total_visits,
#     "cities": visited_cities
#   })

# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")