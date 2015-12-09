
# TournamentStore is responsible for access to a persistent 
# collection of Tournament records in the database.
class TournamentStore():

    def __init__(self, db):
        self.db = db

    def deleteAll(self):
        """Remove all the records from the database."""
        self.db.execute("DELETE FROM TOURNAMENT;", ())

    def createTournament(self, name, registrations, matches, players):
        """create new tournament"""
        self.db.execute(
            "INSERT INTO TOURNAMENT (name, round) VALUES(%s,0);", (name,))
        result = self.db.fetchAll(
            "SELECT id FROM TOURNAMENT WHERE name=%s;", (name,))
        id = result[0][0]
        return Tournament(id, name, 0, registrations, matches, players)

    def getByName(self, name):
        result = self.db.fetchAll(
            "SELECT * FROM TOURNAMENT WHERE name=%s;", (name,))
        if len(result) == 1:
            row = result[0]
            tournament = Tournament(
                row[0], row[1], row[2], registrations, matches)
            return tournament
        elif len(result) > 1:
            raise NameError("more than one tournament with name: %s" % name)
        else:
            return None
    

# Tournament is responsible for access to attributes of a tournament
# including the relationshipes between players, registrations, matches
# and so forth.
class Tournament():

    def __init__(self, id, name, round, registrations, matches, players):
        self.id = id
        self.name = name
        self.round = round
        self.registrations = registrations
        self.matches = matches
        self.players = players

    def recordOutcome(self, winner, loser):
        self.matches.recordOutcome(self, winner, loser)

    def swissPairings(self):
        """Returns a list of pairs of players for the next round of a match.

        Assuming that there are an even number of players registered, each player
        appears exactly once in the pairings.  Each player is paired with another
        player with an equal or nearly-equal win record, that is, a player adjacent
        to him or her in the standings.

        Returns:
          A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name
        """
        standings = self.matches.tallyWins(self)
        standings = sorted(standings, key=getWins)
        pairings = []
        player1 = None
        for s in standings:
            if player1 == None:
                # remember first player for next pairing
                player1 = (s[0], s[1])
            else:
                # create pairing with second player
                pairings.append((player1[0], player1[1], s[0], s[1]))
                player1 = None
        return pairings

    def playerStandings(self):
        return self.matches.tallyWins(self)

def getWins(standingTuple):
    # tuple structure is (id,name,wins,matches)
    return standingTuple[2]
