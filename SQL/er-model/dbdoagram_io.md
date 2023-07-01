// Use DBML to define your database structure
// Docs: https://dbml.dbdiagram.io/docs

Table users {
  id integer [primary key]
  nickname varchar
  profile_url varchar
  email varchar
  region varchar
  created_at timestamp
}

Table articles {
  id integer [primary key]
  title varchar
  body text [note: 'Content of the post']
  category varchar
  created_at timestamp
  user_id integer
}

Table comments {
  id integer [primary key]
  body text
  user_id integer
  article_id integer
  created_at timestamp
}

Table likes{
  id integer [primary key]
  user_id integer
  article_id integer
  created_at timestamp
}

Ref : users.id < articles.user_id

Ref: users.id < comments.user_id

Ref : articles.id < comments.article_id

Ref : users.id < likes.user_id

Ref : articles.id < likes.article_id
