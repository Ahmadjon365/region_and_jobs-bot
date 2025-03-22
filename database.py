import sqlite3

class DataBase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()
    
    def get_all_regions(self):
        self.cur.execute("SELECT * FROM regions")
        regions = dict_fetchall(self.cur)
        return regions

    def get_countries_by_region(self, region_id):
        self.cur.execute("SELECT * FROM countries WHERE region_id=?", (region_id,))
        countries = dict_fetchall(self.cur)
        return countries

    def get_all_jobs(self):
        self.cur.execute("SELECT * FROM jobs")
        jobs = dict_fetchall(self.cur)
        return jobs
    
    def get_job_by_id(self, job_id):
        self.cur.execute("SELECT min_salary, max_salary FROM jobs WHERE job_id=?", (job_id,))
        job = dict_fetchall(self.cur)
        return job
    
    def get_country_by_id(self, country_id):
        self.cur.execute("SELECT flags FROM countries WHERE country_id=?", (country_id,))
        country = dict_fetchall(self.cur)
        return country



def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    print(columns)
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

    # desc = cursor.description
    # return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
