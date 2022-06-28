import os
import os.path
#import re
from Partition import *

class PartitionManagerException(Exception):
    def __init__(self, partitions : str, *args):
        super().__init__(args)
        self.__partitions = partitions

    def __str__(self):
        return f'Partitions: {self.__partitions} is not found'

#Singleton
class PartitionManager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return  cls.__instance

    def __init__(self) -> None:
        self.__proj_dir = None
        self.__proj_name = None
        self.__partitions = list()
        self.__partitions.append(Partition()) #create bootloder partition
        self.__partitions.append(Partition()) #create partition-table partition

    def setPartitionTableOffset(self, offset):
        self.__partitions[1].offset = offset

    def setBootloaderOffset(self, offset):
        self.__partitions[0].offset = offset

    def setBootloaderSize(self, size):
        self.__partitions[0].len = size

    def setProjDir(self, project_dir):
        self.__proj_dir = project_dir + '/'
        os.chdir(project_dir)
        with open(str(self.__proj_dir) + "CMakeLists.txt", 'r') as f:
            CMakeLists_file = f.read()
            r = re.search(r'project\((\w+)\)', CMakeLists_file)
            self.__proj_name = r.group(1)

    def findPartitions(self):
        f_bl = str(self.__proj_dir) + "build/bootloader/bootloader.bin"
        if os.path.isfile(f_bl) != True:
            raise PartitionManagerException('bootloader.bin was not found')

        self.__partitions[0].name = 'bootloader.bin'
        self.__partitions[0].path = str(self.__proj_dir) + 'build/bootloader/'

        f_pt = str(self.__proj_dir) + "build/partition_table/partition-table.bin"
        if os.path.isfile(f_pt) != True:
            raise PartitionManagerException('partition-table.bin was not found')

        self.__partitions[1].name = 'partition-table.bin'
        self.__partitions[1].path = str(self.__proj_dir) + 'build/partition_table/'

        with open(str(self.__proj_dir) + 'partitions.csv', 'r') as partitions:
            for line in partitions:
                if line[0] == '#':
                    continue

                partit = Partition()
                
                part_data       = re.findall(r'\w+', line)
                partit.name     = part_data[0]
                partit.offset   = part_data[3]
                partit.len      = part_data[4]

                if (partit.name == 'nvs' or partit.name == 'phy_init' or partit.name == 'ota_0' or partit.name == 'ota_1'):
                    if (partit.name == 'nvs'):
                        self.__partitions[1].len = hex(int(partit.offset, 16) - int(self.__partitions[1].offset, 16))
                    partit.path = None
                elif (partit.name == 'otadata'):
                    partit.name = 'ota_data_initial.bin'
                    partit.path = str(self.__proj_dir) + 'build/'
                elif (partit.name == 'factory'):
                    partit.name = self.__proj_name + '.bin'
                    partit.path = str(self.__proj_dir) + 'build/'
                else:
                    partit.name = partit.name + '.bin'
                    partit.path = str(self.__proj_dir) + 'build/'
                    if os.path.isfile(partit.path + partit.name) != True:
                        partit.path = None

                if partit.path != None:
                    if os.path.isfile(partit.path + partit.name) != True:
                        raise PartitionManagerException(f'{partit.name} was not found')

                self.__partitions.append(partit)

    def makeBinary(self, out_filename):
        outdata = bytearray()
        outdata.extend(bytes().ljust(int(self.__partitions[0].offset, 16), b'\xFF'))

        for item in self.__partitions:
            if item.path == None:
                outdata.extend(bytes().ljust(int(item.len, 16), b'\xFF'))
            else:
                with open(item.path + item.name, 'rb') as f:
                    fdata=f.read()
                    outdata.extend(fdata)
                    extra_dummy_size = int(str(item.len), 16) - len(fdata)
                    outdata.extend(bytes().ljust(extra_dummy_size, b'\xFF'))

        f_name = out_filename[0] + '.bin'
        print(f_name)
        with open(f_name, 'wb') as out:
            out.write(outdata)        