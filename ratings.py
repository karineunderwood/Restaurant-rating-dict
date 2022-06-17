"""Restaurant rating lister."""


# put your code here
def processing_restaurant_rating():
    file_data = open("scores.txt")
    scores_dict = {}

    for line in file_data:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores_dict[restaurant] = int(score)
    
    return scores_dict

def add_scores(scores_dict):
    "Add a restaurant and rating."

    print("Please rate your favorite restaurant")
    restaurant = input("Restaurant name > ")
    rating = int(input("You rating: "))

    scores_dict[restaurant] = rating

def print_restaurant_alphabetic_order(scores_dict):
    "Print all of the ratings in alphabetic order"

    for restaurant, rating in sorted(scores_dict.items()):
        print(f"{restaurant} is rated at {rating}.")
 
 # read existing scores in from file
scores_dict = processing_restaurant_rating()
# allow user to add a restaurant/rating pair
add_scores(scores_dict)
# print an alphabetical list of all rated restaurants and their ratings
print_restaurant_alphabetic_order(scores_dict)

