

import datetime

entry = input("What did you learn today ? ").strip()

rating = input("Rate your productivity today (1-5)").strip()

now = datetime.datetime.now()

date_str = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"\n Date: {date_str}\n{entry}"

if rating:
    journal_entry += f"\n Productivity Rating: {rating}\n"
    
journal_entry += "\n" + "_" * 50


with open("learning_journal.txt", "a", encoding="utf-8") as file:
    file.write(journal_entry)
    
print("Your entry has been saved to learning_journal.txt")
