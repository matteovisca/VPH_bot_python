import matplotlib.pyplot as plt
import json
from datetime import datetime
import csv

from os import listdir
from os.path import isfile, join
import core.DEF as DEF
import time
import platform

header = ['time', 'spCella', 'pvCella', 'pvCellaSonda', 'spPress', 'pvPress']

def select_path(bench):
    path_log_source = ''
    if bench == DEF.BENCH_VBA.PULSANTE:
        path_log_source = DEF.PATH.PATH_LOG_387
    if bench == DEF.BENCH_VBA.SCOPPIO:
        path_log_source = DEF.PATH.PATH_LOG_511
    if bench == DEF.BENCH_VBA.CIRCOLAZIONE_A:
        path_log_source = DEF.PATH.PATH_LOG_470_A
    if bench == DEF.BENCH_VBA.CIRCOLAZIONE_B:
        path_log_source = DEF.PATH.PATH_LOG_470_B
    if bench == DEF.BENCH_MF.MF_AP:
        path_log_source = DEF.PATH.PATH_LOG_449
    if bench == DEF.BENCH_MF.MF_BP:
        path_log_source = DEF.PATH.PATH_LOG_449_B

    return path_log_source


def concat_log(typeLog, bench):
    path_log_source = select_path(bench)

    if platform.platform().__contains__('macOS'):
        path_log_source = DEF.PATH.PATH_LOG_LOCAL

    onlyFiles = []
    myList = listdir(path_log_source)
    myList.sort()
    for f in myList:
        if isfile(join(path_log_source, f)) and f.__contains__(typeLog) :
            onlyFiles.append(f)
            print(onlyFiles)
    with open('sample.txt', 'w') as outfile:
        for fname in onlyFiles:
            with open(path_log_source + fname) as infile:
                for line in infile:
                    outfile.write(line)
    print('File sample.txt created....')

def read_dataLogLs(pathFile, filename):
    time = []
    temperature = []
    pressure = []
    rows = []
    result = []
    maxpressure:float = 0
    for line in open(pathFile + filename, 'r'):
        lines = [i for i in line.split()]
        data = json.loads(lines[4])
        app_data = lines[1][:8]
        my_time_date = lines[0] + ' ' + app_data
        time.append( datetime.strptime(my_time_date, '%Y-%m-%d %H:%M:%S'))
        temperature.append(float(data['pvTCe']))
        pressure.append(float(data['pvTUp']))
        if float(data['pvTUp']) > maxpressure:
            maxpressure = float(data['pvTUp'])
        row = [
            my_time_date,
            float(data['spTCe']),
            float(data['pvTCe']),
            float(data['pvtR1']),
            float(data['spTFl']),
            float(data['pvTUp'])
        ]
        rows.append(row)

    result.append(time)
    result.append(temperature)
    result.append(pressure)
    result.append(rows)
    return result

def read_dataLogHs(pathFile, filename):
    timeArr = []
    temperature = []
    pressure = []
    rows = []
    result = []
    offset = 0
    intervallo = 1800
    durata = 60
    abil_save = False
    time_end = 0
    line_array = []

    #app_time:datetime = datetime.now()
    time_start = time.time()
    # for line in open(pathFile + filename, 'r'):
    #     line_array.append(line)

    print(
        "%.4f"
        % (time.time() - time_start)
    )
    time_start = time.time()
    # for line in line_array:
    count_total_lines = 0
    for line in open(pathFile + filename, 'r'):
        count_total_lines = count_total_lines + 1
        cols = [i for i in line.split()]
        my_time_date = cols[0] + ' ' + cols[1][:8]
        app_datetime = datetime.strptime(my_time_date, '%Y-%m-%d %H:%M:%S')
        seconds = get_seconds(app_datetime)
        #print(seconds)
        if (seconds - offset) % intervallo == 0:
            # abil_save = True
            time_end = seconds + durata

        # if abil_save and seconds <= time_end:
        if seconds <= time_end:
            data = json.loads(cols[4])
            timeArr.append(app_datetime)
            temperature.append(float(data['pvPDn']))
            pressure.append(float(data['pvPUp']))
            row = [
                my_time_date,
                float(data['spPr']),
                float(data['pvPUp']),
                float(data['pvPDn']),
            ]
            rows.append(row)
        # else:
        #     abil_save = False
    print(
        "%.6f : righe_estratte=%i : righe_totali=%i "
        % (time.time() - time_start, len(rows), count_total_lines)
    )
    result.append(time)
    result.append(temperature)
    result.append(pressure)
    result.append(rows)
    return result

def get_seconds(date):
    return date.hour * 3600 + date.minute * 60 + date.second

def draw_graph(data_objects):
    plt.title("Pressure graph")
    fig, ax1 = plt.subplots()
    fig.set_size_inches(15, 10)
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_axes([0.2, 0.18, 0.6, 0.3])
    ax1.plot(data_objects[0], data_objects[1], 'g')
    ax2.plot(data_objects[0], data_objects[2], 'r-')
    ax1.set_ylim(25, 85)
    ax2.set_ylim(0.75, 3.12)
    ax1.set_xlabel('time')
    ax1.set_ylabel('temperature')
    ax2.set_ylabel('pressure')
    fig.savefig('testteo.png')

def try_this(typeLog):
    concat_log(typeLog, '387')
    return draw_graph(read_dataLogLs('','sample.txt'))

def write_csv(name, dataHeader, dataRows):
    with open(name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(dataHeader)
        writer.writerows(dataRows)

def scrivi_csv(typeLog, bench, filename):
    concat_log(typeLog, bench)
    if typeLog == 'lsData':
        my_data = read_dataLogLs('', 'sample.txt')
    else:
        my_data = read_dataLogHs('', 'sample.txt')
    write_csv(filename, header, my_data[3])





