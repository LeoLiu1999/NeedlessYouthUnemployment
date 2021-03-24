
create table IF NOT EXISTS Users
(
    UserID int NOT NULL,
    firstName VARCHAR(20) NOT NULL,
    lastName VARCHAR(20) NOT NULL,
    email VARCHAR(64),
    PhoneNum VARCHAR(10),
    JoinDate date,
    primary key (UserID)
);

create table IF NOT EXISTS Company
(
    CompID int,
    CompName VARCHAR(20),
    primary key (CompID)
);

create table IF NOT EXISTS Position
(
    CompID int NOT NULL,
    PosName VARCHAR(100) NOT NULL,
    PosDesc VARCHAR(500),
    Salary float,
    PosLink VARCHAR(100),
    primary key (CompID, PosName),
    foreign key (CompID) references Company (CompID)
);

create table IF NOT EXISTS Applications
(
    UserID int,
    CompID int,
    PosName VARCHAR(100) NOT NULL,
    Completed bit DEFAULT 0,
    AppStatus VARCHAR(20) DEFAULT "Waiting",
    primary key (UserID, CompID, PosName),
    foreign key (UserID) references Users (UserID),
    foreign key (CompID, PosName) references Position (CompID, PosName)
);
