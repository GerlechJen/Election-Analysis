# Election_Analysis
## Overview of Election Audit 
I was to assist a Colorado Board of Elections employee in auditing the tabulated results for a recent Colorado local congressional election. Part of my task was to: 
1. calculate the total number of votes cast. 
2. get a complete list of candidates who received votes.
3. calculate the total number of votes each candidate received.
4. calculate the percentage of votes each candidate won.
5. determine the winner of the election based on popular vote.

The goal here is to automate the process using Python so that the code can be used to audit not only other congressional districts, but senatorial districts and local elections. 

In this project, some additional data has been requested of me to complete the audit. I will be providing additional data on:
1. the voter turnout for each county. 
2. the percentage of votes from each county out of the total count.
3. the county with the highest turnout.

After the analysis, a vote count report will be generated to certify the election results.

## Resources 
- Data Source: election_results.csv
- Software: Python 3.10.4, Visual Studio Code, 1.67.2

## Chalenge Overview

In carrying out this analysis, I began by initializing an empty county list called "counties" that would hold the names of the counties. I also initialized an empty dictionary called "county_votes" that would hold the county as the key and the votes cast for each county as the values. To hold the county name for the county with the largest turnout, I initiallized an empty string "largest_county". The variables "largest_count" and "largest_percentage" were initialized to hold the number of votes of the county that had the largest turnout and the percentage voter turnout of the county respectively.

In the already created for loop, a script was created to get the county name from each row. A decision statement was created to check if the county name acquired using the for loop is already in the counties list. If the county was not in the list, it was added to the counties list. The code below shows how this was executed.

``` python 
   if county_name not in counties:
            counties.append(county_name)
```
A script was then created that initializes the county vote to 0 to begin tracking the vote turnout of each county. Another script was created that adds a vote to the county’s vote count as all the rows are looped through.

A repetition statement was written to get the county from the county_votes dictionary. A variable, "vote_count" was initialized to hold the county’s votes as they are retrieved from the county_votes dictionary. Another script was created to calculate the county’s votes as a percentage of the total votes. The procedures stated were executed using the code below:


``` python 
   for county in county_votes:
        vote_count = county_votes[county]
        county_vote_percentage = (vote_count / total_votes)* 100
```

A print statement was created to print the current county, its percentage of the total votes, and its total votes to the command line.

A decision statement was created that determines the county with the largest vote count and then adds that county and its vote count to the largest_county and largest_count variables respectively.

A print statement that prints out the county with the largest turnout was written. 

A script was written that saves each county, the county’s total votes, and the county’s percentage of total votes to the election_results.txt file using the following code:

``` python 
   county_detailed_results = (f"{county}: {county_vote_percentage:.1f}%  ({vote_count:,})\n")
        txt_file.write(county_detailed_results)
```

Finally, a script that saves the county with the largest turnout was also written to the election_results.txt file as seen below:

``` python 
   largest_county_results = (
        "\n-------------------------\n"
        f'Largest County Turnout: {largest_county}\n'
        "-------------------------\n")
    txt_file.write(largest_county_results)
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
To the election commission, I would like to make these proposals which will make it possible to use the code for any election. I will also include some recommendations that would enhance the presented election results.

First of all, the Python Script can be refactored to accept generic csv files that are not hard coded named. A function could also be created to take in variables like county name and vote count and the refactored code placed under the function. This would be very efficient as we wouldn't have to perform the same long steps for every election.

In terms of enhancing the results of the election, a bar chart showing the counties and their voter turnout or the different candidates and their percentage of votes could be included. An additional touch would be a map of the colorado area with census data mapped over.


----

**Completed by:** Jennifer Anno-Kusi

**Email:** jannokusi@gmail.com 
