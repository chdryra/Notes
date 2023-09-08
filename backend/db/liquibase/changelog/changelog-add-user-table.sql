--liquibase formatted sql

--changeset rizwan.choudrey:1 labels:version-1 context:dev
--comment: adding users table
create table users (
    id int primary key not null,
    name varchar(50) not null,
    email varchar(320),
)
--rollback DROP TABLE users;



