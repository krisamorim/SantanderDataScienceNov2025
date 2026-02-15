#https://app.quickdatabasediagrams.com

Users
-
id PK int
name string
dateOfBirth Date
Address1 string

Booking
-
id PK int
idUsers int FK >- Users.id
idDestination int FK >- Destination.id
status boolean

Destination
-
id PK int
name string
descrition string
