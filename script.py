import re

INPUT_FILE = 'input_file.txt'
OUTPUT_FILE = 'output_file.txt'

file = open(INPUT_FILE, 'r',encoding='utf-8')
file2 = open(OUTPUT_FILE, 'a+',encoding='utf-8')
file2.seek(0)
list = [r"\bhttps://youtu.*", r"\bhttps://www.you.*", r"\bhttps://www.mu.*", r"\bhttps://mu.*"]

for x in file:
    link = None
    for y in range(len(list)):
        li = re.search(list[y],x)
        if li:
            link = li.group()
            break
    if link:
        if not any(link.rstrip('\n') == x.rstrip('\r\n') for x in file2):
            file2.write(link +'\n')
file.close()
file2.close()
print("Done")
