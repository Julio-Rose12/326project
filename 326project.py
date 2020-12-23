import pandas as pd
import sys
from argparse import ArgumentParser


class Footballcalculator:  
    """ This class will read data on football stats and return the stats as well as the winner 
    for a given year.
    
    
    file(str): A file containing statistics regarding Super Bowl games
    year (int): The year to draw the winner from 
        
    """
    def __init__(self, file):
        df = pd.read_csv(file)
        self.dictionary = df.to_dict(orient = "index")
        self.dictionary2 = df.to_dict()

        
 
    def get_winner(self, year):
        """  Returns which team won the Superbowl game according to year. 
    
    
        Args:
            Year (int): Which year of the superbowl
        Returns:
            winner(str): Name of the team who won the game for the given year 
            and the division they belong to.
        """
        single_year_stats = self.stat_dic_by_year(year)
        winner = single_year_stats['Division, Winner']
        print(winner) 
    
    def average_stats_winner(self):
        """ Calculate the averages of all important statistics for past Super Bowl winning Quarterbacks.
        
        
        Args: 
            self:
    
        Returns: 
            average winner statistics (int) : return an integer representing the average for all of the important
            winning Quarterback statistics 
        """
 

        winningqbrdict = self.dictionary2['QBR']
        averagewinningQBR = round(sum(winningqbrdict.values()) / float(len(winningqbrdict.values())), 1)
        print("Average winning Quarterback Rating: " + str(averagewinningQBR))

        winningyardsdict = self.dictionary2['Yards']
        averagewinningyards = sum(winningyardsdict.values()) / float(len(winningyardsdict.values()))
        print("Average winning Passing Yards: " + str(averagewinningyards))

        winningTDsdict = self.dictionary2['TDs']
        averagewinningTDs = sum(winningTDsdict.values()) / float(len(winningTDsdict.values()))
        print("Average winning Passing Touchdowns: " + str(averagewinningTDs))

        winningINTsdict = self.dictionary2['Ints']
        averagewinningINTs = sum(winningINTsdict.values()) / float(len(winningINTsdict.values()))
        print("Average winning Interceptions: " + str(averagewinningINTs))
         
         
    def average_stats_loser(self):
    
         """ Calculate the averages of all important statistics for past Super Bowl winning Quarterbacks.
        
        
         Args: 
            Self:
    
         Returns: 
             average loser statistics (int) : return an integer representing the average for all 
             of the important
             losing Quarterback statistics
         """ 
        
         losingqbrdict = self.dictionary2['QBR1']
         averagelosingQBR = round(sum(losingqbrdict.values()) / float(len(losingqbrdict.values())), 1)
         print("Average losing Quarterback Rating: " + str(averagelosingQBR))

         losingyardsdict = self.dictionary2['Yards1']
         averagelosingyards = sum(losingyardsdict.values()) / float(len(losingyardsdict.values()))
         print("Average losing Passing Yards: " + str(averagelosingyards))

         losingTDsdict = self.dictionary2['TDs1']
         averagelosingTDs = sum(losingTDsdict.values()) / float(len(losingTDsdict.values()))
         print("Average losing Passing Touchdowns: " + str(averagelosingTDs))

         losingINTsdict = self.dictionary2['Ints1']
         averagelosingINTs = sum(losingINTsdict.values()) / float(len(losingINTsdict.values()))
         print("Average losing Interceptions: " + str(averagelosingINTs))
    

    def stat_dic_by_year (self, year ):
        """extracts one dictionary from the collection of nested dictionaries based on year.
    
        Arguments:
            year: The year you want statistics from
        
        returns:
            A single dictionary containg stats for the superbowl game of a specific year
        """
        for i in self.dictionary.values():
            if i['Year']== 2012:
                single_year_stats = i
        return single_year_stats
        print (single_year_stats)


def parse_args(arglist):
    """Parse Quaterback statistics from oppsing teams in the Super Bowl.
    
    
    Args:
        arglist (list of str): list of statistics from oppsing teams in the Super Bowl
    Returns:
        namespace: the parsed arguments, as returned by
        argparse.ArgumentParser.parse_args().
    """
    
    parser = ArgumentParser()
    parser.add_argument('file', type = str, help = 'file containing data') 
    parser.add_argument('year', type = int , help = 'What year to get data from') 
    return parser.parse_args(arglist)  
     
if __name__ == "__main__" : 
    args = parse_args(sys.argv[1:])
    f = Footballcalculator(args.file)
    print (f'The winner for the {args.year} superbowl is')
    f.get_winner(args.year)
    print ("here are the average statistics for the winning team during the last 10 superbowls")
    f.average_stats_winner()
    print ("here are the average statistics for the losing team during the last 10 superbowls")
    f.average_stats_loser()