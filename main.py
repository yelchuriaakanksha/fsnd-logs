#!/usr/bin/env python

import psycopg2

DATA_BASE = "news"


def connect(que):
    data = psycopg2.connect(database=DATA_BASE)
    hov = data.cursor()
    # Execution
    hov.execute(que)
    # Fetch output
    outputs = hov.fetchall()
    data.close()
    return outputs

# Question 1. What are the most popular three articles of all time?

que1 = ''' SELECT title, count(log.path) as views FROM articles INNER JOIN log ON
        concat('/article/', articles.slug) = log.path
        where articles.slug = substring(log.path, 10)
        GROUP BY title ORDER BY views desc LIMIT 3; '''


def articles3(que):
    outputs = connect(que)
    try:
        print('\n Three most popular articles are:\n')
        if(outputs):
            for res in outputs:
                tit = res[0]
                cnt = res[1]
                tup = (tit, cnt)
                if (tup):
                    print('\t' + str(tit) + ' - ' + str(cnt) + " views")
                else:
                    print("Error")
            print("=========================================================")

    except Exception as Failed:
            print(Failed)
# Question 2. Who are the most popular four article authors of all time?


que2 = '''
            SELECT name, count(*) AS views
                 from authors INNER JOIN  articles
                 ON authors.id = articles.author
                 INNER JOIN log
                 ON log.path = concat('/article/', articles.slug)
                 GROUP BY name
                 ORDER BY views
                 desc LIMIT 4;
       '''


def authors_popular4(que):
    try:
        outputs = connect(que)
        print('\n Four most popular authors are:\n')
        if(outputs):
            for res in outputs:
                tit = res[0]
                cnt = res[1]
                tup = (tit, cnt)
                if (tup):
                    print("\t {} - {} views ".format(tit, cnt))

                else:
                    print("Error")
            print("=========================================================")
    except Exception as Failed:
            print(Failed)
# Question 3. On which days did more than 1% of requests lead to errors?

que3 = '''
    SELECT date(time) as dt,
    (100.0 * error_log.qtd / request_log.qtd) AS perc
    FROM log
    JOIN (SELECT date(time) AS de, count(*) AS qtd
            FROM log WHERE status != '200 OK' GROUP BY de) AS error_log
    ON date(log.time) = error_log.de
    JOIN (SELECT date(time) AS ds, count(*) AS qtd
        FROM log GROUP BY ds) AS request_log
    ON date(log.time) = request_log.ds
    WHERE ((100.0 * error_log.qtd) / request_log.qtd) > 1.0
    GROUP BY dt, perc;
    '''


def log_errors1(que):
    try:
        outputs = connect(que)
        print('\n Days with more than 1% of requests leads to error are:\n')
        if(outputs):
            for res in outputs:
                tit = res[0]
                cnt = res[1]
                tup = (tit, cnt)
                if (tup):
                    print('\t' + str(tit) + ' - ' + str(cnt) + " views")
                else:
                    print("Error")
            print("=========================================================")
    except Exception as Failed:
            print(Failed)

if __name__ == '__main__':
    articles3(que1)
    authors_popular4(que2)
    log_errors1(que3)
