-- Repositories.{UserId}.db
create table Repositories (
    Id          integer primary key autoincrement,
    Name        text unique,
    Created     text -- yyyy-MM-dd HH:mm:ss
);
