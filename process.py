#!/usr/bin/env python
# -*- coding:utf-8 -*-
#This project is used for pre-process the multispectral data of VAST 2017 Mini Challenge 3

import csv
import cv2
import os
import numpy as np

def read_csv_file(filename):
    filepath = "Data/"+filename
    with open(filepath, 'rb') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def gene_single_band_img(data_list):
    width = 651
    height = 651
    channels = 1
    image_list = []
    for i in range(7):
        img = np.zeros((width, height,channels), np.uint8)  # generate a gray image
        image_list.append(img)
    for row in data_list:
        if(row[0] == 'X'):continue
        x = int(row[0])
        y = int(row[1])
        for i in range(6):
            index = i + 2
            image_list[i][y,x] = row[index]
    return image_list

def gene_ndvi_img(data_list):
    width = 651
    height = 651
    channels = 1
    img = np.zeros((width, height, channels), np.uint8)  # generate a gray image
    for row in data_list:
        if(row[0] == 'X'):continue
        x = int(row[0])
        y = int(row[1])
        offset = 2
        dnvi = 0
        if(row[3+offset] != '0' or row[2+offset] != '0'):
            dnvi = (float(row[3+offset])-float(row[2+offset]))/(float(row[3+offset])+float(row[2+offset]))
        dnvi = (dnvi+1)/2*255
        img[y,x] = int(dnvi)
    return img

def gene_rgb_img(data_list, path_prefix):
    width = 651
    height = 651
    channels = 3
    offset = 2
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if(i!=j and i!=k and j!=k):
                    img = np.zeros((width, height, channels), np.uint8)  # generate a gray image
                    for row in data_list:
                        if (row[0] == 'X'): continue
                        x = int(row[0])
                        y = int(row[1])
                        # access a pixel from red channel
                        img.itemset((y, x, 2), row[i+offset])
                        # access a pixel from green channel
                        img.itemset((y, x, 1), row[j+offset])
                        # modify a pixel from blue channel
                        img.itemset((y, x, 0), row[k+offset])
                    filename = "b"+str(i+1)+"b"+str(j+1)+'b'+str(k+1)+".jpg"
                    cv2.imwrite(path_prefix+filename,img)
                    print filename+" saved."

if __name__ == '__main__':
    filename_list = ['image01_2014_03_17.csv','image02_2014_08_24.csv','image03_2014_11_28.csv','image04_2014_12_30.csv','image05_2015_02_15.csv','image06_2015_06_24.csv','image07_2015_09_12.csv','image08_2015_11_15.csv','image09_2016_03_06.csv','image10_2016_06_26.csv','image11_2016_09_06.csv','image12_2016_12_19.csv']
    for filename in filename_list:
        data_list = read_csv_file(filename)
        date_str = filename[filename.index('_')+1:filename.index('.')]
        result_path_prefix = 'Result/'+date_str
        if not os.path.exists(result_path_prefix):
            os.mkdir(result_path_prefix)
        result_path_prefix = result_path_prefix +"/"
        print 'Start process: '+date_str
        img = gene_ndvi_img(data_list)
        cv2.imwrite(result_path_prefix+"dnvi.jpg",img)
        print 'DNVI image saved.'
        img_list = gene_single_band_img(data_list)
        for i in range(6):
            cv2.imwrite(result_path_prefix+"b"+str(i+1)+".jpg",img_list[i])
        print 'Single band images saved.'
        gene_rgb_img(data_list,result_path_prefix)
        print date_str+" finished.\n"