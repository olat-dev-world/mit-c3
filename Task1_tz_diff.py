# importing datetime module
from datetime import timezone 
import datetime 

# Convert string to date
def convert(dtime):
    format = '%a %d %b %Y %H:%M:%S  %z'
    datetime_str = datetime.datetime.strptime(dtime, format)
    return datetime_str

def timeDiff_sec(timeDiff):
    time_secs = 0
    tdays = str(timeDiff).split(',')
    print(tdays)
    for i in tdays:
        if "day" in i:
            time_secs += int(i.split(' ')[0])*24*3600
        else:
            ts = i.split(":")
            time_secs += int(ts[0])*3600 + int(ts[1])*60 + int(ts[2])
    return time_secs

def timeDiff(t1,t2):
    t_diff = convert(t1) - convert(t2)
    t_diffsec = timeDiff_sec(t_diff)
    return str(t_diffsec)

def main():

    t1 = 'Sat 02 May 2015 19:54:36 +0530' #Dec 4 2024 10:07AM
    t2 = 'Fri 01 May 2015 13:54:36 -0000'
    t_diff = timeDiff(t1,t2)
    print(t_diff)
if __name__ == "__main__":
    main()