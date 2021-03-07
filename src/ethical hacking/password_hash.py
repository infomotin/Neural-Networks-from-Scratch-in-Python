import optparse
import zipfile
from threading import Thread


def extract_zip(zfile, password):
    try:
        zfile.extractall(pws=password)
        print("[+] Password Found: " + password + '\n')
    except:
        pass


def main():
    parser = optparse.OptionParser(" usage %prog")+"-f <zipfile> -d <dictionary>")
