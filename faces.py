# define convert function
def convert(text):

    # replace :) with 🙂 and :( with 🙁
    user_text = text.replace(":)","🙂").replace(":(","🙁")

    #return the converted user input
    return user_text

def main():
    # take input 
    user_input = input("enter your word : ")

    # call the convert function and store the result in a new variable
    result = convert(user_input)

    #printing the converted user input
    print(f"{result}")

main()