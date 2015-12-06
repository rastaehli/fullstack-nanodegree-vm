class MatchStore():

    def __init__(self, db):
        self.db = db

    def deleteAll(self):
        """Remove all the match records from the database."""
        self.db.execute("DELETE FROM MATCH;")

    def createMatch(self, tournament, player1, player2):
        """create match in current tournament round between player 1 and 2"""
        match = Match(tournament, player1, player2)
        self.db.execute("INSERT INTO MATCH VALUES (%s,%s,%s,null,%s,null);", (match.tournament,match.round,match.p1,match.p2))
        return match

    def recordScores(self, match):
        updateStmt = "UPDATE MATCH m SET m.SCORE1=%(score1)i, m.SCORE2=%(score2)i WHERE m.id=%(match)i;" % {"score1": match.score1, "score2": match.score2, "match": match.id}
        self.db.execute(updateStmt)


class Match():

    def __init__(self, tournament, player1, player2):
        self.tournament = tournament.id
        self.round = tournament.round
        self.p1 = player1.id
        self.score1 = null
        self.p2 = player2.id
        self.score2 = null

