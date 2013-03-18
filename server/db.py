#coding=utf8
import config

def listing(**k):
    return config.DB.select('news', order='created desc', **k)

def counting():
    return config.DB.query('select count(*) as count from news')[0].count
