import matplotlib.pyplot as plt
import datetime

class Claim:

    def __init__(self, dateString, claims):
        """
        Holds data for a week of claim data.
        Args:
            dateString (String): String representing the date. Format follows YYYY-MM-DD
            claims (int): number of initial unemployment claims for that week
        """
        #convert dateString into datetime object
        dateString = dateString.split('-')
        self.date = datetime.datetime(int(dateString[0]), int(dateString[1]), int(dateString[2]))
        self.claims = int(claims)

    def __str__(self):
        return "Date :" + str(self._date) + "\nClaims: " + str(self._claims)

def parse(fname):
    """
    Parses unemployment document from federal reserve.
    Args:
        fname (String): name of file
    Returns:
        List of Claim objects from file, in increasing order by date
    """
    f = open(fname, 'r')
    f.readline() #skip first line
    lines = f.readlines()
    claims = []
    for line in lines:
        line = line.split(',')
        claims.append(Claim(line[0], line[1]))
    f.close()
    return claims

def aggregateData(claims, getAttr):
    """
    Helper function for byMonth and byYear
    Aggregates claim data by specified attribute dataFunc
    Args:
        claims: list of Claim object. Must be sorted in ascending order. Modifies this list
        getAttr (lambda function): returns the data attribute to be aggregate by (e.g. year, month)
            for a given Claims object
    """
    i = 0
    while(i < len(claims)-1):
        if getAttr(claims[i]) == getAttr(claims[i+1]):
            claims[i].claims += claims[i+1].claims
            claims.remove(claims[i+1])
        else:
            i += 1

def byMonth(claims):
    """
    Aggregates claim data by month
    Args:
        claims: list of Claim objects. Must be sorted in ascending order.
            Modifies this list.
    """
    aggregateData(claims, lambda claim: claim.date.month)


def byYear(claims):
    """
    Aggregates claim data by year
    Args:
        claims: list of Claim object. Must be sorted in ascending order
            Modifies this list
    """
    aggregateData(claims, lambda claim: claim.date.year)


def saveGraph(claimsList, title):
    """
    Plots and saves a graph for the data to local directory
    Args:
        claimsList: list of Claims objects to be displayed on graph
        title: String of graph title. Graph is save as title.png
    """
    plt.cla() #ensure graph is clean before working with it
    dates = [claim.date for claim in claimsList]
    claimNumbers = [claim.claims for claim in claimsList]
    plt.plot(dates, claimNumbers)
    plt.title(title)
    plt.xticks(rotation=90)
    plt.savefig(title)
    plt.cla() #clean up graph

def main():
    claimsList = parse("ICNSA.csv") #loads in data
    #plot weekly data
    saveGraph(claimsList, "Weekly Unemployment Data")
    #aggregate by month and plot monthly data
    byMonth(claimsList)
    saveGraph(claimsList, "Monthly Unemployment Data")
    #aggregate by year and plot yearly data
    byYear(claimsList)
    saveGraph(claimsList, "Yearly Unemployment Data")

main()
