#Corey Monsma
#Python Challenge
#PyBank main script
#March 30, 2023
#########################################################################
def main(pFile, pDName, pFName):
    import os #import the os library to use the given python framework
    import csv #import the csv library to use the give pyton framework
#tell python where the files are we processing the input files says were the files are    
    inputpath = os.path.join(pFile,pDName,pFName)
    if ( inputpath != None ):
        with open(inputpath) as inputfile:
            csvreader = csv.reader(inputfile, delimiter=',') #create cvs reader object per our class activity
#            print(csvreader)
            csv_header = next(csvreader) #next command deals with the header...ignore the header
            totalMonths = 0
            netTotal = 0
            profitChange = 0
            average = []
            monthList = []
            for row in csvreader:
# loop through the cvs file via the reader class
                totalMonths += 1
                netTotal += float(row[1])
                average.append(float(row[1]))
#keep a list of the months                
                monthList.append(row[0])
# loop through the float list of profit changes.
            listSize = len(average) - 1
            deltaProfitList = []
            deltaProfit = 0
            baseline = 0
            change = 0
            i = 0
            j = 1
            averageChange = 0
            MonthProfitDictionary = {}
#loop through the chane list and process the values into the desired questions for answers
            for x in average:
             if ( i < listSize ):
                baseline = average[i]
                change = average[j]
#next period was a loss                
                if ( baseline > change or (( baseline < change )) ):
#loss posted                   
                   deltaProfit = (baseline - change) * -1
                else:
                   deltaProfit = (baseline - change) 
# the change in profit will be used a the key for reterving the month it happened.
                MonthProfitDictionary[deltaProfit] = monthList[j]
#sum the change values                   
                averageChange += deltaProfit
#store all the change values in another list for referencing the largest and smallest change.                
                deltaProfitList.append(deltaProfit)
                i += 1
                j += 1
#get the months that are key... The one with the largest profit and loss.
        deltaProfitList.sort(reverse=True)
        profitChange = deltaProfitList[0]
        ProfitMonth = MonthProfitDictionary[profitChange]
        LossChange = 0
        deltaProfitList.sort()
        LossChange = deltaProfitList[0]
        LossMonth = ""
        LossMonth = MonthProfitDictionary[LossChange]
#format the dollar amounts into nnnn.nn
        netTotal = format(netTotal,'.2f')

#print out the information to the command line screen.
        print("Financial Analysis")
        print('\n')
        print("----------------------------------")
        print(f'Total Months: {str(totalMonths)}')
        print('\n')
        print(f'Total: ${str(netTotal)}')
        print('\n')
# the average change
        averageChange = averageChange/listSize 
        averageChange = format(averageChange,'.2f') #format the calculation into 123.11
        print(f'Average Change: ${str(averageChange)}')
        print('\n')
#the largest profit 
        profitChange = format(profitChange,'.2f')
        print(f'Greatest Increase in Profits: {ProfitMonth} ($ {str(profitChange)} )')
        print('\n')
#the greatest loss
        LossChange = format(LossChange,'.2f')               
        print(f'Greatest Decrease in Profits: {LossMonth} ($ {str(LossChange)} )')
#Write the key information to a text file.
# start writing the key varibles and string text to our file.
# Open the file using "write" mode. Specify the variable to hold the contents
        # Specify the file to write to
        output_path = os.path.join("", "analysis", "results.txt")
        with open(output_path, 'w') as file:
           file.write('Financial Analysis\n-------------------\nTotal Months: ')
           file.write(str(totalMonths))
           file.write(f'\nTotal: $ {str(netTotal)}')
           file.write(f'\nAverage Change: $ {str(averageChange)}')
           file.write(f'\nGreatest Increase in Profits: {ProfitMonth} (${str(profitChange)})')
           file.write(f'\nGreatest Decrease in Profits: {LossMonth} (${str(LossChange)})')
#
    return 1
#end of the function##################################################################################

#Set the variable for relative path to blank so the program can find the files
relativeP = ""
exe = main(relativeP,"Resources","budget_data.csv")
