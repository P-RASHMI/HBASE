HBASE version:(hbase version): 1.4.6

Hadoop Version :(hadoop version):3.3.1

Python Version:(python3 --version):3.8.10



Real time stock data storing on HBase with python's happybase:



1)Start hadoop server, hbase server,hbase shell :
   $start-all.sh
   $jps
   $start-hbase.sh
   $jps
   $hbase shell


2)Create python code using hbase to connection,create table,import Api live stock data from website into hbase table and print it


3)To execute the code in terminal, run the thrift command
   ~$ hbase-daemon.sh start thrift


4)Now in vs code run the python code,output printed on the  terminal:



5)Now in the hbase shell see the table data with :scan ‘tablename’
            hbase(main):005:0> scan ‘stockdata_table’

