#Corey Monsma
#Python Challenge
#PyPoll main script
#April 2, 2023
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
# create varibles for procssing the input data including the data structure dictionary to hold the read in data.
            d_election_results = {}
 # set the counter variable to 0           
            total_votes = 0
            cc_total_votes = 0
            dd_total_votes = 0
            rad_total_votes = 0
            cc_percent = 0
            dd_percent = 0
            rad_percent = 0
            cc_name = 'Charles Casper Stockham'
            dd_name = 'Diana DeGette'
            rad_name = 'Raymon Anthony Doane'
            result_list = []
            winner_name = ''            
            for row in csvreader:
#because we know the data format we can hardcode the columns and do other conidtions when things are unstructured we have to use a different method.
                total_votes += 1
# who is the vote for ?
                if( str(row[2]) == cc_name ):
                    cc_total_votes += 1
                elif (str(row[2]) == dd_name):
                    dd_total_votes += 1
                elif(str(row[2]) == rad_name):
                    rad_total_votes += 1
# store the key information in a dictionary structure.                    
            d_election_results[cc_name] = cc_total_votes
            d_election_results[dd_name] = dd_total_votes
            d_election_results[rad_name] = rad_total_votes
#calculate the % of votes won
            cc_percent = ( cc_total_votes / total_votes ) * 100
            dd_percent = ( dd_total_votes / total_votes ) * 100
            rad_percent = ( rad_total_votes / total_votes ) * 100
# format the percents into a cleaner number            
            cc_percent = format(cc_percent,".3f")
            dd_percent = format(dd_percent,".3f")
            rad_percent = format(rad_percent,".3f")
# compare the results to find the winner.
            result_list.append(cc_percent)
            result_list.append(dd_percent)
            result_list.append(rad_percent)
#sort the list and then compare the top one with the candidates % to determin the winner
            result_list.sort(reverse=True)
            if (result_list[0] == cc_percent):
                winner_name = cc_name
            elif( result_list[0] == dd_percent):
                winner_name = dd_name
            else:
                winner_name = rad_name
#print out the results to the screen
            print('Election Results\n')
            print('-------------------\n')
            print(f'Total Votes: {str(total_votes)}\n')
            print('-------------------\n')
            print(f'Charles Casper Stockham: {str(cc_percent)} % ( {str(d_election_results[cc_name])} )\n')
            print(f'Diana DeGette: {str(dd_percent)} % ( {str(d_election_results[dd_name])} ) \n')
            print(f'Raymon Anthony Doane: {str(rad_percent)} % ( {str(d_election_results[rad_name])} ) \n')
            print('-------------------\n')
            print(f'Winner: {winner_name}\n')
            print('-------------------\n')
#write to the file
            # start writing the key varibles and string text to our file.
# Open the file using "write" mode. Specify the variable to hold the contents
        # Specify the file to write to
        output_path = os.path.join("", "analysis", "results.txt")
        with open(output_path, 'w') as file:
           file.write('Election Results\n-------------------\nTotal Votes: ')
           file.write(f'{str(total_votes)}\n-------------------\n')
           file.write(f'Charles Casper Stockham: {str(cc_percent)} % ( {str(d_election_results[cc_name])} )\n')
           file.write(f'Diana DeGette: {str(dd_percent)} % ( {str(d_election_results[dd_name])} ) \n')
           file.write(f'Raymon Anthony Doane: {str(rad_percent)} % ( {str(d_election_results[rad_name])} ) \n')
           file.write('-------------------\n')
           file.write(f'Winner: {winner_name}\n-------------------\n')


    return 1
                                

#end of the function##################################################################################

#Set the variable for relative path to blank so the program can find the files
relativeP = ""
exe = 0
exe = main(relativeP,"Resources","election_data.csv")
