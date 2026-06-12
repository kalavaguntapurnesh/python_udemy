import textwrap

name = input("Enter your name : ").strip()

profession = input("Enter your profession : ").strip()

passion = input("Enter your passion : ").strip()

emoji = input("Enter your favourite emoji : ").strip()

website = input("Enter your favourite website : ").strip()

print("\nChoose your style: ")

print("1. Simple Lines")
print("2. Vertical Flair")
print("3. Emoji Sandwich")

style = input("Enter 1, 2 or 3 : ").strip()



def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession}💡\n  {passion}\n {website}"

    elif style == "2":
        return f"{emoji} {name}\n {profession}🔥\n {passion}\n {website}"
    elif style == "3":
        return f"{emoji * 3}\n {name} - {profession}\n {passion}\n {website}\n{emoji * 3}"
    
    
bio = generate_bio(style)

print("\nYour Generated Bio:\n")
print("*"*50)
print(textwrap.dedent(bio)) #dedent removes any common leading whitespace from every line in the input text
print("*"*50)

save = input("Do you want to save this bio to a file ? (y/n) : ").strip().lower()

if save == "y":
    filename = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(bio)
    print("File Saved Successfully !")