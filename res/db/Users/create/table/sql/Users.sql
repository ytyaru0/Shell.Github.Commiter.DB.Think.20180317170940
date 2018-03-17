-- Users.db
create table Users (
    Id          integer primary key autoincrement,
    IdOnGithub  integer,
    Name        text unique
);
