# PyBasicBlockchain2 Lib V1 📩🧱

Welcome to **PyBasicBlockchain2 Lib V1**! Custom ```SQL``` engine built with blockchain!

### *Taste!!!*

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

## Known Bugs 🐞
- The current implementation has a known issue where the blockchain validation fails due to hash mismatches. For example:
```shell
Block 1 hash mismatch: 000056ccfdd3c323f561a7a5aa736b918ec8300190c7ad76f71a7cdff0af5a5a != 5c82a22c32bd3232f1d8fcb129198a3ab521041cbe52001a7339d0fa1cc1df1e
Is blockchain valid? False
```

- This bug affects the is_chain_valid method, and fixing it will involve troubleshooting the hash computation and block validation logic.

*FOR MORE INFO SEE `./KRAZY.md`*
