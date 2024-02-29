# Dictionary to store user selections
frame = [{"index": 1, "value": "| 1 |"}, {"index": 2, "value": "| 2 |"}, {"index": 3, "value": "| 3 |"},
         {"index": 4, "value": "| 4 |"}, {"index": 5, "value": "| 5 |"}, {"index": 6, "value": "| 6 |"},
         {"index": 7, "value": "| 7 |"}, {"index": 8, "value": "| 8 |"}, {"index": 9, "value": "| 9 |"}
         ]

def winner():
    if frame[0]["value"] == frame[1]["value"] == frame[2]["value"]:
        print("You Won!!")
        return False
    elif frame[3]["value"] == frame[4]["value"] == frame[5]["value"]:
        print("You won!!")
        return False
    elif frame[6]["value"] == frame[7]["value"] == frame[8]["value"]:
        print("You won!!")
        return False
    elif frame[0]["value"] == frame[3]["value"] == frame[6]["value"]:
        print("You Won!!")
        return False
    elif frame[1]["value"] == frame[4]["value"] == frame[7]["value"]:
        print("You Won!!")
        return False
    elif frame[2]["value"] == frame[5]["value"] == frame[8]["value"]:
        print("You won!!")
        return False
    elif frame[0]["value"] == frame[4]["value"] == frame[8]["value"]:
        print("You won!!")
        return False
    elif frame[2]["value"] == frame[4]["value"] == frame[6]["value"]:
        print("You won!!")
        return False
    return True
