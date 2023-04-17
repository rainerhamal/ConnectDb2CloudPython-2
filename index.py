# Import the ibm_db Python library
# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
#!pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
#!pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
#!pip install ipython-sql
import ibm_db
from config import dsn_hostname,dsn_uid,dsn_pwd,dsn_driver,dsn_database,dsn_port,dsn_protocol,dsn_security

# Identify the database connection credentials in config.py

# Create the DB2 database connection
# Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};"
).format(dsn_driver,dsn_database,dsn_hostname,dsn_port,dsn_protocol,dsn_uid,dsn_pwd,dsn_security)

# print the connection string to check correct values are specified
print(dsn)

# Establish the connection to the database
# Create a database connection
try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
except:
    print("Unable to connect: ", ibm_db.conn_errormsg())

# Retrieve Metadata for the Database Server
server = ibm_db.server_info(conn)
print("DBMS_NAME: ", server.DBMS_NAME)
print("DBMS_VER: ", server.DBMS_VER)
print("DB_NAME: ", server.DB_NAME)

# Retrieve Metadata for the Database Client / Driver
client = ibm_db.client_info(conn)
print ("DRIVER_NAME: ", client.DRIVER_NAME) 
print ("DRIVER_VER: ", client.DRIVER_VER)
print ("DATA_SOURCE_NAME: ", client.DATA_SOURCE_NAME)
print ("DRIVER_ODBC_VER: ", client.DRIVER_ODBC_VER)
print ("ODBC_VER: ", client.ODBC_VER)
print ("ODBC_SQL_CONFORMANCE: ", client.ODBC_SQL_CONFORMANCE)
print ("APPL_CODEPAGE: ", client.APPL_CODEPAGE)
print ("CONN_CODEPAGE: ", client.CONN_CODEPAGE)

# Close the Connection
# We free all resources by closing the connection. Remember that it is always important to close connections so that we can avoid unused connections taking up resources.
try:
    ibm_db.close(conn)
    print("True")
except:
    print("Connection not close: ", ibm_db.conn_errormsg())