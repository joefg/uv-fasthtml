-- 0001-logbook.sql

create table if not exists logbook (
	id integer not null primary key autoincrement,
	content text not null,
	created_at timestamp not null default current_timestamp
);

insert into logbook (
	id,
	content
) values (
	0,
	"First entry!"
);
