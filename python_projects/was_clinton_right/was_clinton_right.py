"""
Was_Clinton_Right.py
This program will deterimine if president clinton was correct in a speech
given in 2012: “Since 1961, for 52 years now, the Republicans have
held the White House 28 years, the Democrats 24. In those 52 years, our private
economy has produced 66 million private-sector jobs. So what`s the jobs score? Republicans
24 million,Democrats 42 (million).”This will be determined by using a data file
given from the Bureau of Labor Servicesto identify exact job creation amounts and
under whos leadership those creations occured.

By Sam Oblad
"""

import csv


def main():
    """
    takes two different csvs and extracts years, political parties, and employment growths
    and calculates how much employee growth during each year and who was in control """

    
    employment_growth = {}
    political_party_years = {}
    with open("employment_data.csv", 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skips header line in csv file
        for row in csvreader:
          employment_growth[row[0]] = str(int(row[-1]) - int(row[1])) # sets year equal to growth dict

    with open("Presidents.csv", 'r', encoding='utf-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skips header line in csv file
        for row in csvreader:
            # sets year equal to what party controlled the presidency in dict
            political_party_years[row[0]] = row[2]

    starting_year = 1961
    ending_year = 2012
    party_yearly_growth = {}
    year = str(starting_year)
    while True:
        party_yearly_growth[employment_growth[year]] = political_party_years[year]
        year = int(year)
        year += 1
        if year >= ending_year:
            break
        year = str(year)

    democrat_growth = 0
    republican_growth = 0
    party_yearly_growth = party_yearly_growth.items()
    for pair in party_yearly_growth:
        if pair[1] == 'Democrat':
            democrat_growth += (int(pair[0]) / 1000)
        elif pair[1] == 'Republican':
            republican_growth += (int(pair[0]) / 1000)

    print(
        f"Democratic Employee Growth {starting_year}-{ending_year}: {democrat_growth} million")
    print(
        f"Republican Employee Growth {starting_year}-{ending_year}: {republican_growth} million")


if __name__ == "__main__":
    main()
