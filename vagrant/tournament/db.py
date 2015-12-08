import psycopg2

# Convenience wrapper for database access via psycopg2.
# Responsible for opening/closing connections, managing 
# transactions.
class DB():

    def __init__(self, dbname):
        self.dbname = dbname

    def connect(self):
        """Connect to the PostgreSQL database.  Returns a database connection."""
        try:
            return psycopg2.connect("dbname=%s" % self.dbname)
        except:
            print "unable to connect to %s" % self.dbname

    def execute(self, sql, params):
        # print sql, params
        conn = self.connect()
        result = conn.cursor().execute(sql, params)
        conn.commit()
        conn.close()
        # print result

    def fetchAll(self, sql, params):
        # print sql, params
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(sql, params)
        resultRows = cur.fetchall()
        conn.commit()
        conn.close()
        return resultRows
