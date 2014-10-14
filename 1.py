#Write a shopping list in Notepad and save it as 'shopping.txt'. Write a program to read in the shopping list from the file and display it on the screen.
def shopping_list():
    with open("shoppinglist.txt" , mode="r", encoding ="utf-8") as my_file:
        for line in my_file:
            print(line)
