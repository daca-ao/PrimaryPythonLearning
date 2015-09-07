# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
text = handle.read()
words = text.split()

counts = dict()
for line in handle:
    if line.startswith('From ') and not line.startswith('From: '):
        line = line.split()
        counts[line[1]] = counts.get(line[1], 0) + 1

maxMail = None
maxNum = None
for email, count in counts.items():
    if maxMail == None or count > maxNum:
        maxMail = email
        maxNum = count
print maxMail, maxNum