def inputs_questions_country():
    Number_Of_Countries = int(input("How many countries do you want to visit? "))
    Countries_list = []
    while Number_Of_Countries < 1:
        Number_Of_Countries = int(input("Please enter a valid number \n How many countries do you want to visit? "))
    if Number_Of_Countries == 1:
        Countries_list.append((input("Which country ? ")))
    else:
        Countries_list.append(input("What is the first country ? "))
        for n in range(Number_Of_Countries-1):
            Countries_list.append(input("What else ? "))
    return(Countries_list)

def inputs_questions_city():
    Number_Of_Cities = int(input("How many cities do you want to visit? "))
    while Number_Of_Cities < 2:
        Number_Of_Cities = int(input("Please enter a valid number \n How many cities do you want to visit? "))
    else:
        Cities_list = []
        Cities_list.append((input("What is the first city ? ")))
        for n in range(Number_Of_Cities-1):
           Cities_list.append((input("What else ? ")))
    return(Cities_list)
    
Countries_list = inputs_questions_country()
Cities_list = inputs_questions_city()
    
print(Countries_list, Cities_list)