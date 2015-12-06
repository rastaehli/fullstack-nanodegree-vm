import psycopg2
import pdb

class DB():

    def __init__(self, dbname):
        self.dbname = dbname

    def connect(self):
        """Connect to the PostgreSQL database.  Returns a database connection."""
        pdb.set_trace()
        try:
            return psycopg2.connect("dbname=%s" % self.dbname)
        except:
            print "unable to connect to %s" % self.dbname

    def execute(self, sql, params):
        print sql
        cur = self.connect().cursor()
        result = cur.execute(sql, params)
        print result

    def fetchAll(self, sql, params):
        print sql
        cur = self.connect().cursor()
        cur.execute(sql, params)
        return cur.fetchall()
