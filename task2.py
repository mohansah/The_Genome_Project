import mysql.connector as mc

# Open database connection
try:
    db = mc.connect(
      host="localhost",
      user="root",
      passwd="",
      database="s_engineering")
    print("Database Connected Successfully")
except:
    print("Database Not Connected")

with open("Output1.txt","r") as f:
    lines=f.read().split("\n")

# prepare a cursor object using cursor() method
cursor = db.cursor()

for i in range(1,len(lines)):
    data=lines[i].split('\t\t')
    SI_No=int(data[0])
    Gene_Info=data[1]
    Gene_Seq=data[2]
    Count_A=data[2].count('A')
    Count_T=data[2].count('T')
    Count_G=data[2].count('G')
    Count_C=data[2].count('C')
    Length=Count_A+Count_T+Count_G+Count_C
    GC_Per=(Count_G +  Count_C)*100/(Count_A + Count_T+ Count_G+ Count_C)

    # Prepare SQL query to INSERT a record into the database.
    sql='INSERT INTO se VALUES({},"{}","{}",{},{},{},{},{},{})'.format(SI_No, data[1], data[2], Count_A, Count_T, Count_G, Count_C, Length, GC_Per)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        print("Inserted")
    except:
        # Rollback in case there is any error
        print("Error")
        db.rollback()

# disconnect from server
db.close()
