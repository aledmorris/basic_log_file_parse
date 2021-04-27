import re
import glob
import os

file_location = '*support.log*'

#sorts the filename based on the modified time
filenames = sorted(glob.glob(file_location), key=os.path.getmtime)

# regex looks for user-agent data but is always followed by 'Allow' in the SDP
regex = '\^MUser-Agent\: (.*)\^MAllow'

#open file for writing
txt_file = open("user-agents.txt", "w")

for f in filenames:
    outfile = open(f,'r')
    data = outfile.readlines()
    outfile.close()

    match_list = []

    for line in data:
        for match in re.finditer(regex, line, re.S):
            match_text = match.group(1)
            match_list.append(match_text)
            #write match to file with newline
            txt_file.write(match_text+'\n')
            print(match_text)

txt_file.close