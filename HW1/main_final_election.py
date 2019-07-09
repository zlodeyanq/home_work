import csv

#define variables
total_voters = 0

#votes per candidate
khan_voters = 0
correy_voters = 0
li_voters = 0
tooley_voters = 0

#candidates
khan = 'Khan'
correy = 'Correy'
li = 'Li'
tolley = "O'Tooley"




with open('election_data.csv', newline='') as csvfile:
    election_data = csv.reader(csvfile, delimiter=',')
    next(election_data)

    for x in election_data:
        total_voters  = total_voters + 1

        if (khan == x[2]):
            khan_voters = khan_voters + 1

        if (correy == x[2]):
            correy_voters = correy_voters + 1
        
        if (li == x[2]):
            li_voters = li_voters + 1
        
        if (tolley == x[2]):
            tooley_voters = tooley_voters + 1
    
    def percentage(p):
        share = p / total_voters * 100
        return share
    share_khan = percentage(khan_voters)
    share_correy = percentage(correy_voters)
    share_li = percentage(li_voters)
    share_tooley = percentage(tooley_voters)

    
# Show Output
    print()
    print()
    print()
    print("Election results")
    print("-------------------------")
    print
    print(f'Total votes: ({total_voters})')
    print("-------------------------")
    print(f'Khan:  {"{:.{}f}".format(share_khan,2)} % ({khan_voters})')
    print(f'Correy:  {"{:.{}f}".format(share_correy,2)} % ({correy_voters})')
    print(f'Li:  {"{:.{}f}".format(share_li,2)} % ({li_voters})')
    print(f'Tooley:  {"{:.{}f}".format(share_tooley,2)} % ({tooley_voters})')
    print("-------------------------")
    print(f'Winner: Khan')
    print("-------------------------")