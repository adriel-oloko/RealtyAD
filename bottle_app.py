from bottle import run, route, request, response,  jinja2_template, static_file, error, redirect, TEMPLATE_PATH, default_app

import sqlite3, types

import mysql.connector
from mysql.connector import Error

import itertools
import statistics
from statistics import mode

from datetime import datetime, timezone

import requests, ssl
import json

import time
import random
import os
import csv

import hashlib

TEMPLATE_PATH.append('/home/realestatead/mysite/')

@route('/')
def home():
    return jinja2_template('index.html')

@route('/about-us')
def about_us():
    return jinja2_template('page.html')

@route('/admin')
def admin():
    return jinja2_template('admin.html')

@route('/listings')
def listings():
    connection = sqlite3.connect('/home/realestatead/mysite/estate.db')
    cursor = connection.cursor()
    if not request.query_string:
        page = 0
    else:
        page = int(request.query_string)

    start, end = (page*8), (page+1)*8
    cursor.execute('SELECT * FROM listings ORDER BY id DESC LIMIT ?, 8', (start, ))
    data = cursor.fetchall()

    cursor.execute('SELECT COUNT(*) FROM listings')
    count = cursor.fetchone()[0]

    kwargs = {
        'data': data,
        'count': count,
        'page': page,
        'rem': int(count)%4,
        'has_next': end < count,
		'query_string': '?'+request.query_string,
    }

    connection.close()
    return jinja2_template('property_sales.html', **kwargs)

@route('/listing/<hash>')
def listing(hash):
    connection = sqlite3.connect('/home/realestatead/mysite/estate.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM listings WHERE list_hash = ?', (hash, ))
    data = cursor.fetchone()

    cursor.execute('SELECT link FROM images WHERE p_id = ?', (data[0], ))
    images = cursor.fetchall()
    img = []
    for im in images:
        img.append(im[0])

    images = img
    cursor.execute('SELECT COUNT(*) FROM listings')
    count = cursor.fetchone()[0]

    kwargs = {
        'data': data,
        'count': count,
        'images': images,
        'rem': int(count)%4,
    }
    connection.close()
    return jinja2_template('listing.html', **kwargs)

@route('/image-upload', method="POST")
def image_upload():
    img = request.files.get('file')
    #img.filename = str(hash)+'.jpg'

    img.save('/home/realestatead/mysite/images/', overwrite=True) # appends upload
    #return (True)

@route('/upload', method='post')
def upload():
    connection = sqlite3.connect('/home/realestatead/mysite/estate.db')
    cursor = connection.cursor()
    now = datetime.now()

    hash = bytes(str(now.timestamp()), encoding='utf-8')
    hash = hashlib.md5(hash).hexdigest()
    street = request.forms.get('street')
    area = request.forms.get('area')
    state = request.forms.get('state')
    price = format(int(request.forms.get('price')), ',')
    property_type = request.forms.get('property_type')
    bedroom = request.forms.get('bedroom')
    bathroom = request.forms.get('bathroom')
    toilet = request.forms.get('toilet')
    parking = request.forms.get('parking')

    img_list = request.forms.get('img_list')
    img_list = img_list.split(',')
    address = street+', '+area+', '+state
    added_date = str(now.strftime("%b %d, %Y"))
    status = 'Availaible'
    cursor.execute('INSERT INTO listings (list_hash, list_address, list_street, list_area, list_state, list_price, list_property_type, list_building_type, list_bedroom, list_bathroom, list_toilet, list_parking, list_added_date, list_status, list_img) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (hash, address, street, area, state, price, property_type, property_type, bedroom, bathroom, toilet, parking, added_date, status, img_list[0]))
    connection.commit()

    cursor.execute('SELECT id FROM listings ORDER BY id DESC')
    p_id = cursor.fetchone()[0]

    for img in img_list:
        cursor.execute('INSERT INTO images (p_id, link) VALUES (?, ?)', (p_id, img))
        connection.commit()

    connection.close()
    redirect('/listings')

@route('/mailer', method='POST')
def mailer():
    return (True)

@error(404)
@error(500)
def error(error):
    return static_file('error.html', root='/home/realestatead/mysite/')

@route('/<filetype>/<file>')
def static_i(filetype, file):
    return static_file(file, root='/home/realestatead/mysite/'+filetype+'/')

@route('/<filetype>/<fle>/<file>')
def static_ii(filetype, fle, file):
    return static_file(file, root='/home/realestatead/mysite/'+filetype+'/'+fle+'/')

#run(reloader=True, debug=True)
application = default_app()