def wr_new_text(text):
    with open("user_input.txt", "w") as f:
        f.write(text)

def add_text(text):
    with open("user_input.txt", "a") as f:
        f.write(text)




