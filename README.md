# Election_Analysis
Analysis using Python

## Overview of Project
**Assist a Colorado Board of Elections employee to perform an election audit of a recent local congressional election.**

**The Analysis should include the following information:**
1. The total number of votes cast
2. The voter turnout for each county
3. The percentage of votes from each county out of the total count
4. The county with the highest turnout
5. A complete list of candidates who received votes
6. The percentage of votes each candidate won
7. The total number of votes each candidate won
8. The winner of the election based on popular vote

## Resources
- Data Source: [election_results.csv](Resources/election_results.csv)
- Source Code: [PyPoll_Challenge](PyPoll_Challenge.py)
- Analysis Results: [election_analysis.txt](analysis/election_analysis.txt)
- Software: Python 3.8.3 64-bit (conda); Visual Studio Code 1.52.0

## Summary
- **There were 369,711 votes cast in the congressional election.**
- *The list of counties and the voter turnout in those counties:*
    - Jefferson County, voter turnout was 10.5% of total votes and 38,855 number of votes cast in this county.
    - Denver County: voter turnout was 82.8% of total votes and 306,055 number of votes cast in this county.
    - Arapahoe County: voter turnout was 6.7% of total votes and 24,801 number of votes cast in this county.
- *The county with the highest number of votes was:*    
    - Denver County
- *The candidates were:*
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- *The results for each candidate were:*
    - Charles Casper Stockham received 23.0% of the total vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the total vote and 272,892 number of votes.
    - Raymon Anthony Doane 3.1% of the total vote and 11,606 number of votes.
- *The winner of the election was:*
    - Diana DeGette, who received 73.8% of the total vote and 272,892 number of votes.
    
### Election-Audit Summary:
The current Python script that was used to perform the congressional election audit could be re-used with minor modifications in the future elections.  

**Some Examples:**
1. State-wide election tracking and audit (to enhance reporting add party column to track party affiliation of each candidate)
2. By adding year column to the dataset, this script could be used to compare results of two consecutive elections to compare voter turnout by county. This could be used for planning purposes to encourage voters in counties that have declining trend of voter turnout.

