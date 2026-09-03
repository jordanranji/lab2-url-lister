Solution for Lab 2 - Jordan Ranji - CSCI 5253\
The following is my output for my Mapper.py -> Reducer.py function:\

\#       18\
https://en.wikipedia.org/wiki/Google_File_System        6\
https://en.wikipedia.org/wiki/ISBN_(identifier) 18\
https://en.wikipedia.org/wiki/S2CID_(identifier)        14\
mw-data:TemplateStyles:r1295599781      33\

The mapper function splits each line by space, and then looks for words starting with href= to determine where the urls are.\
Then, those urls are parsed from the word by removing the first 6 characters (href=") and finding the index of the next quotation mark and keeping all characters up to that point.\
To run this you will need Hadoop and Python.\

With 2 workers, the time for execution was 1m35.753s. With 4 workers, it surprisingly slowed down to 1m54.178s.
