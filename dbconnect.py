from MySQLdb import _mysql

def connection():
    db = _mysql.connect(host="localhost", user="root", passwd="password", db="thoughtsweb_db")
    return db

def fetch_thoughts():
    db = connection()
    db.query("select body from thoughts where display_date = CURDATE()")
    results = db.store_result()
    return results.fetch_row()

def submit_thoughts_db(thought):
    print(thought)
    db = connection()
    query_str = 'insert into thoughts values(null,"'+thought+'",CURDATE())'
    db.query(query_str)
