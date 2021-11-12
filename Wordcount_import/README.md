
HBASE version:(hbase version): 1.4.6
Hadoop Version :(hadoop version):3.3.1
Python Version:(python3 --version):3.8.10

Import output of wordcount program in HBase table with  python's happybase library:

 Initially install happybase : pip3 install happybase
 1)Start the hadoop server by following command and start the hbase server and start hbase shell :
  $start-all.sh
   $jps
   $start-hbase.sh
   $jps
   $hbase shell
2) Download the wordcount output file  from hdfs into local system directory
             $ hadoop  fs  -get   /word-count-2/outputfile/part-00000      /home/lenovo/word_count/out 
3) Go to the vs code and write the python code for creating connection with hbase and create table insert the data from wordcount output file and display the table contents,use logger .
4)To start Execution give the following code in terminal :
   $hbase-daemon.sh start thrift
5)Run the code in vs code , you can get output in printed on vs code terminal .
6)you can check it in the hbase shell also using : scan ‘tablename’
  >scan ‘WordCount1’

