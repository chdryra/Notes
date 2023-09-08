--liquibase formatted sql

--changeset rizwan.choudrey:1 labels:version-1 context:dev
--comment: adding person table
create table person (
    id int primary key not null,
    name varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city varchar(30)
)
--rollback DROP TABLE person;



