## 1) Reads in text file; prints out only lines containing 'Subject: '
##  Excludes the keyword 'Subject: '
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith("Subject: "):
        print(line.strip("Subject: "))
## 2) Prompts for a file name; reads through the file; looks for lines like:
## X-DSPAM-Confidence: 0.8475
## Computes spam confidence total values
## At the end, prints out the average spam confidence
count = 0
avgSpamConfidence = 0
print("Enter a file: ", end = '')
fhand = open(input())
for line in fhand:
    if line.startswith("X-DSPAM-Confidence: "):
        numFloat = float(line.strip("X-DSPAM-Confidence: "))
        avgSpamConfidence += numFloat
        count += 1

print("Average spam confidence:", round(avgSpamConfidence / count, 12))
