-- Repositories.{UserId}.db
create table EditingAmounts (
    Id          integer primary key,
    CommitId    integer,
    LanguageId  integer, -- Languages.db Languages.Id
    Insertions  integer,
    Deletions   integer,
    foreign key CommitId reference Commits(Id)
);
