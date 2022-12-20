import json
import random
import string
import sys

import psycopg2
from confluent_kafka.serialization import StringSerializer
from kafka import KafkaProducer
# from caphca.etl.employee import Employee

employee_topic_name = "employee_cdc"

class CaphcaProducer:
    def __init__(self, host="localhost", port="29092"):
        self.host = host
        self.port = port
        self.producer = KafkaProducer(bootstrap_servers=('%s:%s' % (self.host, self.port)))

    def producer_msg(self, topic_name, key, value):
        self.producer.send(topic=topic_name, key=key, value=value).get(timeout=5)

def read_employee():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres",
            port = '5432')
        conn.autocommit = True

        # create a cursor
        cur = conn.cursor()
        result = cur.execute(
            "select * from employees_cdc order by emp_id limit 1")
        # result2 =
        conn.commit()
        for i in cur:
            print(i)
            return(i)
        # if result:
        #     cur.execute("delete from employees_cdc where emp_id = (select min(emp_id) from employees_cdc) on conflict do nothing")
        #     return result
    except Exception as e:
        print(e)
    finally:
        print(result)
        cur.close()

if __name__ == '__main__':
    producer = CaphcaProducer()
    i = 0
    while i<50:
        i+=1
        emp = read_employee()
        if emp:
            producer.producer_msg(employee_topic_name, key=str(emp[0]).encode(), value=','.join(emp[1:]).encode())
