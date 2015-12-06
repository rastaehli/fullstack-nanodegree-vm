import standings

class TournamentStore():

    def __init__(self, db):
        self.db = db

    def deleteAll(self):
        """Remove all the records from the database."""
        self.db.execute("DELETE FROM TOURNAMENT;",())

    def createTournament(self, name, registrations, matches, players):
        """create new tournament"""
        self.db.execute("INSERT INTO TOURNAMENT (name, round) VALUES(%s,0);", (name,))
        result = self.db.fetchAll("SELECT id FROM TOURNAMENT WHERE name=%s;", (name,))
        id = result[0][0]
        return Tournament(id,name,0,registrations,matches,players)

    def getByName(self, name):
        result = self.db.fetchAll(
            "SELECT * FROM TOURNAMENT WHERE name=%s;", (name,))
        print result
        if len(result) == 1:
            row = result[0]
            tournament = Tournament(row[0], row[1], row[2], registrations, matches)
            print tournament
            return tournament
        elif len(result) > 1:
            raise NameError("more than one tournament with name: %s" % name)
        else:
            return None

    def recordScores(self, match):
        self.db.execute("UPDATE MATCH m SET m.SCORE1=%s, m.SCORE2=%s WHERE m.id=%s;" , (match.score1, match.score2, match.id))


class Tournament():

    def __init__(self, id, name, round, registrations, matches, players):
        self.id = id
        self.name = name
        self.round = round
        self.registrations = registrations
        self.matches = matches
        self.players = players

    def playerStandings(self):
        standingsMap = {}
        allRegistrations = self.registrations.allRegistrations(self.id)
        for reg in allRegistrations:
            standingsMap[reg[0]] = standings.Standings(reg[0])
        allMatches = self.matches.allMatches(self.id)
        for match in allMatches:
            p1Standings = standingsMap[match.p1]
            p2Standings = standingsMap[match.p2]
            if match.score1 > match.score2:
                p1Standings.tallyWin()
                p2Standings.tallyLoss()
            elif match.score1 == match.score2:
                p1Standings.tallyDraw()
                p2Standings.tallyDraw()
            else:
                p1Standings.tallyLoss()
                p2Standings.tallyWin()
        result = []
        for reg in allRegistrations:
            print 'registration: ', reg
            regId = reg[0]
            playerId = reg[1]
            player = self.players.getById(playerId)
            winTally = standingsMap[regId].winTally
            matchTally = standingsMap[regId].matchTally
            result.append( (regId, player.name, winTally, matchTally))
        return result
