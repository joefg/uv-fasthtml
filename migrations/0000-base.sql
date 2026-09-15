CREATE TABLE user (
	id INTEGER NOT NULL, 
	is_active BOOLEAN NOT NULL, 
	is_admin BOOLEAN NOT NULL, 
	gh_login VARCHAR NOT NULL, 
	gh_node_id VARCHAR NOT NULL, 
	gh_avatar_url VARCHAR NOT NULL, 
	gh_type VARCHAR NOT NULL, 
	gh_created_at DATETIME NOT NULL, 
	creation_date DATETIME, 
	last_login DATETIME, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_user_id ON user (id);

CREATE TABLE "usernote" (
	id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	note_added_by INTEGER NOT NULL, 
	note VARCHAR NOT NULL, 
	created_at DATETIME, 
	PRIMARY KEY (id), 
	CONSTRAINT fk_usernote_user_added_by FOREIGN KEY(note_added_by) REFERENCES user (id)
);
CREATE INDEX ix_usernote_id ON usernote (id);
