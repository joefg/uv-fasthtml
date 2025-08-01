-- 0002-users.sql

create table if not exists users (
    id integer not null primary key autoincrement,
    email text not null unique,
    password_hash text not null,
    password_salt text not null,
    is_active boolean not null,
    is_admin boolean not null default false,
    creation_date datetime not null default current_timestamp,
    last_login datetime
);

-- Insert a dummy user with no privileges to kickstart the autoincrement.
insert into users (
    id,
    email,
    password_hash,
    password_salt,
    is_active,
    is_admin
)
values (
    0,
    'none@none.null',
    -- sha256(nopassword)
    'b0aafc49c0854fc6c1e612dbe0856e4b801867ce55d6c8023f358c17aef4867a',
    '',
    false, -- inactive
    false  -- Not an admin
);