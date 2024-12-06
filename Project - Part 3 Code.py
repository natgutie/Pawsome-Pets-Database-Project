# Anna Valente and Natalie Gutierrez
# Project Part 3

import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('project.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

#----------Create tables--------------
create_clinic_table = """
    CREATE TABLE IF NOT EXISTS Clinic(
    clinicNo INT not null,
    clinicName VARCHAR(100) not null,
    clinicAddress VARCHAR(50) not null,
    clinicPhoneNumber VARCHAR(11) not null,
    PRIMARY KEY(clinicNo)
    );
    """

create_staff_table = """
    CREATE TABLE IF NOT EXISTS Staff(
    staffNo INT not null,
    staffName VARCHAR(30) not null,
    staffAddress VARCHAR(50),
    staffDOB VARCHAR(10),
    staffPosition VARCHAR(30) not null,
    staffSalary INT not null,
    clinicNo INT not null,
    PRIMARY KEY(staffNo),
    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    );
    """

create_petowner_table = """
    CREATE TABLE IF NOT EXISTS PetOwner(
    ownerNo INT not null,
    ownerName VARCHAR(30) not null,
    ownerAddress VARCHAR(50),
    ownerPhoneNumber VARCHAR(11) not null,
    clinicNo INT not null,
    PRIMARY KEY(ownerNo),
    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    );
    """

create_pet_table = """
    CREATE TABLE IF NOT EXISTS Pet(
    petNo INT not null,
    petName VARCHAR(30) not null,
    petDOB VARCHAR(10) not null,
    animalSpecies VARCHAR(30) not null,
    petBreed VARCHAR(30) not null,
    petColor VARCHAR(30) not null,
    clinicNo INT not null,
    ownerNo INT not null,
    PRIMARY KEY(petNo),
    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo),
    FOREIGN KEY (ownerNo) REFERENCES PetOwner(ownerNo)
    );
    """

create_exam_table = """
    CREATE TABLE IF NOT EXISTS Examination(
    examNo INT not null,
    complaint VARCHAR(200) not null,
    dateSeen VARCHAR(10) not null,
    actionsTaken  VARCHAR(200) not null,
    staffNo INT not null,
    petNo INT not null,
    PRIMARY KEY(examNo),
    FOREIGN KEY (staffNo) REFERENCES Staff(staffNo),
    FOREIGN KEY (petNo) REFERENCES Pet(petNo)
    );
    """

# Execute query, the result is stored in cursor
cursor.execute(create_clinic_table)
cursor.execute(create_staff_table)
cursor.execute(create_petowner_table)
cursor.execute(create_pet_table)
cursor.execute(create_exam_table)

#----------Insert rows into tables--------------
insert_into_clinic = """
   INSERT OR IGNORE INTO Clinic VALUES 
    (0011, 'Healthy Paws', '49 Clay St, Miami, FL 33146', '3055551234'),
    (0012, 'Palms Vet', '345 Westbrook Dr, Miami, FL 33146', '3055553456'),
    (0013, 'Animal Care and Help', '89 South Dixie Hwy, Miami, FL 33146', '3055558754'),
    (0014, 'Coral Gables Vet Clinic', '264 Grenada Blvd, Miami, FL 33146', '3055559365'),
    (0015, 'Blue Star Vet', '78 Hillside Ave, Miami, FL 33146', '3055556543'),
    """

insert_into_staff = """
   INSERT OR IGNORE INTO Staff VALUES 
    (1015, 'Lisa Martinez', '5 Iguana Rd, Miami, FL 33146', '06-17-1989', 'Veterinarian Manager', 145000, 0011),
    (1002, 'Henry Green', '4 Glades Rd, Boca Raton, FL 33765', '11-29-1965', 'Veterinarian', 130000, 0011),
    (1007, 'Gloria Hernandez', '68 Pensacola Dr, Fort Lauderdale, FL 33206', '04-05-1995', 'Veterinarian Technician', 45000, 0011),
    (1008, 'Robert Jones', '123 Green St, Kendall, FL 33152', '09-12-2000', 'Receptionist', 35000, 0011),
    
    (1003 'Anthony Ramirez', ' 1200 Sunset Drive, Miami, FL 33143', '05-23-1975', 'Veterinarian', 125000, 0012),
    (1089, 'Olivia Torres', '840 Coconut Grove Boulevard, Miami, FL 33133', '12-25-1983', 'Veterinarian Manager', 135000, 0012),
    (1067, 'Daniel Perez', '567 Wynwood Street, Miami, FL 33127', '06-12-1998', 'Veterinarian Technician', 48000, 0012),
    (1019, 'Emily Woods', '243 South Beach Avenue, Miami, FL 33139', '10-05-2003', 'Receptionist', 32000, 0012),
    
    (1056 'Clara Rhodes', '1025 Little Havana Lane, Miami, FL 33130', '03-29-1972', 'Veterinarian', 111000, 0013),
    (1055, 'Benjamin Cruz', '475 Midtown Avenue, Miami, FL 33137', '02-12-1969', 'Veterinarian Manager', 120000, 0013),
    
    (1064 'Chloe Ramirez', '230 Pinecrest Road, Miami, FL 33156', '07-04-1950', 'Veterinarian', 140000, 0014),
    (1068, 'David Fernandez', '718 Allapattah Street, Miami, FL 33142', '03-04-1987', 'Veterinarian Manager', 160000, 0014),
    
    (1071 'Mia Rivera', '230 Pinecrest Road, Miami, FL 33156', '08-29-1950', 'Veterinarian', 112000, 0015),
    (1072, 'David Fernandez', '392 Bay Harbor Lane, Miami, FL 33154', '05-13-1987', 'Veterinarian Manager', 125000, 0015)
    """

insert_into_petowner = """
   INSERT OR IGNORE INTO PetOwner VALUES 
    (2000, 'Ethan Scott', '101 Lincoln Road, Miami, FL 33139', '3055557382', 0011),
    (2001, 'Sofia Franks', '238 Brickell Avenue, Suite 304, Miami, FL 33131', '3055558245', 0011),
    (2002, 'Noah Garcia', '870 Coral Gables Drive, Miami, FL 33134', '3055551526', 0012),
    (2003, 'Liam Johnson', '490 Little Havana Avenue, Miami, FL 33130', '3055557382', 0013),
    (2004, 'Ava Clarke', '90 South Beach Way, Miami, FL 33139', '3055556102', 0014),
    (2005, 'Nora Johns', '95 Allapattah Road, Miami, FL 33142', '3055558375', 0015)
    """

insert_into_pet = """
   INSERT OR IGNORE INTO Pet VALUES 
    (200, 'Lulu', '09-10-2017', 'Felis catus', 'Siamese cat', 'White and black', 0011, 2000),
    (201, 'Charlie', '01-19-2020', 'Canis lupus familiaris', 'Labrador retriever', 'Black', 0011, 2002),
    (202, 'Kaya', '10-29-2018', 'Canis lupus familiaris', 'Golden labrador retriever', 'Yellow', 0012, 2001),
    (203, 'Binx', '03-05-2022', 'Felis catus', 'Black cat', 'Black', 0013, 2003),
    (204, 'Zoe', '03-05-2022', 'Canis lupus familiaris', 'German shepard pointer', 'Brown and white', 0014, 2004),
    (205, 'Tigre', '05-10-2022', 'Canis lupus familiaris', 'German shepard mix', 'Brown', 0015, 2005),
    """

insert_into_exam = """
   INSERT OR IGNORE INTO Examination VALUES 
    (200, 'Lulu', '09-10-2017', 'Felis catus', 'Siamese cat', 'White and black', 0011, 2000),
    (201, 'Charlie', '01-19-2020', 'Canis lupus familiaris', 'Labrador retriever', 'Black', 0011, 2002),
    (202, 'Kaya', '10-29-2018', 'Canis lupus familiaris', 'Golden labrador retriever', 'Yellow', 0012, 2001),
    (203, 'Binx', '03-05-2022', 'Felis catus', 'Black cat', 'Black', 0013, 2003),
    (204, 'Zoe', '06-05-2020', 'Canis lupus familiaris', 'German shepard pointer', 'Brown and white', 0014, 2004),
    (205, 'Tigre', '05-10-2022', 'Canis lupus familiaris', 'German shepard mix', 'Brown', 0015, 2005),
    """

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()

