def story_gen(who, name, residence):
    return line1 + line2
import random
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 1st of April', 'Before Thanos arrived', 'In future']
who = input("Who:")
name = input("Name:")
residence = input("Location:")
went = ['Zoo', 'Cinema', 'Supermarket', 'Cheesecake shop', 'Shopping mall', 'Bat Cave', 'Avengers HQ', 'Hospital', 'Work', 'School', 'Nowhere', 'Overseas']
went1 = random.choice(went)
happened = ['made a lot of friends', 'had a burger', 'found a stash of money', 'solved a mistery', 'to fight for justice', 'to dance', 'saved an elderly person', 'died', ]
happened1 = random.choice(happened)
find = ['friends', 'money', 'vampires', 'gold', 'food', 'COVID', ' a date']

line1=( RED + random.choice(when) + ',' + BLUE + (who) +' named '+ (name) + ' that lived in ' + CYAN + (residence) +', went to the ' + (went1) + ' and ' + BLUE + (happened1) + '.' )
line2=( RED + (name) + ' loves going to ' + GREEN + (went1) + ' along with friends.' + CYAN +(went1) + ' is the best place to find ' + random.choice(find) + '.')
print (line1,line2)
