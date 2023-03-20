ticket = int(input())
ticket_smash = [int(a) for a in str(ticket)]
summ_1 = ticket_smash[0] + ticket_smash[1] + ticket_smash[2]
summ_2 = ticket_smash[3] + ticket_smash[4] + ticket_smash[5]
s = 'yes' if summ_2 == summ_1 else 'no'
print(s)