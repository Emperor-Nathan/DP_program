# DP_program
Program for selecting the user's optimal 2020 Democratic Primary preference.
## Usage
To use, you must install BeautifulSoup and TkInter.
## How it works
Each candidate receives a certain number of "points". For every issue that the user agrees with a candidate on, the candidate receives 1 point. If the user and candidate disagree, then the candidate loses 1 point. The total number of ideological points is then multiplied by the user's preference level for ideology divided by the default (which is the total number of issues).
Categories of issues can also have certain preference levels. A category's preference level indicates how many points are added/subtracted for each issue in that category.
Then comes experience. The default experience multiplier is the maximum experience of any candidate minus the minimum.
After that comes age, location, and veracity of statements.
