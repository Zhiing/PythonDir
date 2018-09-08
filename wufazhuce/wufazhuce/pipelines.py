# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class WufazhucePipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('./wufazhuce.db')
        self.cursor = self.conn.cursor()

        # self.create_table()

    def process_item(self, item, spider):
        print(item)
        insert_photo = item.get('photo_id')
        insert_article = item.get('article_id')
        insert_question = item.get('question_id')

        if insert_photo is not None:
            self.insert_photo(item)
            return item
        if insert_article is not None:
            self.insert_article(item)
            return item
        if insert_question is not None:
            self.insert_question(item)
            return item
        print('''
        #############  ERROR  #############
        ''')

    def insert_photo(self, item_data):
        insert_sql = '''
        INSERT INTO photo VALUES ({0},"{1}","{2}","{3}","{4}")
        '''.format(
            item_data.get('photo_id'), item_data.get('photo_url'),
            item_data.get('photo_date'), item_data.get('photo_text'),
            item_data.get('wufazhuce_url'))

        self.cursor.execute(insert_sql)
        self.conn.commit()

    def insert_article(self, item_data):
        insert_sql = '''
        INSERT INTO article VALUES ({0},"{1}","{2}","{3}","{4}")
        '''.format(
            item_data.get('article_id'), item_data.get('article_title'),
            item_data.get('article_author'), item_data.get('article_text'),
            item_data.get('article_body'))

        self.cursor.execute(insert_sql)
        self.conn.commit()

    def insert_question(self, item_data):
        insert_sql = '''
        INSERT INTO question VALUES ({0},"{1}","{2}","{3}")
        '''.format(
            item_data.get('question_id'), item_data.get('question_title'),
            item_data.get('question_text'), item_data.get('question_body'))

        self.cursor.execute(insert_sql)
        self.conn.commit()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE photo (
                photo_id INT PRIMARY KEY NOT NULL,
                photo_url TEXT,
                photo_date TEXT,
                photo_text TEXT,
                wufazhuce_url TEXT
            );
            ''')
        self.cursor.execute('''
            CREATE TABLE article (
                article_id INT PRIMARY KEY NOT NULL,
                article_title TEXT,
                article_author TEXT,
                article_text TEXT,
                article_body TEXT
            );
            ''')
        self.cursor.execute('''
            CREATE TABLE question (
                question_id INT PRIMARY KEY NOT NULL,
                question_title TEXT,
                question_text TEXT,
                question_body TEXT
            );
            ''')
        self.conn.commit()
        self.conn.close()
