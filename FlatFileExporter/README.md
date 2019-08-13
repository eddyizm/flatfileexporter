# Flat File Exporter
---
#### CURRENT BUILD - BETA 0.0.1.0
---

## Overview 

Application to generate flat files or excel data dumps. The application will take a sql file or stored procedure and export a file.

Supported extensions: 
* txt
* csv
* xlsx
  
Supported delimiters:  
* pipe ( | )
* comma ( , )
* tab ( )

## Requirements 

* ODBC Driver 17 for SQL Server
* Microsoft .NET Framework 4.6.1 

If you don't have it on your system, please install ODBC Driver 17 for SQL Server here:
https://www.microsoft.com/en-us/download/details.aspx?id=56567  

Update .Net Framework here:
https://www.microsoft.com/en-us/download/details.aspx?id=49981


# GUI 
---
![alt text](assets/ffe_01.png "Flat File Exporter") 

The server and database has a dummy value, `Server1` and `DB1`. 
You will need to specify your actual server by clicking on the plus and going to the Add A Server screen. 

![alt text](assets/ffe_02.png "Add A Server") 

Add your databases...

![alt text](assets/ffe_03.png "Add A Database") 

### Credentials

By default Flat File Exporter uses Microsoft's ODBC Driver 17 for SQL Server and the Trusted_Connection=yes setting, passing the credentials of the user along to the db. This is standard practice in Enterprise environments that relay on AD to manage permissions. If you enter credentials below then your default credentials will be ignored."

![alt text](assets/ffe_04.png "Credentials") 

---
# Command Line Interface (CLI)  

The CLI is far more powerful and allows passing a stored procedure. You can also call the exe directly to schedule file exports along with calling it programmatically to go through loops over large amounts of variables and data.

```
usage: flatfile_cli.py [-h] [-V] [-f FILENAME] [-u USERNAME] [-pass PASSWORD]
                       (-csv | -txt | -xlsx) (-c | -t | -p)
                       (-s SQLSCRIPT | -sp STOREDPROC)
                       server db directory

Takes sql script or stored proc to export csv, txt or excel file.

positional arguments:
  server                server to run query against.
  db                    database to use on server.
  directory             location to export flat file. do not specify
                        extension.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -f FILENAME, --filename FILENAME
                        filename. Date will be appended.
  -u USERNAME, --username USERNAME
                        username for db connection.
  -pass PASSWORD, --password PASSWORD
                        use login/pass from instead of default Integrated
                        Security (Trusted_Connection).
  -csv, --csv           output file with csv extension.
  -txt, --txt           output file with txt extension.
  -xlsx, --xlsx         output excel file.
  -c, --comma           use comma character for seperator.
  -t, --tab             use tab for seperator.
  -p, --pipe            use pipe character for seperator.
  -s SQLSCRIPT, --sqlscript SQLSCRIPT
                        full path of sql script *MUST HAVE* SET NO COUNT on
                        script.
  -sp STOREDPROC, --storedproc STOREDPROC
                        instead of sql script, point to stored procedure on
                        database. Wrap in double quotes with parameters eg.
                        "EXEC SAMPLE_SP '<Param>'"
```                        