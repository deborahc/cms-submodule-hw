import os
import csv



PATH = "/home/deborahc/Documents/school/Spring_2015/CMS.831/cms-submodule-hw/CMS.631-s15-Favorite-Restaurants"

# Read files to get all lines
all_lines = []
for f in os.listdir(PATH):
    if f.endswith(".csv"):
        with open(PATH + "/" +f, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            ## Skip first line
            csvfile.readline()
            for line in reader:
                all_lines.append(line)
print all_lines

# Write files
with open('all.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['user', 'restaurant', 'address'])
    for line in all_lines:
        reformat = ['"' + line[0] + '"','"' + line[1] + '"', '"' + line[2]+ '"']
        print line, 'line'
        writer.writerow(line)

