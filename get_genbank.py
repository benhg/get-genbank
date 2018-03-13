import os
import subprocess
import time
databases_list = open("genbank_list.txt").readlines()

for database in databases_list:
    time.sleep(2.5)
    database = database.strip()
    db_name = "".join(x for x in database if x.isalpha())
    if not db_name in os.listdir('/home/users/glick/genbank'):
        os.makedirs('/home/users/glick/genbank/{}'.format(db_name))
    os.popen("""cd {}
/home/users/glick/genbank/get_blast.pl --passive {} --decompress""".format(db_name, database))
    


