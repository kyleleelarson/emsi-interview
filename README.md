My solution is in interview_project.py.

It is written in Python version 3.9.1, and it was run via terminal on MacOS. 
The text file, lepanto.txt, should be in the same directory.

I used a vector space modeling approach, using the bag-of-words model. Each word (after normalizing) is treated as a token. 
The best_match function counts how many words in the input string appear in each line, and returns the line with the most.
