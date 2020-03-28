import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

def byMonth(claims):
    """
    Aggregates claim data by month
    Args:
        claims: list of Claim objects. Must be sorted in ascending order.
            Modifies this list.
    """
    i = 0
    while(i < len(claims)-1):
        if claims[i].date.month == claims[i+1].date.month:
            claims[i].claims += claims[i+1].claims
            claims.remove(claims[i+1])
        else:
            i += 1

def byYear(claims):
    pass

def main():
    claimsList = parse("ICNSA.csv")
    byMonth(claimsList)
    dates = [claim.date for claim in claimsList]
    claimNumbers = [claim.claims for claim in claimsList]
    plt.plot(dates, claimNumbers)
    plt.xticks(rotation=90)
    plt.show()

main()