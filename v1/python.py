import sys
import time
import json
if __name__=='__main__':
    target = sys.argv[1]
    for i in xrange(int(target)):
        time.sleep(0.001)
        sys.stdout.write(json.dumps({'data': i}))
        sys.stdout.flush()
