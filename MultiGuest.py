#!/usr/bin/env python3

import sys, yaml#, json
import subprocess as sbp
from time import sleep

def Multiguest(var):
    for i in range(5):
        # T
        sbp.Popen(f"adb shell input tap {var['T'][0]} {var['T'][1]}",shell=True,stdout=sbp.PIPE)
        sleep(var['sleeptime'])
        # Y
        sbp.Popen(f"adb shell input tap {var['Y'][0]} {var['Y'][1]}",shell=True,stdout=sbp.PIPE)
        sleep(var['sleeptime'])
        # Space
        sbp.Popen(f"adb shell input tap {var['Space'][0]} {var['Space'][1]}",shell=True,stdout=sbp.PIPE)
        sleep(var['sleeptime'])
        # Space
        sbp.Popen(f"adb shell input tap {var['Space'][0]} {var['Space'][1]}",shell=True,stdout=sbp.PIPE)
        sleep(var['sleeptime'])
        # U
        sbp.Popen(f"adb shell input tap {var['U'][0]} {var['U'][1]}",shell=True,stdout=sbp.PIPE)
        sleep(var['sleeptime'])
    # X
    sbp.Popen(f"adb shell input tap {var['X'][0]} {var['X'][1]}",shell=True,stdout=sbp.PIPE)
    sleep(var['sleeptime'])
    

if __name__ == '__main__':

    try:
        platform = sys.argv[1]
    except KeyboardInterrupt:
        sys.exit()
    except:
        sys.exit(
"""MultiGuest 1.0.0\n\n\
Usage: MultiGuest.py <platform>\n\n\
platforms:\n  emu\n  cel"""
        )
    else:
        if platform == 'emu':
            # file = "variables.json"
            file = "variables.yml"
        elif platform == 'cel':
            # file = "varcel.json"
            file = "varcel.yml"
        else:
            sys.exit(
"""MultiGuest 1.0.0\n\n\
Usage: MultiGuest.py <platform>\n\n\
platforms:\n  emu\n  cel"""
            )

        with open(file, 'r') as fp:
            # var = json.load(fp)
            var = yaml.safe_load(fp)
        try:
            while True:
                Multiguest(var)
        except KeyboardInterrupt:
            sys.exit()
