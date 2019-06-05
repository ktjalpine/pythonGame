
class total_game_inventory :
    weapons = ["M4","Bow","AK47","Knife","Glock 30"]
    provisions = ["Animal Meat","Canned Goods","Water","Beer","Whiskey"]
    coldGear = ["Heavy Patagonia Coat","North Face Himalaya Suit","North Face Himalaya Gloves","Patagonia Skiing Pants",
                "Fleece lined balaclava","Beanie"]
    campingGear = ["Mountain Hardwear Fitz Roy Tent","Mountain Hardwear Ghost Sleeping Bag"]





def startInventory():
    print("\nYour current inventory is as follows:")

def startTimeSystem(added_time):
    starting_time = 1600
    current_time = starting_time + added_time
    time_range = [0,2400]
    if current_time > time_range[1]:
        rem = time_range[1] - added_time
        current_time = time_range[0] + rem

