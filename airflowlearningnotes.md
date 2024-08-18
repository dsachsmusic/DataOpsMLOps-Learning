Inspect shape (shape of data)
Describe (prints the table?)
Series….vs…categories?
Piping and chaining
Using scikitlrn for Regression and all sorts of other modeling
“Fit” method/function/whatever
Normalizing/standardizing - so data fits better? 

The “Request” library (module) and the “JSON” library
Pretty print
results.json (converts json to python dictionary(?))
A property in a json object can be a list
For getting a specific item out of JSON, in python, loop, and index into it (?)
JSON has types - you can have strings, INTs, floats(?), lists (?) or arrays or something, etc.
python: URL lib (module), http lib/module
Error handling - …import the httperror class, and or the urlerror class?
Cookies, authentication, session handling - the “requests” lib has functionality
Httpbin.org for testing requests
Requests.get
Request.text

with python, to read in a file, open the file with open(filename, mode ='r'), and then do file.read
**and then have to close the file (or it stays open forever?)
note - in python, if divide a number by another number, it will come out as a float (even if its a round nubmer - like 2.0 - and that makes it hard to compare to an int later)
---** so, could do, example [int]4/2 - or something, but also could 4 // 2 - this // operator gives you the floor (floor meaning rounds down)
creating a function (with "def")


open(file_path, "r") as f:
        values = f.read()
    f.close()

values = [
        int(i) for i in values
    ]
	
word_one = "a word"
word_two = "another word"
print("Word one is {} word two is {}".format(word_one, word_two))

pip freeze would ge tlist of installed modules - build requirements file from that

Virtenvwrapper or something
.py packages vs packages
pip -V (version)
pip —user
pip comes with python 3 when you download an installer, but not when you use a package manager
Env variable for python and for pip in PATH
Pip install (or something) installs all dependencies for a given module/library pollutes your python environment …pip install -U or uninstall or whatever does not remove those dependencies, so have to uninstall 1 by 1
Location where modules get installed?
Pip show - tells you info about your pip install
Pip help
Pypi.org or whatever - also called the cheese site or something - python package index - where you can download packages
Pypi.org or whatever - also called the cheese site or something - python package index - where you can download packages
Virtenvwrapper activates the environment and moves you to it
virtenvwrapper, pip env 
Wheel - name for a package or something … old name / version was something else
pip env exit to log out (instead of deactivate)


Python lambdas - python object oriented, python taking in and formatting JSON
Python comprehensions 
Python data types list and dictionary

Databricks - Databricks can direct data directly into a model (LLM, AI, whatever?).

Processing - Spark
Scheduling - Airflow (scheduling transfer of data….in order needed, if dependencies apply)
Making schema efficient (for structured DBs)
Database types: structures (tabular), semi structured (JSON, for instance), unstructured (video and image data, for instance?)
Distributed systems…..for parallel processing….so that memory that has the data in it can be close to the compute
distributed computing: split the data…to commodity compute hardware…process in parallel…and then rejoin

Schema - getting the schema right/optimized important
Dimensional schema (or whatever) ….such as the star schema…where you have a fact table, and then you have dimension tables….one tells you about the world, and the other tells you about the things in the world
Data frames….
Map Reduce - group by ….and then separate groups…and process separately?  Or something
Hadoop - distributed….
map reduce 
HDFS - filesystem….used for hadoop
Transfomations include groupbykey()
Scheduling - Data might come from APIs, csv’s, etc…so a chron job or something usually isn’t sufficient
Unstructured data (text), flat files (tab delimited or csv), or json
DAG - Directed Acyclic Graph - for scheduling and orchestrating jobs for getting data based on dependencies….
Extraction is pulling data out of storage, or from APIs, and getting it into memory
OLTP - (online) transaction databases…used for applications…because applications generally have a lot of transactions
OLAP - (online) analytics databases ….used for analytics…. Big queries?  Maybe?
Extract from postgresql db…using pyspark…from command line …(?) with jdbc driver……get a dataframe 
Do a group by, and an aggregation (such as getting the average of a column…) and and then you end up new data (like a typical aggregation I used to see at wayfair, perhaps…new column with the average, for each….) and can print that out with the print function….to check/confirm….(in real time?) and then load….which is putting it in a new table?
Data Engineers are master automators…they have to find creative ways to automate manual processes
originally, ETL was done all with scripts…now we have software…to do with “workflows”…
Orchestration -.... Airflow
DAG includes managing dependencies…and not starting jobs until others are finished, and that kind of stuff (workflows?)
Airflow is pretty open / extensible…you can customize “operators” (or something), can do custom executors, etc etc.and it’s in python, (also uses jinja btw ….not jinja2, jinja)
Airflow is both a (python) library and an application…understand this distinction
Airflow has a db and a webserver …db holds the DAG configurations?  Webserver is an interface for managing and configuring DAGs?  And schedules? (??)
ETL vs ELT….loading it into new final location before doing transform?
Tasks - in a DAG
Dependencies, in a DAG
Direct edge - or something - two tasks next to each other?
Can do transforms in SQL, or Python, etc….but
…but also, can use Pandas
The entire ETL process can be enclosed in a DAG…calling other DAGs?
Databases with Rows and columns are good for data integrity but they aren’t as horizontally scalable as those without
Hadoop - the map reduce approach, and the storage (HDFS, at the time, was all that was used. Cloud versions - GCP Dataproc….AWS EMR (elastic map reduce)??? 
Three parts to map reduce: map, Shuffle, reduce
Scala, by the way, is functional Java
“Hello world” example in Map reduce is to do a word count of a text…use regex to split words, ignore periods, tabs, etc.  …for Shakespeare text, as example … 
…result /outcome of map reduce (at least the basic word count example?) is key value pairs (in the word count example, key is a word, and value is number of times it appears)
Not only SQL
Built for the web…fast, flexible…
NoSQL schema is ….non existent? Flexible?  
Main types/classes of databases: Wide column (casandra? couchDB?) , Document (MongoDB?), Key value (redis), and one other. 
Graph databases have nodes and edges....no ohter structure
Pandas (Python library (?) - can build a full data pipeline just with this…
Transform - involves things like standardizing data, removing duplicates (?) or nulls ? (?)...adjusting column formats (?) . like, if date is represented as a string, typing it as a date (or vice versa, or whatever)
Load is getting it into a place -like a data lake or data warehouse, where people can do analytics on it
Sequence and frame

Architectural considerations/scheduling - How often to Truncate…whether to truncate (?)

Dataflow - Apache Beam - Beam is a way to create pipeline definitions that are separate from whatever pipeline software/stack(?) you use

Redshift is AWS’ Data warehouse solution
RDMBS’ ….files written on a disk …in blocks (like all databases?) - and…when query it, needs to scan the whole file (there is a term for this) …
…can do index….so doesn’t have to scan entire file (knows what file to go to, for, say keys x, through y)...but still
…and you have locks….locks lock the whole file …and row locks…those are a little better…but still
Setting up a data warehouse/optimizing: with reporting/analysis, often, you know what kind of reports you are going to want 

There are a number of ways to you can Redshift will split the data to databases, and sort the databases….this includes choose what column to sort by before doing a split…for example, if you sort by date, and then split the data in chunks of date ranges…say jan - mar, april - jun, etc…then when you query for jan-mar…its not optimized/not using parallel processing. W

NoSQL AWS managed database - similar to MongoDB (in that it’s NoSQL) but also different in many ways.
But first: SQL vs NoSQL - relational databases were developed /popularized in a time when storage was very expensive…separating out into tables means less duplicate data (don’t have an infinite sized row for every peice of data….just join it when needed). But now, data storage is cheap, and it’s processing time/power that we need to make the most of…and, with NoSQL - you don’t have joins - data is simply all there? 



Big Data learning
Three Vs: volume, velocity, variety
Velocity is like …coming in real time, for instance (sensor data, etc.)

Big Data learning
Three Vs: volume, velocity, variety
Velocity is like …coming in real time, for instance (sensor data, etc.)

Evolution of data stuff:  data warehouses….typically for relational db data…all in one location, often…just text…issue is that data is siloed…by organizational unit (HR data, marketing data, etc) and can’t be used together for analytics??
Data lake - like Hadoop - can store the variety of data types …risk of becoming a “swamp” …
Cloud approach …better than ever(?)



salmon farming vs wild caught …. If you create (farm, so to speak) your own data (somehow…for instance, a biotech company does its own experiments ….hundreds of thousands) you don’t have a problem of cleaning the data….wild caught data needs to be cleaned…example phone numbers, dates…etc… machines don’t know how to read the differences (dashes, slashes)....will interpret them as different data.  Also, 999 and 888, etc.  all that stuff.

Types of math you need to know….Calculus, linear regression, other sorts of math…( I think there are found you can use) …you understand these, and how/when to use them (i.e. when define your procedure for a given problem you decide which of these to use

Cloud native DB - serverless
- is a lake house - meaning it can do 
datawarehousing and datalake functionality …
Parque (?) data format

Run Ubuntu running in WSL
(starting from fresh install of Ubuntu)
Set up virtual env 
- sudo apt install python3.10-venv
- python3 -m venv airflow_env
Install Airflow
- sudo apt install python3-pip
- pip install apache-airflow
Activate virtual env
- source airflow_env/bin/activate	
Set up the Airflow home directory (environment variable in bash)
- export AIRFLOW_HOME=~/airflow
- echo $AIRFLOW_HOME
Initialize the Airflow DB
- airflow db init
Create a user
- airflow users create --username admin --firstname Admin --lastname User  --role Admin --email admin@example.com
- For password, enter "admin" (just for local use...not secure)
Start webserver
- airflow webserver --port 8080
In a separate terminal, start the scheduler
- a	irflow scheduler
- Visit the scheduler (http://localhost:8080)	
Create a DAG
- Might need to create dags directory (though it should have been created automatically)
-- mkdir ~/airflow/dags
- Create a file
-- simple_dag.py
-- create dag contents (details not includeded here)
Run the DAG
- Go to airflow web UI > DAGs...
- Find the DAG and run it

Notes:
If ever want to reset the db (clear it)
- rm -rf $AIRFLOW_HOME/db.sqlite $AIRFLOW_HOME/logs/
