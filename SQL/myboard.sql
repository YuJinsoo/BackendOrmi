CREATE TABLE "users" (
  "id" serial PRIMARY KEY,
  "nickname" varchar(255),
  "profile_url" varchar(255),
  "email" varchar(255),
  "region" varchar(255)(255),
  "created_at" timestamp
);

CREATE TABLE "articles" (
  "id" serial PRIMARY KEY,
  "title" varchar(255),
  "body" text,
  "category" varchar(255),
  "created_at" timestamp,
  "user_id" integer
);

CREATE TABLE "comments" (
  "id" serial PRIMARY KEY,
  "body" text,
  "user_id" integer,
  "article_id" integer,
  "created_at" timestamp
);

CREATE TABLE "likes" (
  "id" serial PRIMARY KEY,
  "user_id" integer,
  "article_id" integer,
  "created_at" timestamp
);

COMMENT ON COLUMN "articles"."body" IS 'Content of the post';

ALTER TABLE "articles" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "comments" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "comments" ADD FOREIGN KEY ("article_id") REFERENCES "articles" ("id");

ALTER TABLE "likes" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "likes" ADD FOREIGN KEY ("article_id") REFERENCES "articles" ("id");
