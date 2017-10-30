t_exist = False
c_exist = False
g_exist = False

card_list = []

t_cards = 0
c_cards = 0
g_cards = 0

list = [i for i in input()]

for x in range(len(list)):
    if list[x] == "T":
        t_exist = True
        t_cards += 1
    elif list[x] == "C":
        c_exist = True
        c_cards += 1
    else:
        g_exist = True
        g_cards += 1

card_list.append(t_cards)
card_list.append(c_cards)
card_list.append(g_cards)

#sum of the squares
answer = (t_cards * t_cards)+(c_cards * c_cards)+(g_cards * g_cards)


#check how many sets of bonus 7 points are added
if t_exist and c_exist and g_exist:
    answer += 7*min(card_list)

print(answer)

