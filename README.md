# Election_Analysis
## Overview of Election Audit 
I was to assist a Colorado Board of Elections employee in auditing the tabulated results for a recent Colorado local congressional election. I was tasked to: 
1. calculate the total number of votes cast. 
2. get a complete list of candidates who received votes.
3. calculate the total number of votes each candidate received.
4. calculate the percentage of votes each candidate won.
5. determine the winner of the election based on popular vote.
The goal here is to automate the process using Python so that the code can be used to audit not only other congressional districts, but senatorial districts and local elections. In this project, some additional data has been requested of me to complete the audit. I will be providing additional data on:
1.The voter turnout for each county
2.The percentage of votes from each county out of the total count
3.The county with the highest turnout
After the analysis, a vote count report will be generated to certify the election results.

## Resources 
- Data Source: election_results.csv
- Software: Python 3.10.4, Visual Studio Code, 1.67.2

## Chalenge Overview

In carrying out this analysis, I began by initializing an empty county list called counties that would hold the names of the counties.I also initialized an empty dictionary called county_votes that would hold the county as the key and the votes cast for each county as the values.To hold the county name for the county with the largest turnout, I initiallized an empty string "largest_county". The variables "largest_count" and "largest_percentage" were initialized to hold the number of votes of the county that had the largest turnout and the percentage voter turnout of the county respectively.

In the already created for loop, a script was created to get the county name from each row. A decision statement was created to check if teh county name acquired using the for loop is already in the counties list using the code below:

provide a description of the challenge here you can also add a description of your key findings 
also include a clearly written overview of your methodfs (this will help your audience understand what you did and what they might be able to do with the data you presented.)

``` VBA
    If Cells(i, 1).Value = tickers(tickerIndex) And Cells(i - 1, 1).Value <> tickers(tickerIndex) Then
            
             tickerStartingPrices(tickerIndex) = Cells(i, 6).Value
                
    End If
```

## Election-Audit Results 
The analysis of the election showed that: 

- The total number of votes casted in this congressional election was 369,711 votes.

- There were three counties in the precinct. They were: Jefferson, Denver and Arapahoe. Jefferson county had 38,855 votes which represents 10.5%,
Denver county had 306,055 votes which represents 82.8%, and Arapahoe county had 24,801 votes which represents 6.7%.

- Denver county had the largest number of votes of 306,055 (82.8%).

- There were three candidates in this election. Below is a breakdown of their votes and percentage of the total votes each candidate received.
  1. Charles Casper Stockham received 85,213 votes which is 23.0 %  of the votes.
  2. Diana DeGette received  272,892 votes which is 73.8 % of the votes.
  3. Raymon Anthony Doane received 11,606 votes which is 3.1 % of the votes.

- The winner of the election was Diana DeGette, who received 272,892 number of votes representing 73.8 % of total votes cast.


## Election-Audit Summary 
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
This code can be modified and used for any election.
The code can be modified by:
1.
2. 














