import person_mod

# RegistrationStore is responsible for access to persistent
# collection of Registration records in the database.
class RegistrationStore():

    def __init__(self, db):
        self.db = db
        # access to persistent store of persons
        self.persons = person_mod.PersonStore(db)

    def deleteAll(self):
        """Remove all the registration records from the database."""
        self.db.execute("DELETE FROM REGISTRATION;", ())

    def countAll(self):
        rows = self.db.fetchAll("SELECT COUNT(*) FROM REGISTRATION;", ())
        return rows[0][0]

    def allRegistrations(self, tournament):
        rows = self.db.fetchAll(
            "SELECT id, player FROM REGISTRATION WHERE tournament=%s;", (tournament,))
        return rows

    def getNameById(self, tournament, id):
        rows = self.db.fetchAll(
            "SELECT player FROM REGISTRATION WHERE TOURNAMENT=%s AND ID=%s;", (tournament.id, id,))
        if len(rows) < 1:
            return None
        person = self.persons.getById(rows[0][0])
        return person.name

    def createRegistration(self, name, tournament):
        """create registration for person with name in tournament"""
        person = self.persons.getByName(name)
        if (person == None):
            self.persons.createPerson(name, None)
            person = self.persons.getByName(name)
        self.db.execute(
            "INSERT INTO REGISTRATION (PLAYER,TOURNAMENT) VALUES(%s,%s);", (person.id, tournament.id))

# Registration is responsible for properties of an
# individual registration of a player in a tournament.
# A player may register in multiple tournaments, so
# the unique registration id is used to identify the
# player in this tournament, but player attributes
# like name are still the responsibility of the 
# Person class.
class Registration():

    def __init__(self, id, player, tournament):
        self.id = id
        self.player = player
        self.tournament = tournament
