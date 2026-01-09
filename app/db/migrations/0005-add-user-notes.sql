-- 0005-add-user-notes.sql
--
-- Description: Support staff should be able to add
-- internal notes to user profiles. This is the data
-- store.
--

create table if not exists user_note (
		id integer not null primary key,
		user_id integer not null,
		added_by_id integer not null,
		note text,
		creation_date datetime not null default current_timestamp,
		foreign key (user_id) references users(id),
		foreign key (added_by_id) references users(id)
);

insert into user_note (
		id,
		user_id,
		added_by_id,
		note
) values (
		1,
		1001,
		1002,
		"Test note."
);
