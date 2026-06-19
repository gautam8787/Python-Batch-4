# modules in Python : module is python file(.py) which contains classes , methods , variables that can be used in another program or module 
'''
class sample:
    name = "sairam"
    def demo(self):
        print(name)   # sairam
    

name ="Rocky"
print(name)


obj =sample()
obj.demo()
'''
# why modules ?? 
# organise code 
# easy maintainence 
# resuablity
# individual development 

'''
# inbuilt modules
import math

print(math.factorial(5))
print (int(math.sqrt(81)))


import random

print(random.randint(1000,9999))
print(random.choice(["sairam","sumit","sai","deepika"]))


import datetime

today = datetime.datetime.now()
print(today)


import sys
print(sys.version)




# user defined 
# import operations
from operations import demo

a = int(input("enter a value : "))
b = int(input("enter b value : "))

obj=demo()

option = int(input(' enter 1 for addition ,  enter 2 for subtraction ,  enter 3 for multiplication , enter 4 for division'))
if option ==1:
    print(obj.add(a,b))

elif option ==2:
    print(obj.sub(a,b))

elif option ==3:
    print(obj.mul(a,b))

elif option ==4:
    print(obj.div(a,b))

else:
    print("you have choosen wrong option.")



# help("modules")
__future__          _stat               fileinput           rlcompleter
__hello__           _statistics         fnmatch             runpy
__phello__          _string             fractions           sched
_abc                _strptime           ftplib              secrets
_aix_support        _struct             functools           select
_android_support    _suggestions        gc                  selectors
_apple_support      _symtable           genericpath         shelve
_ast                _sysconfig          getopt              shlex
_ast_unparse        _thread             getpass             shutil
_asyncio            _threading_local    gettext             signal
_bisect             _tkinter            glob                site
_blake2             _tokenize           graphlib            smtplib
_bz2                _tracemalloc        gzip                socket
_codecs             _types              hashlib             socketserver
_codecs_cn          _typing             heapq               sqlite3
_codecs_hk          _uuid               hmac                sqlparse
_codecs_iso2022     _warnings           html                sre_compile
_codecs_jp          _weakref            http                sre_constants
_codecs_kr          _weakrefset         idlelib             sre_parse
_codecs_tw          _winapi             imaplib             ssl
_collections        _wmi                importlib           stat
_collections_abc    _zoneinfo           inspect             statistics
_colorize           _zstd               io                  string
_compat_pickle      abc                 ipaddress           stringprep
_contextvars        annotationlib       itertools           struct
_csv                antigravity         json                subprocess
_ctypes             argparse            keyword             symtable
_datetime           array               linecache           sys
_decimal            asgiref             locale              sysconfig
_elementtree        ast                 logging             tabnanny
_functools          asyncio             lzma                tarfile
_hashlib            atexit              mailbox             tempfile
_heapq              base64              marshal             textwrap
_hmac               bdb                 math                this
_imp                binascii            mimetypes           threading
_interpchannels     bisect              mmap                time
_interpqueues       builtins            modulefinder        timeit
_interpreters       bz2                 modules             tkinter
_io                 cProfile            msvcrt              token
_ios_support        calendar            multiprocessing     tokenize
_json               cmath               netrc               tomllib
_locale             cmd                 nt                  trace
_lsprof             code                ntpath              traceback
_lzma               codecs              nturl2path          tracemalloc
_markupbase         codeop              numbers             tty
_md5                collections         opcode              turtle
_multibytecodec     colorsys            operator            turtledemo
_multiprocessing    compileall          optparse            types
_opcode             compression         os                  typing
_opcode_metadata    concurrent          pathlib             tzdata
_operator           configparser        pdb                 unicodedata
_osx_support        contextlib          pickle              unittest
_overlapped         contextvars         pickletools         urllib
_pickle             copy                pip                 uuid
_py_abc             copyreg             pkgutil             venv
_py_warnings        csv                 platform            warnings
_pydatetime         ctypes              plistlib            wave
_pydecimal          curses              poplib              weakref
_pyio               dataclasses         posixpath           webbrowser
_pylong             datetime            pprint              winreg
_pyrepl             dbm                 profile             winsound
_queue              decimal             pstats              wsgiref
_random             difflib             pty                 xml
_remote_debugging   dis                 py_compile          xmlrpc
_sha1               django              pyclbr              xxsubtype
_sha2               doctest             pydoc               zipapp
_sha3               email               pydoc_data          zipfile
_signal             encodings           pyexpat             zipimport
_sitebuiltins       ensurepip           queue               zlib
_socket             enum                quopri              zoneinfo
_sqlite3            errno               random              
_sre                faulthandler        re                  
_ssl                filecmp             reprlib  

'''

# In built modules :

import math

print(math.ceil(22.9))  # round numbers to nearest largest number 
print(math.floor(22.9))   # round numbers to nearest smallest number 

print(abs(-10))
print(math.fabs(-10.3))

print(math.factorial(5))
print(math.sqrt(81))


import random

print(random.randint(1000,9999))

print(random.random())

print(random.choice([1,45,65,67,89,90,34,55,65]))

print(random.sample([1,45,65,67,89,90,34,55,65],3))

print(random.sample(["sai","ram","sumit","deepika","gautum"],3))


import datetime

today = datetime.datetime.now()
print(today)


print(dir(datetime))


# library ---> packages --> modules ---> classes ---> methods , attribuites(variables)


