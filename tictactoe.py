from winner import winner, frame


is_game_active = True
counter = 0
while winner():
    selected_box = input("Select where you want to place your mark:")
    counter += 1
    if counter % 2 != 0:
        if frame[int(selected_box)]['value'] != f"| {selected_box} |":
            print('Box already filled')
        frame[int(selected_box) - 1]["value"] = "| X |"
    else:
        frame[int(selected_box) - 1]["value"] = "| O |"
    winner()
    for index, box in enumerate(frame):
        if box["index"] % 3 == 0:
            print(frame[index-2]['value']+frame[index-1]['value']+frame[index]['value'])



