
#!/usr/bin/env python

# parse qq chat text

QQTXT = '/home/jzh/corpus/qq/chaguan02.html'

keys = ['228219579', '746525371', '38035354', '30173423', '619511600']

def main():
    with open(QQTXT) as fp:
        for line in fp:
            ss = line.split("<br/><br/>")
            for s in ss:
                if any(i in s for i in keys):
                    s = s.replace('&nbsp;', ' ')
                    s = s.replace('<br/>', ' ')
                    t = s.split(' ')
                    t = t[3:]
                    for x in t:
                        if any(i in x for i in keys):
                            print('\n')
                        print (x)    

if __name__ == '__main__':
    main()
