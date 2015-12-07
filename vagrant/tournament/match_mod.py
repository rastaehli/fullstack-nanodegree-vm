class MatchStore():

    def __init__(self, db):
        self.db = db

    def deleteAll(self):
        """Remove all the match records from the database."""
        self.db.execute("DELETE FROM MATCH;", ())

    def allMatches(self, tournament):
        rows = self.db.fetchAll("SELECT p1, score1, p2, score2 FROM MATCH WHERE TOURNAMENT=%s AND ROUND=%s;", (tournament.id,tournament.round,))
        matches = []
        for row in rows:
            matches.append(self.matchFromRow(tournament,row))
        return matches

    def matchFromRow(self,tournament,row):
        match = Match(tournament,row[0],row[2])
        match.score1 = row[1]
        match.score2 = row[3]
        return match

    def getByPlayers(self, tournament, player1, player2):
        query = "SELECT p1, score1, p2, score2 FROM MATCH WHERE tournament=%s AND round=%s AND p1=%s AND p2=%s;"
        rows = self.db.fetchAll(query, (tournament.id, tournament.round,player1,player2,))
        if len(rows) < 1:
            rows = self.db.fetchAll(query, (tournament.id, tournament.round,player2,player1,))
            if len(rows) < 1:
                return None
        return self.matchFromRow(tournament,rows[0])

    def createMatch(self, tournament, player1, player2):
        """create match in current tournament round between player 1 and 2"""
        match = Match(tournament, player1, player2)
        self.db.execute("INSERT INTO MATCH VALUES (%s,%s,%s,null,%s,null);", (match.tournament,match.round,match.p1,match.p2,))
        return match

    def recordOutcome(self, tournament,winner,loser):
        match = self.getByPlayers(tournament,winner,loser)
        if match==None:
            match = self.createMatch(tournament,winner,loser)
        if match.p1==winner:
            match.score1=1
            match.score2=0
        else:
            match.score1=0
            match.score2=1
        self.recordScores(match)

    def recordScores(self, matchUpdate):
        query = "UPDATE MATCH SET SCORE1=%s, SCORE2=%s WHERE TOURNAMENT=%s AND ROUND=%s AND P1=%s AND P2=%s;"
        self.db.execute(
            query, (
                matchUpdate.score1, 
                matchUpdate.score2, 
                matchUpdate.tournament, 
                matchUpdate.round, 
                matchUpdate.p1, 
                matchUpdate.p2,))


class Match():

    def __init__(self, tournament, player1, player2):
        self.tournament = tournament.id
        self.round = tournament.round
        self.p1 = player1
        self.score1 = None
        self.p2 = player2
        self.score2 = None

