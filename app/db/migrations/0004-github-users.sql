-- 0004-github-users.sql
--
-- Description:
-- This migration deprecates the password login mechanism
-- present in the user model, including dropping columns.
--
-- Risks:
-- * No migration of users: at present there are zero users.
--   Even so, there will be a legacy_users table.

-- Archive existing users table prior to new schema;
create table if not exists users_archive_231125 as
		select *
		from users;

-- Drop users table and recreate.
-- This is necessary because there's currently no way
-- of disabling autoincrements on the id column.
drop table users;
create table if not exists users (
		id integer not null primary key,
		email text not null,
		gh_login text not null,
		gh_node_id text not null,
		gh_avatar_url text,
		gh_type text,
		gh_created_at datetime,
		is_active boolean not null,
		is_admin boolean not null default false,
		creation_date datetime not null default current_timestamp,
		last_login datetime
);
