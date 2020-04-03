
# Unemployment-Claims-Analysis
A simple python script to aggregate and display unemployment claims data

Dependencies:
  matplotlib
  datetime
  
Created in light of recent unemployment spike to compare it to historical data.
The script aggregates and displays the unemployment data by week (given in csv), month, and year. The reasoning behind this was to compare the recent one week spike with similar trends that may have occured over several months in previous recessions.

Data, ICNSA.csv, comes from the Federal Reserve Bank of St. Louis, and the current data can be found here: https://fred.stlouisfed.org/series/ICNSA

Graphs are created and saved as .png files to local directory when run.
Output graphs appear as follows:\
**By Week:**\
![](https://i.imgur.com/5g2Ntmp.png)\
**By Month:**\
![](https://i.imgur.com/F5HEQaP.png)\
**By Year:**\
![](https://i.imgur.com/oECfoDm.png)\
