import os

def memory_data(file_path, limit=10000000):
    # limit 10Mb
    file_size = os.path.getsize(file_path)
    unit = 'Bytes'

    if file_size > limit: 
        return None, {'msg': 'error: max file size is 10Mb'}
    
    if file_size < 10**6:
        unit = 'Bytes'
        filesize = file_size
    elif file_size < 10**9:
        unit = 'Kb'
        filesize = file_size*10**-3
    elif file_size < 10**12:
        nit = 'Mb'
        filesize = file_size*10**-6
    elif file_size < 10**15:
        unit = 'Gb'
        filesize = file_size*10**-9
    else:
        unit = 'Tb'
        filesize = file_size*10**-12
        
    return {'memory': f'{filesize}', 'unit': f'{unit}'}, None
    

