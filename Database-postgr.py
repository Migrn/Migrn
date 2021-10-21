#!/usr/bin/env python
# coding: utf-8

# # Lesson 1 Exercise 2: Creating a Table with Apache Cassandra
# <img src="images/cassandralogo.png" width="250" height="250">

# ### Walk through the basics of Apache Cassandra. Complete the following tasks:<li> Create a table in Apache Cassandra, <li> Insert rows of data,<li> Run a simple SQL query to validate the information. <br>
# `#####` denotes where the code needs to be completed.

# #### Import Apache Cassandra python package

# In[1]:


import cassandra


# ### Create a connection to the database

# In[2]:


from cassandra.cluster import Cluster
try: 
    cluster = Cluster(['127.0.0.1']) #If you have a locally installed Apache Cassandra instance
    session = cluster.connect()
except Exception as e:
    print(e)
 


# ### TO-DO: Create a keyspace to do the work in 

# In[3]:


## TO-DO: Create the keyspace
try:
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS musicmig 
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
)

except Exception as e:
    print(e)


# ### TO-DO: Connect to the Keyspace

# In[4]:


## To-Do: Add in the keyspace you created
try:
    session.set_keyspace('musicmig')
except Exception as e:
    print(e)


# ### Create a Song Library that contains a list of songs, including the song name, artist name, year, album it was from, and if it was a single. 
# 
# `song_title
# artist_name
# year
# album_name
# single`

# ### TO-DO: You need to create a table to be able to run the following query: 
# `select * from songs WHERE year=1970 AND artist_name="The Beatles"`

# In[18]:


## TO-DO: Complete the query below
query = "CREATE TABLE IF NOT EXISTS musicmig "
query = query + "(song_title text,artist_name text,year int,album_name text,single boolean , PRIMARY KEY (year, artist_name))"
try:
    session.execute(query)
except Exception as e:
    print(e)


# ### TO-DO: Insert the following two rows in your table
# `First Row: "1970", "Let It Be", "The Beatles", "Across The Universe", "False", `
# 
# `Second Row: "1965", "Think For Yourself", "The Beatles", "Rubber Soul", "False"`

# In[25]:


## Add in query and then run the insert statement
query = "insert into musicmig (year,song_title,artist_name,album_name,single)" 
query = query + " VALUES (%s, %s, %s, %s, %s)"

try:
    session.execute(query, (1970, "Let It Be", "The Beatles", "Across The Universe", False))
except Exception as e:
    print(e)
    
try:
    session.execute(query, (1965, "Think For Yourself", "The Beatles", "Rubber Soul", False))
except Exception as e:
    print(e)


# ### TO-DO: Validate your data was inserted into the table.

# In[27]:


## TO-DO: Complete and then run the select statement to validate the data was inserted into the table
query = 'SELECT * FROM musicmig'
try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)


# ### TO-DO: Validate the Data Model with the original query.
# 
# `select * from songs WHERE YEAR=1970 AND artist_name="The Beatles"`

# In[37]:


##TO-DO: Complete the select statement to run the query 
query = "select * from musicmig where year=1965 and artist_name='The Beatles'"

try:
    rows = session.execute(query)
except Exception as e:
    print(e)
    
for row in rows:
    print (row.year, row.album_name, row.artist_name)


# ### And Finally close the session and cluster connection

# In[ ]:


session.shutdown()
cluster.shutdown()


# In[ ]:




