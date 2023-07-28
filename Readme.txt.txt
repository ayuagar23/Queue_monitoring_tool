
Patch Tool to Clear RabbitMq Messages

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


This python Script is regarding filtering rabbitmq queues with non-zero values (error messages) , 
and printing them in console with the total number of error messages.
Also , In the input file there are duplicate queues with same name format and in the output file 
those duplicate queues are merged as unique queues (in generalised form) and also the number of 
occurrences of each queue is also printed in the output file.




Example
------------------------------------------------------------------------------------------------------


INPUT File:

LdapMigration_1_ZVF-SDLA-0111-PRO-VM_MANAGER_LISTENER   50
NSRDataQuery_1_ZVF-SDLA-0111-PRO-VM_RPC_REPLY_1 0
MultiSAImport_1_ZVF-SDLA-0111-PRO-VM_RPC_REPLY_1        0
BulkQueryConsumer_3_ZVF-SDLA-0111-PRO-VM_RPC_REPLY_1    0
ServiceManager_ZVF-SDLA-0111-OPS-VM_MANAGER_LISTENER    0
LdapMigration_2_ZVF-SDLA-0111-PRO-VM_MANAGER_LISTENER   0
NSRDataQuery_2_ZVF-SDLA-0111-PRO-VM_RPC_REPLY_1 0


-------------------------------------------------------------------------------------------------------


OUTPUT File:

LdapMigration_n_ZVF-SDLA-n-PRO-VM_MANAGER_LISTENER , 2
NSRDataQuery_n_ZVF-SDLA-n-PRO-VM_RPC_REPLY_n , 2
MultiSAImport_n_ZVF-SDLA-n-PRO-VM_RPC_REPLY_n , 1
BulkQueryConsumer_n_ZVF-SDLA-n-PRO-VM_RPC_REPLY_n , 1
ServiceManager_ZVF-SDLA-n-OPS-VM_MANAGER_LISTENER , 1


--------------------------------------------------------------------------------------------------------


CONSOLE OUTPUT:

Queues with non-zero messages :

LdapMigration_n_ZVF-SDLA-n-PRO-VM_MANAGER_LISTENER : 50



:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


Some FAQs


1) What is the problem addressed by this script 
2) What is the scenario when this script is to be executed 
3) What is the impact without this script.


Most of the issues regarding job management can be narrowed down to a particualar area if any queue values 
are non zero.We get a handy list of queues with non zero messages using this script.
Also aggregation of queues is is done based on worker type.
This script can be executed when trouble shooting or debugging any job related issues. 
Using this script finding queues with non zero messages is easier.
Once we find queues with non zero messages we can narrow down the issue to the particular worker responsible 
for consuming those messages and check why the worker is not reading those
