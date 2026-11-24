# Personal Diary using python programming language 

diary = []

entry = input("Write your diary entry: ")
diary.append(entry)

print("\nYour Diary Entries:")

for note in diary:
    print("-", note)

print("Total entries:", len(diary))