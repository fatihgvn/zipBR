# zipBR
brute forse zip password

It is a simple and small archive password enforcement algorithm that overcomes a core of the processor.
Only available for ZIP archives.

## Program parameters

usage: zipBR.exe [-h] [-f FILE] [-a] [-c] [-n] [-s] [-p]

short | long | explanation
------|------|------------
-h| --help|show this help message and exit
-f FILE| --file FILE | Location of the archive to open
-a| --all            | Use any chars
-c| --useChars       | Use all letters from a to Z
-n| --useNumbers     | Use all figures
-s| --useSpecialChars| Use special characters
-p| --useSpace       | Use <SPACE> character
-v| --version        | Show version number


## tested password list

testDoc1.zip -> /Sk85Q
- not tested

testDoc2.zip -> &5{5wLAdU.)a
- not tested

testDoc3.zip -> sY>8_e3/Pj5A~PT7Z\p9Rg58
- not tested

easy.zip -> dfsf
- Total time 0:03:13.970651

### easy.zpi test output

Using start command ``.\zipBR.exe -c -f .\zips\easy.zip``

```
Using char list is:
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
Start Time 2019-05-17 15:22:18.812588
Trying a 1-digit password
Trying a 2-digit password
Trying a 3-digit password
Trying a 4-digit password
password is dfsf
End Time 2019-05-17 15:25:32.783239
Total time 0:03:13.970651
```