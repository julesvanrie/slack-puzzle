This little puzzle was used during my lectures to

- Remind students in a friendly way to keep an eye on our Slack channels
- Remind them of how useful the Tab and Shift-Tab commands in Jupyter Notebook are
- To link to the announcement of a little coding tournament and our
participation to the Advent of Code


# What it does

1. Students receive a message on Slack with the request to import the attached `fixchallenge.py` and import it in their Jupyter Notebook, and put a :check: to mark that they have read the message (encourage good practice).
2. Upon import of the module, students are asked if they indeed put the :check: in the Slack message. If not, they are requested to do so.
3. Next, they can move on to the next part, where they are confronted with a little puzzle: they see some text that needs to be encrypted.
4. They can solve the puzzle by just using a function that is available in the module.
5. Once solved, they know they can submit their results, and then go claim their reward.


# How it works

## fixchallenge.py

This is the module to be imported by students in their notebook.

Structure does not follow good coding conventions on purpose. Main requirement was to have everything in one file. Furthermore, I wanted some code to be executed upon import:

- Make an API call to the back-end to track who had imported it (so I could - manually - check if they had put a :check: on Slack).
- Start asking questions to students

Students can then use the `decoder` and `submit` function to solve the puzzle.


## wsgi.py

A small back-end app to follow if students have imported and solved the puzzle.
- Using Flask with two endpoints:
    - `BASE_URI/imported/<user>`
    - `BASE_URI/solved/<check>&<user>`
- The back-end was set-up using a free dyno on Heroku (when that free walhalla still existed).
- Logging was followed with Papertrail add-on. Filtering on `just` limits the logs to only relevant messages.


## Other files

All these are the classic configuration files


# The message on Slack to start it

> Hi @here,<BR><BR>
You need to make a quick fix while working on the second challenge.<BR>
Copy this little file in the challenge folder, and create a new jupyter notebook in the same folder.<BR>
Run the following command in an empty cell, and follow the guidance from there:<BR>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```import fixchallenge``` <BR>
Teachers don't need this fix.<BR>
Please react with a little :check: to this message when you have read it.


# Potential improvements

- Input requests in a notebook running in VS Code are less clear
- Tab and Shift-Tab seem to work differently in VS Code
- Tracking if students have put a :check: on Slack
- Give some hint that they can use everything in the module file to solve the puzzle (discovering through Tab and Shift-Tab)
- Some kind of leaderboard on the online platform.
