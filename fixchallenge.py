"""Ugly piece of code to test if students actually look at
our slack messages."""

import os
import string
import requests

#######################
## Setting it all up ##
#######################

BASE_URI = "https://slack-puzzle-jvr.herokuapp.com/"
# BASE_URI = "http://localhost:5000"

check = None

__user = os.getenv("USER")

__first_message = """
\033[91mThis might take a minute. Please be patient and stay here.
"""

__message_on_import = """
\033[94mGreat! You made it to here :-)
So you have read the message on Slack. Cool!

But did you leave a little green check or some other emoji
on the channel, so the teacher actually knows you saw it?

If not, now is the time to do it, before you can go to
the next part of this little puzzle.

Did you do it?    """

__wait_for_check = """
\033[91mOH NO!!! Please leave a checkbox or something else then.
Did you do it now?    """

__thank_you_for_check = """
\033[92mThank you, very much appreciated.
Now, let's move on to the next part..."""

__puzzle_message = """
\033[94mFollow the instructions in the following piece of text to get your reward.
Oh, it has been encrypted. :grinning-face:
So you will have to find the function to decode it..."""

def __decoder(text):
    '''Given a string, this function will decode it.'''
    if text:
        chars = string.ascii_letters
        encoding = {coded: encoded for coded, encoded in zip(chars, chars[::-1])}
        new_text = ""
        for c in text:
            new_text += encoding.get(c, c)
        if text[:10] == 'tIVZG DLIP':
            global check
            check = new_text[:10]
        return new_text
    else:
        return "Please give me some text to decode."

def decoder(text):
    '''Given a string, this function will decode it and print it
    out for you. So no need to do any prints or so. Just call the function.

    To pass a multi-line string, you will need to enclose it in triple quotes.
    Like this: \"\"\"A long multi-line
    piece of text.\"\"\"


    '''
    print(__decoder(text))

__puzzle_text_decoded = f"""
Great work {__user.capitalize()} !!!
You have decoded this message, and solved the first part of this puzzle.
Now, you can go to the second part to finally claim your reward:

Go on and find the function to submit your result to the game platform.
"""

__puzzle_text_encoded = f"""
tIVZG DLIP {__decoder(__user.capitalize())} !!!
bLF SZEV WVXLWVW GSRH NVHHZTV, ZMW HLOEVW GSV URIHG KZIG LU GSRH KFAAOV.
mLD, BLF XZM TL GL GSV HVXLMW KZIG GL URMZOOB XOZRN BLFI IVDZIW:

tL LM ZMW URMW GSV UFMXGRLM GL HFYNRG BLFI IVHFOG GL GSV TZNV KOZGULIN.
"""

__failed_one = "Sorry, you did not solve the first part of the puzzle. Try again."


def __imported():
    url = BASE_URI + "/imported/" \
                   + __decoder(__user.capitalize())
    requests.get(url).json()
    return


def submit():
    """Just run this function without any arguments.
    It will connect to the game platform in the cloud,
    and will tell you if you succeeded.

    """
    if check != "Great work":
        print(__failed_one)
        return
    url = BASE_URI + "/solved/" \
                   + check + '&' \
                   + __decoder(__user.capitalize())
    result = requests.get(url).json()
    if result['result'] == "Great work" and result['user'] == __user:
        print("Amazing, you did it. Now go claim your reward!")
    else:
        print("Nah, you didn't get there. Try again.")
    return


##################
## Main program ##
##################

print(__first_message)

__imported()

__answer = input(__message_on_import)

while __answer.upper() not in ["YES", "Y", "I DID", "YES!"]:
    __answer = input(__wait_for_check)

print(__thank_you_for_check)


# Showing the encrypted message
print(__puzzle_message)
print('\033[95m ' + __puzzle_text_encoded)
