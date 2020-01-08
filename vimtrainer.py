#Created by Nic Holaday 2016
#nic.holaday@comfyapp.com

import random
import time
import vimdict

#instead of having dictionaries in program import from csv files

cycles = 1
wronglist = []
correct_counter = 0
total_counter = 0
answertime = []
commands = []

while commands == []:
    print "Please enter which command set to practice\n"
    for cont in sorted(vimdict.contents):
        print cont
    print ""

    selection = raw_input("> ")
    for cont in vimdict.contents:
        if selection == cont:
            print "\n" + cont + "!"
            commands = vimdict.contents[selection]
    if commands == []:
        print "Invalid selection"

for i in range(0, cycles):
    print "List of %d commands running %d cycle(s)" % (len(commands), cycles)
    keys = commands.keys()

    random.shuffle(keys)

    for question in keys:
        start = time.time()

        print question, "> ",
        answer = raw_input()

	if commands[question] in answer:
            correct_counter += 1
#            print "Correct!"
        else:
            print "Incorrect, answer is: %s" % (commands[question])
            wronglist.append(commands[question])

        total_counter += 1
        end = time.time()

        answertime.append(end - start)

print "\nCongrats! Score: %d / %d" % (correct_counter, total_counter)
accuracy = (float(correct_counter) / float(total_counter) * 100)
print "Average answer time: %.2fs, Accuracy: %.0f" % (sum(answertime)/len(answertime), accuracy), "%"

print "You got these commands incorrect: "
print wronglist, "\n"
