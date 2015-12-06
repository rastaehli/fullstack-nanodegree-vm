
import person_mod
import sql

class RegistrationStore():

    def __init__(self, db):
        self.db = db
        self.persons = person_mod.PersonStore(db)  # access to persistent store of persons

    def deleteAll(self):
        """Remove all the registration records from the database."""
        self.db.execute("DELETE FROM REGISTRATION;")

    def countAll(self):
        rows = self.db.fetchAll("SELECT COUNT(*) FROM REGISTRATION;")
        return rows[0][0]

    def createRegistration(self, name, tournament):
        """create registration for person with name in tournament"""
        person = self.persons.getByName(name)
        if (person == None):
            person = self.persons.createPerson(name,None)
        self.db.execute("INSERT INTO REGISTRATION (PLAYER,TOURNAMENT) VALUES(%s,%s);", (person.id, tournament.id))


class Registration():

    def __init__(self, id, player, tournament):
        self.id = id
        self.player = player
        self.tournament = tournament
