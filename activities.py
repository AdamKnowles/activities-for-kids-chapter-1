# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

# For example, Jay ran like a fool! or Chantelle slid down the slide!.

# The following lists of children should be iterated, and the names sent to the appropriate functions.

# running_kids = ["Pam", "Sam", "Andrea", "Will"]
# swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
# sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
# hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

running_kids = ["Pam", "Sam", "Andrea", "Will"]

swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]

sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]

hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

def run(kids):
    for name in kids:
        print(f'{name} ran a mile!')

run(running_kids)

def swing(kids):
    for name in kids:
        print(f'{name} is swinging!')

swing(swinging_kids)

def slide(kids):
    for name in kids:
        print(f'{name} is sliding down the slide!')

slide(sliding_kids)

def hide(kids):
    for name in kids:
        print(f'{name} is hiding from the monster!')

hide(hiding_kids)
