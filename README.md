# Log-Analysis Project
### By Yelchuri Aakanksha

## About

This is the third project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, and authors as well as the web server log for the site.

## What it is

A Reporting page that prints out reports in a plain text format based on the data in the database.This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Installation

There are some dependancies and a few instructions on how to run the application.

## Requirements

1. Python
2. Vagrant
3. VirtualBox

## Dependencies

- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install VirtualBox & Vagrant
2. Clone the Udacity Vagrantfile
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Exit one directory by using commannd: cd ..
6. Exit again one directory:cd ..
7. Navigate to `cd vagrant` as instructed in terminal

## How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/Log-Analysis`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using the command:
  
  ```
    $ vagrant up
  ```
  2. Then Log into this using command:
  
  ```
    $ vagrant ssh
  ```

  4. The command line will now start with vagrant. Here cd into the /vagrant folder.
  
  5. In terminal Change directory to `vagrant/` and look around with ls.
  
  6. All the tables are present in newsdata.sql.
  
  7. To load the data into local database type 
  
  ```
	$ psql  -d news -f newsdata.sql
  ```

  8. To run the database type 
  
  ```
	$ psql -d news
  ```
  
  9. Load the data in local database using the command:

  ```
    $ psql -d news -f newsdata.sql
  ```
  
  10.Load the views into database using the command:
  ```
    $ psql -d news -f view.sql
  ```
  
  11. Run main.py using:
  
  ```
    $ python main.py
  ``` 
  The database includes three tables:
- Authors table
- Articles table
- Log table

  ## Project content

This project consists for the following files are:

* main.py - main file to run this Logs Analysis Reporting tool
* README.md - instructions to install this reporting tool
* view.sql - database file
* logopt.png

##  Create Views

Views were created to answer the  queries in the project with the purpose of leaving the original database unchanged. They also helped break the question down into comprehensible portions.

### The first view code is as follows:
			create or replace view article_log as
			select title, count(title) from articles,log
			where log.status like '%200%'
			group by log.path, articles.title;


### The second view code is as follows:
			create view authname_logs AS
			SELECT title, name, author, bio
			FROM articles, authors
			WHERE articles.author = authors.id;


			CREATE VIEW artviews_logs AS
			SELECT title, count(log.id), count(title) as views
			FROM articles, log
			WHERE path<>'/' AND status ='200 OK'
			GROUP BY articles.title
			ORDER BY views desc;

### There is no view for third Query.

### Troubleshooting
If your command prompt does not start with vagrant after typing vagrant ssh then please try the winpty vagrant ssh on your Windows system.

### Output
![logopt.png](https://github.com/yelchuriaakanksha/fsnd-logs/blob/master/logopt.png)


