import sql

class TournamentStore():

    def __init__(self, db):
        self.db = db

    def deleteAll(self):
        """Remove all the records from the database."""
        self.db.execute("DELETE FROM TOURNAMENT;")

    def createTournament(self, name):
        """create new tournament"""
        insertStmt = "INSERT INTO TOURNAMENT (name, round) VALUES('%(name)s',0);" % {"name": name}
        self.db.execute(insertStmt)

    def getByName(self, name):
        result = self.db.fetchAll("SELECT * FROM TOURNAMENT;")
        print result
        result = self.db.fetchAll(
            "SELECT * FROM TOURNAMENT WHERE name=%(name)s;" % {"name":sql.string(name)})
        print result
        if len(result) == 1:
            row = result[0]
            tournament = Tournament(row[0], row[1], row[2])
            print tournament
            return tournament
        elif len(result) > 1:
            raise NameError("more than one tournament with name: '%(name)s';" % {"name":name})
        else:
            return None

    def recordScores(self, match):
        updateStmt = "UPDATE MATCH m SET m.SCORE1=%(score1), m.SCORE2=%(score2) WHERE m.id=$(match);" % {"score1": match.score1, "score2": match.score2, "match": match.id}
        self.db.execute(updateStmt)

class Tournament():

    def __init__(self, id, name, round):
        self.id = id
        self.name = name
        self.round = round


