# Easy Sql (Esql) 

- ## *I did'nt knew SQL, so i created a simple form of that which i can use in my small python projects, and its very handy if you ask me , feel free to contribute, this is just a starting!*

> Made by Me, (Hamza .S) aka (hmZa)

## This ```PACKAGE``` contains:
- ```nSqlServerUtil.py:``` The main code file!
- ```repl.py:``` The `esql` repl!
- ```codefile.esql:``` Basic commands and workthrough!

## Learn

### *Commands*
```ruby
[-h] 
[--serve SERVE] 
[--newdb NEWDB] 
[--dbpath DBPATH] 
[--newtable NEWTABLE] 
[--columns COLUMNS [COLUMNS ...]] 
[--insert INSERT [INSERT ...]] 
[--replace REPLACE [REPLACE ...]]
[--showgrid]
[--grid {json,yaml,toml}] 
[--savetable SAVETABLE] 
[--savedb SAVEDB] 
[--saveall SAVEALL] 
[--savegrid SAVEGRID SAVEGRID]
```

### *Examples*

```ps

PS G:\fri3nds\w-category-projects\JsonSql\Release> python repl.py
>> --newdb db1

>> --newtable UserAccessTokens --columns User_Name Access_Token Quota_Limit Used_Quota User_Type --dbpath ./db1

>> --insert Hamza y877T(Tt*T87tG76T76T76t^& 15000 10090 Premium_User --dbpath ./db1/UserAccessTokens.json

>> --insert Moobi 0xUYT74T37TR4YTYYTYRTY3UG 50000 13090 Premium_User --dbpath ./db1/UserAccessTokens.json  

>> --insert Dude  0x898t76t6T77TtfTFtFTftFt 2000  1900  Free_User    --dbpath ./db1/UserAccessTokens.json    

>> --insert Trump 0x7t58747tr74tr74t37ytryu 2000  1250  Free_User    --dbpath ./db1/UserAccessTokens.json  

>> --showgrid --dbpath ./db1/UserAccessTokens.json
+-------------+---------------------------+---------------+--------------+--------------+
| User_Name   | Access_Token              |   Quota_Limit |   Used_Quota | User_Type    |
+=============+===========================+===============+==============+==============+
| Hamza       | y877T(Tt*T87tG76T76T76t&  |         15000 |        10090 | Premium_User |
+-------------+---------------------------+---------------+--------------+--------------+
| Moobi       | 0xUYT74T37TR4YTYYTYRTY3UG |         50000 |        13090 | Premium_User |
+-------------+---------------------------+---------------+--------------+--------------+
| Dude        | 0x898t76t6T77TtfTFtFTftFt |          2000 |         1900 | Free_User    |
+-------------+---------------------------+---------------+--------------+--------------+
| Trump       | 0x7t58747tr74tr74t37ytryu |          2000 |         1250 | Free_User    |
+-------------+---------------------------+---------------+--------------+--------------+

>> --replace Moobi 0xUYT74T37TR4YTYYTYRTY3UG 50000 13090 Premium_User Moobi 
0xUYT74T37TR4YTYYTYRTY3UG 0 0 Hacker_Dectected --dbpath ./db1/UserAccessTokens.json

>> --showgrid --dbpath ./db1/UserAccessTokens.json
+-------------+---------------------------+---------------+--------------+------------------+
| User_Name   | Access_Token              |   Quota_Limit |   Used_Quota | User_Type        |
+=============+===========================+===============+==============+==================+
| Hamza       | y877T(Tt*T87tG76T76T76t&  |         15000 |        10090 | Premium_User     |
+-------------+---------------------------+---------------+--------------+------------------+
| Moobi       | 0xUYT74T37TR4YTYYTYRTY3UG |             0 |            0 | Hacker_Dectected |
+-------------+---------------------------+---------------+--------------+------------------+
| Dude        | 0x898t76t6T77TtfTFtFTftFt |          2000 |         1900 | Free_User        |
+-------------+---------------------------+---------------+--------------+------------------+
| Trump       | 0x7t58747tr74tr74t37ytryu |          2000 |         1250 | Free_User        |
+-------------+---------------------------+---------------+--------------+------------------+
>>

```

# DEVELOPERS!

### *ONLY ME, (hmZa):* 
- > Please, This project needs a fix, I am not drunk but you guys deserve better!


> #  HAPPT CONTRIBUTE!!!!