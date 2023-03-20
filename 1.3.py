ticket = int(input())
ticket_smash = [int(a) for a in str(ticket)]
summ_1 = ticket_smash[0] + ticket_smash[1] + ticket_smash[2]
summ_2 = ticket_smash[3] + ticket_smash[4] + ticket_smash[5]
if summ_1 == summ_2:
    print('yes')
else:
    print('no')