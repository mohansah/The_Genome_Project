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

def Check_Gene_Info(Gene_Info):
    New_Gene_Info=Gene_Info.split(':')[0]
    lis0=Gene_Info.split(':')[1].split(' ')
    lis=lis0[0]
    if(not (',' in lis)):
        #print(lis)
        if(lis[0]=='c'):
            lis1=lis.split('-')
            #print(lis1[1]+'-'+lis1[0][1:])
            loc=lis1[1]+'-'+lis1[0][1:]
            New_Gene_Info+=':'+lis1[1]+'-'+lis1[0][1:]
        else:
            #print(lis)
            New_Gene_Info+=':'+lis
            loc=lis
        for j in range(1,len(lis0)):
            New_Gene_Info+=' '+lis0[j]
        return New_Gene_Info, 1, loc
    else:
        return Gene_Info, 0, '-'

def Info_From_GeneList_File():
    with open("GeneList.txt","r") as f:
        lines=f.read().split("\n")

    dist={}
    for i in range(3,len(lines)):
        lis=[]
        data=lines[i].split('\t')
        for j in range(1,len(data)):
            lis.append(data[j])
        dist[data[0]]=lis

    return dist

dist1={
 "TTT":"Phe",
 "TTC":"Phe",
 "TTA":"Leu",
 "TTG":"Leu",
 "CTT":"Leu",
 "CTC":"Leu",
 "CTA":"Leu",
 "CTG":"Leu",
 "ATT":"Ile",
 "ATC":"Ile",
 "ATA":"Ile",
 "ATG":"Met",
 "GTT":"Val",
 "GTC":"Val",
 "GTA":"Val",
 "GTG":"Val",
 "TCT":"Ser",
 "TCC":"Ser",
 "TCA":"Ser",
 "TCG":"Ser",
 "CCT":"Pro",
 "CCC":"Pro",
 "CCA":"Pro",
 "CCG":"Pro",
 "ACT":"Thr",
 "ACC":"Thr",
 "ACA":"Thr",
 "ACG":"Thr",
 "GCT":"Ala",
 "GCC":"Ala",
 "GCA":"Ala",
 "GCG":"Ala",
 "TAT":"Tyr",
 "TAC":"Tyr",
 "TAA":"Stop",
 "TAG":"Stop",
 "CAT":"His",
 "CAC":"His",
 "CAA":"Gln",
 "CAG":"Gln",
 "AAT":"Asn",
 "AAC":"Asn",
 "AAA":"Lys",
 "AAG":"Lys",
 "GAT":"Asp",
 "GAC":"Asp",
 "GAA":"Glu",
 "GAG":"Glu",
 "TGT":"Cys",
 "TGC":"Cys",
 "TGA":"Stop",
 "TGG":"Trp",
 "CGT":"Arg",
 "CGC":"Arg",
 "CGA":"Arg",
 "CGG":"Arg",
 "AGT":"Ser",
 "AGC":"Ser",
 "AGA":"Arg",
 "AGG":"Arg",
 "GGT":"Gly",
 "GGC":"Gly",
 "GGA":"Gly",
 "GGG":"Gly"}

dist2={
 "Ala": 'A',
 "Cys": 'C',
 "Asp": 'D',
 "Glu": 'E',
 "Phe": 'F',
 'Gly': 'G',
 'His': 'H',
 'Ile': 'I',
 'Lys': 'K',
 'Leu': 'L',
 'Met': 'M',
 'Asn': 'N',
 'Pro': 'P',
 'Gln': 'Q',
 'Arg': 'R',
 'Ser': 'S',
 'Thr': 'T',
 'Val': 'V',
 'Trp': 'W',
 'Tyr': 'Y'
}

def ProteinSequence(GeneSeq,dist1,dist2):
    ProSeq=""
    lastindex = len(GeneSeq) - 3
    for i in range(0,len(GeneSeq),3):
        #print(GeneSeq[i:i+3])
        ThreeLetterCode=dist1[GeneSeq[i:i+3]]
        if(ThreeLetterCode=="Stop"):
            if(i != lastindex):
                print("Warning : Stop Occur in Gene ",lis[3])
            OneLetterCode="Stop"
        else:
            OneLetterCode=dist2[ThreeLetterCode]
        ProSeq+=OneLetterCode

    return ProSeq


# prepare a cursor object using cursor() method
cursor = db.cursor()

dist=Info_From_GeneList_File()
for i in range(1,len(lines)):
    data=lines[i].split('\t\t')
    SI_No=int(data[0])

    New_Gene_Info, Flag, Location=Check_Gene_Info(data[1])

    if(Flag==1):
        #print(New_Gene_Info)

        Gene_Seq=data[2]
        Count_A=data[2].count('A')
        Count_T=data[2].count('T')
        Count_G=data[2].count('G')
        Count_C=data[2].count('C')
        Total_Length=Count_A+Count_T+Count_G+Count_C
        GC_Per=(Count_G +  Count_C)*100/(Count_A + Count_T+ Count_G+ Count_C)

        try:
            lis=dist[Location]
            y=1
        except:
            y=0
            print("Location Not Found")

        if(y):
            PS=""
            for x in data[2]:
                if(x!='\t'):
                    PS+=x
            if(len(PS)%3==0):
                ProSeq=ProteinSequence(PS,dist1,dist2)
                # Prepare SQL query to INSERT a record into the database.
                sql='INSERT INTO task4 VALUES({},"{}","{}",{},{},{},{},{},{},"{}","{}",{},{},"{}","{}","{}","{}","{}","{}")'.format(SI_No, New_Gene_Info, data[2], Count_A, Count_T, Count_G, Count_C, Total_Length, GC_Per, Location, lis[0], int(lis[1]), int(lis[2]), lis[3], lis[4], lis[5], lis[6], lis[7],ProSeq)
                try:
                    # Execute the SQL command
                    cursor.execute(sql)
                    # Commit your changes in the database
                    db.commit()
                    print("Inserted")
                except:
                    # Rollback in case there is any error
                    print("Error : Not Inserted")
                    db.rollback()


# disconnect from server
db.close()
