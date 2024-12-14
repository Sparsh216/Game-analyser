'''
System configurations
'''
import multiprocessing


CPU_THRESHOLD = 90


class System:
    '''
    System configurations
    '''

    class Server:
        '''
        API server configurations
        '''
        HOST = '0.0.0.0'
        PORT = 8080
        WORKERS = int((multiprocessing.cpu_count() * CPU_THRESHOLD)/100)
