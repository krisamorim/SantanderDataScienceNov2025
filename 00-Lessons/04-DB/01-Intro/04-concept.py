#ACID
#Atomicity: Ensures that all operations within a transaction are completed successfully. If any operation fails, the entire transaction is rolled back, leaving the database in its previous state.
#Consistency: Guarantees that a transaction brings the database from one valid state to another, maintaining database invariants.
#Isolation: Ensures that concurrent transactions do not interfere with each other. Each transaction should operate as if it is the only transaction in the system.
#Durability: Once a transaction is committed, its changes are permanent and will survive any subsequent system failures.

#CAP Theorem
#Consistency: Every read receives the most recent write or an error.
#Availability: Every request receives a (non-error) response, without guarantee that it contains the most recent write.
#Partition Tolerance: The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

#In distributed systems, it is impossible to simultaneously provide all three guarantees of the CAP theorem. A system can only guarantee two out of the three at any given time.
#BASE
#Basically Available: The system guarantees availability, even in the presence of failures.
#Soft state: The state of the system may change over time, even without input. This is due to the eventual consistency model.
#Eventual consistency: The system will eventually become consistent once it stops receiving new updates.
#BASE is often used in NoSQL databases, which prioritize availability and partition tolerance over strict consistency.
#In summary, ACID properties are crucial for traditional relational databases to ensure reliable transactions, while CAP theorem and BASE properties are more relevant for distributed systems and NoSQL databases, focusing on availability and partition tolerance.
#ACID properties are essential for ensuring reliable transactions in traditional relational databases, while CAP theorem and BASE properties are more relevant for distributed systems and NoSQL databases, focusing on availability and partition tolerance.