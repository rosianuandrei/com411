# Ask user for place
print("Where should I look?")
place = input()

# Check the bedroom
if (place == "in the bedroom"):
    print("Where in the bedroom should I look?")
    bedroom_place = input()

    if (bedroom_place == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.") 
