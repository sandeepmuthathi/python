import re
with open('/home/sandeep.m/Downloads/wordpress/wp-config.php') as fh:
    for line in fh.readlines():
        if "DB_NAME" in line:
            db=re.findall(r"'(\w+)'", line)
            print("DB name : {}".format(db[1]))
        elif "DB_USER" in line:
            dbu=re.findall(r"'(\w+)'", line)
            print("DB user : {}".format(dbu[1]))
        elif "DB_PASSWORD" in line:
            dbp=re.findall(r"'(.+?)'", line)
            print("DB password : {}".format(dbp[1]))
