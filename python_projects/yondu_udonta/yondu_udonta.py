'''
Project Name: Yondu_Udonta
Author: Sam Oblad
Due Date: 05/20/2022
Course: CS1400-x02

Problem

  Expected duration: 2-3 hours
  Yondu Udonta and his crew of space pirates arrive at the Iron Lotus after several weeks of plundering the high seas.
  Since the crew has been in space for nearly six months, they are ready for a night of celebration.
  Yondu doesn't want to divvy up the plunder just yet, so he gives each crew member other than himself
  and Peter Quill 3 units and sends them off to the Iron Lotus. (We're keeping the units simple for purposes of the problem,
  even though 1 unit is about $2.33.) After the crew has gone, he and Peter count what's left and decide how to split it up among the crew.
  Yondu takes 13% plunder, which he transfers to a hidden bank account. Yondu gives Peter 11% of the remaining units,
  which Peter transfers to his account. The next morning, the remaining units are divided evenly among all of the crew, including Yondu and Quill.
  Little do they know that Yondu and Quill have already taken a cut. If the remaining treasure can't be split evenly, the units left over are given
  to the Reaver's Benevolent Fund (RBF).
  The problem is to compute how many units each person gets and how how much goes to the RBF. A unit cannot be split, so if some calculation yields
  a number that contains a fractional part, you can only give that person the integer part of the value. For example, if your program computed the
  captain's share as 25.67 units, you could only give him 25 units, not 25.67 units. Warning: Always round down, NOT up.
  Simply drop the fractional part, but don't lose any units from the overall total amount.
  It should ask a user for two pieces of information:
  How many units the Reavers came into port with, and
  How many pirates are on the ship, including Yondu and Quill
  The program should then split the units and print out

  Yondu's share
  Peter's share
  The Crew share
  RBF Amount
'''

def main():
    '''
    Program starts here.
    '''
    try:
        print('Avast ye!, How many Reavers there be?')
        reavers = int(input())
        print('Yarr! How much booty came back with ye across the briney deep?')
        units = int(input())

    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    shore_leave = ((reavers - 2) * 3)
    units = units - shore_leave

    yondu_share = int(units * 0.13)
    units = units - yondu_share

    quill_share = int(units * 0.11)
    units = units - quill_share

    crew_members_share = int(units/reavers)

    yondu_share = yondu_share + crew_members_share
    quill_share = quill_share + crew_members_share

    units = units - (crew_members_share * (reavers))
    rbf_fund = units

    print(f"Total Shore Leave: {shore_leave} units")
    print(f"Yondu's Share: {yondu_share} units")
    print(f"Peter's Share: {quill_share} units")
    print(f"Each Crew member will recieve: {crew_members_share} units")
    print(f"The RBF will recieve the remaining: {rbf_fund} units")


if __name__ == "__main__":
    main()
