import pandas as pd

salesinvoiceData = pd.read_csv("/Users/shanlin/Downloads/RPA_Invoice/Pending/Merged_files.csv") #Change the directory

import mysql.connector as msql
from mysql.connector import Error

try:
    conn = msql.connect(host='s123456.mysql.database.azure.com', database='local_db', user='myadmin', password='S123456@')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS sales_invoice;')
        print('Creating table....')
        # in the below line please pass the create table statement which you want #to create
        cursor.execute(
            "CREATE TABLE sales_invoice(Invoice_no varchar(255),Bill_to varchar(255),undefined_Date_undefined varchar(255),Type varchar(255),Status varchar(255),Amount varchar(255),Paid_amount varchar(255),Currency varchar(255),Group_customer varchar(255),Pay_by varchar(255),Payment_terms varchar(255),undefined_Due_Date_Basis_undefined varchar(255), Site varchar(255),Project varchar(255),Sales_rep_1 varchar(255),Cancellation_status varchar(255))")
        print("Table is created....")
        # loop through the data frame
        for i, row in salesinvoiceData.iterrows():
            # here %S means string values
            sql = "INSERT INTO local_db.sales_invoice VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
