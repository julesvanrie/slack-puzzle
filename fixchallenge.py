"""Ugly piece of code to test if students actually look at
our slack messages."""

import os
import string
import requests

#######################
## Setting it all up ##
#######################

BASE_URI = "http://localhost:5000"

message_on_import = """
Great! You made it to here :-)
So you have read the message on Slack. Cool!

But did you leave a little green check or some other emoji
on the channel, so the teacher actually knows you saw it?

If not, now is the time to do it, before you can go to
the next part of this little puzzle.

Did you do it?    """

wait_for_check = """
OH NO!!! Please leave a checkbox or something else then.
Did you do it now?    """

thank_you_for_check = """
Thank you, very much appreciated.
Now, let's move on to the next part..."""

puzzle_message = """
Follow the instructions in the following piece of text to get your reward.
Oh, it has been encrypted. :grinning-face:
So you will have to find the function to decode it..."""

# TODO: get request to back end with username and user
# replace the next print with the request
user = os.getenv("USER")
print(f"{user}")


def decoder(text):
    '''Given a string, this function will decode it.'''
    if text:
        chars = string.ascii_letters
        encoding = {coded: encoded for coded, encoded in zip(chars, chars[::-1])}
        new_text = ""
        for c in text:
            new_text += encoding.get(c, c)
        return new_text
    else:
        return "Please give me some text to decode."

puzzle_text_decoded = f"""
Great work {user.capitalize()} !!!
You have decoded this message, and solved the first part of this puzzle.
Now, you can go to the second part to finally claim your reward:

Go on and find the function to submit your result to the game platform.
"""

puzzle_text_encoded = f"""
tIVZG DLIP {decoder(user.capitalize())} !!!
bLF SZEV WVXLWVW GSRH NVHHZTV, ZMW HLOEVW GSV URIHG KZIG LU GSRH KFAAOV.
mLD, BLF XZM TL GL GSV HVXLMW KZIG:

tL LM ZMW URMW GSV UFMXGRLM GL HFYNRG BLFI IVHFOG GL GSV TZNV KOZGULIN.
"""


def submit():
    url = BASE_URI + "/imported/" + decoder(user.capitalize())
    result = requests.get(url).json()
    print(result)


##################
## Main program ##
##################


print(decoder(puzzle_text_encoded))

answer = input(message_on_import)

while answer.upper() not in ["YES", "Y", "I DID", "YES!"]:
    answer = input(wait_for_check)

print(thank_you_for_check)


# Showing the encrypted message
print(puzzle_message)
print(puzzle_text_encoded)
