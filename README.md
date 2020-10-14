
# DynamoDB
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
DynamoDB allows users to create databases capable of storing and retrieving any amount of data, and serving any amount of traffic. It automatically distributes data and traffic over servers to dynamically manage each customer's requests, and also maintains fast performance.

#### Advantages of DynamoDB:
-   **Scalable –** User can store unlimited amount of data.
-   **Distributed** – DynamoDB scales horizontally by expanding a single table over multiple server
-   **Automatic data replication**  – All data items are stored on Solid State Disks (SSDs) and automatically replicated across multiple availability zones in a region
-   **Secure**  – DynamoDB uses proven secured methods to authenticate users and prevent unauthorized data access
________
## Brief Overview of DynamoDB
In DynamoDB, we have **tables**, **attributes**, and **items**.

A **table** holds sets of items, and **items** hold sets of attributes. An **attribute** is a fundamental element of data requiring no further decomposition, i.e., a field.

In DynamoDB we have Primary Keys and Secondary Indexes. 
Primary Keys serve as the means of unique identification for table items, and Secondary Indexes provide query flexibility. 

### Primary Key
This identifies table items. No two items share a key. DynamoDB uses two types of primary keys −

-   **Partition Key**  − This simple primary key consists of a single attribute referred to as the “partition key.” Internally, DynamoDB uses the key value as input for a hash function to determine storage.
    
-   **Partition Key and Sort Key**  − This key, known as the “Composite Primary Key”, consists of two attributes.
    -   The partition key and
    -   The sort key.
    -  
    DynamoDB applies the first attribute to a hash function, and stores items with the same partition key together; with their order determined by the sort key. **Items can share partition keys, but not sort keys.**

## Secondary Indexes

These indexes allow you to query table data with an alternate key. Though DynamoDB does not force their use, they optimize querying.

DynamoDB uses two types of secondary indexes −

-   **Global Secondary Index**  − This index possesses partition and sort keys, which can differ from table keys.
    
-   **Local Secondary Index**  − This index possesses a partition key identical to the table, however, its sort key differs.

________

## Demos
- Create a New Table: examples/create_table.py creates a new table 'CourseAssistants' with PrimaryKey as id
- Insert Items: examples/insert_item.py inserts the list of TAs with their OH Timings to the table
- Get Item: examples/get_item.py fetches the item for the given key
- Query Item: examples/query_item.py will query the table where the condition matches the input condition
- Delete Item: examples/delete_item.py deletes the item given the Primary Key
- Delete Table: examples/delete_table.py deletes the entire table
- Create Table with GSI: examples/create_table_gsi.py creates another table again named as 'CourseAssistants' (as we deleted the one before), but now with a GSI as name.
- Query Item with GSI: examples/query_item_gsi.py will query the new table, now with GSI. First we needed the ID to fetch the results, but now can fetch the results just with the name attribute.