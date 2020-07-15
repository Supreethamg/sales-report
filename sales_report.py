"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
#Open the sales report file
f = open('sales-report.txt')
#iterate througgh each line in the file
for line in f:
    #Remove tailing space from the word
    line = line.rstrip()
    #Split the line into list of words
    entries = line.split('|')

    #get sales person and melons sold from the list
    salesperson = entries[0]
    melons = int(entries[2])

    #Check if the salesperson is already in salespeople list
    if salesperson in salespeople:

        #get the position of salesperson in salespeople list
        position = salespeople.index(salesperson)
        #Add no of melons sold to that position in melons_sold list
        melons_sold[position] += melons
    else:
        #Add salesperson to salespeople list
        salespeople.append(salesperson)
        #Add melons number to melons_sold list
        melons_sold.append(melons)

#Print the report
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
