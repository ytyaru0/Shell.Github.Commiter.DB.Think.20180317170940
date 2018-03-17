-- Repositories.{UserId}.db
create table Commits (
    Id          integer primary key,
    RepoId      integer,
    Message     text,
    Datetime    text, -- yyyy-MM-dd HH:mm:ss +0900
    Sha         text,
    foreign key RepoId reference Repositories(Id)
);
