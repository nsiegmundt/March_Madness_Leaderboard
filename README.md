# March Madness Leaderboard

## Overview

The March Madness Learboard application lets you view a constantly updating leaderboard of the current standings of each player in your Bracket Challenger group for a specific day. This can come in handy when you just want to know who is winning in the ESPN bracket challenge for a specific day for something like a watch party

## Running the Application

- Make sure you have python 3 or later installed
- clone this repository
- change your directory to the root of the `March_Madness_Leaderboard` folder
- run `pip install -r requirements.txt`
- update the global variable `groupName` at the top of the `MMP.py` file to your ESPN bracket challenge group name
- Right before the games start on the day you want to view the leaderboard for, run `python MMP.py` and go to `http://localhost:5000` in your browser (firefox or chrome)
