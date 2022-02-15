import multiprocessing
import os

process1 = ('main.py')
process2 = ('browser.py')

def execute(process):
    os.system(f'python {process}')

process_pool = multiprocessing.Pool(processes= 2)
process_pool.map(execute, process1)
process_pool.map(execute, process2)
