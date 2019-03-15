-- To create VIEW log_slug
create or replace view article_log as
select title, count(title) from articles,log
where log.status like '%200%'
group by log.path, articles.title;

-- To create VIEW authors_name
create view authname_logs AS
SELECT title, name, author, bio
FROM articles, authors
WHERE articles.author = authors.id;


CREATE VIEW artviews_logs AS
SELECT author, count(log.id), count(title) as views
FROM articles, log
WHERE path<>'/' AND status ='200 OK'
GROUP BY articles.author
ORDER BY views desc;