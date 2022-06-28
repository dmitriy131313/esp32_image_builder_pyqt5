import os
#import struct
import re

srcdir = 'files'
firmware_filename = 'firmware.bin'
start_offset=0x1000
bootloader_size=0x7000




log = open('log.txt', 'w')





os.chdir(srcdir)

partitions = open('partitions.csv', 'r')



writing_file0 = 'bootloader'
outdata = bytearray()

extra_dummy_size = 0


for line in partitions:

    if line[0] == '#':
        continue


    #part_data = re.findall(r'\w+', line)
    part_data = re.findall(r'\w+', line)
    part_name = part_data[0]
    part_type = part_data[1]
    part_subtype = part_data[2]
    part_offset = part_data[3]
    part_size = part_data[4]


    if writing_file0 == 'bootloader':
        writing_file0 = ''

        f=open('bootloader.bin', 'rb')
        outdata.extend(bytes().ljust(start_offset, b'\xFF'))
        outdata.extend(f.read())
        outdata.extend(bytes().ljust(bootloader_size + start_offset - len(outdata), b'\xFF'))
        f.close()

        log.write('bootloader.bin, '+hex(start_offset)+', '+hex(bootloader_size)+'\n')


        f=open('partitions.bin', 'rb')
        outdata.extend(f.read())
        outdata.extend(bytes().ljust(int(part_offset, 16) - len(outdata), b'\xFF'))
        f.close()

        log.write('partitions.bin, '+hex(bootloader_size+start_offset)+', '+hex(int(part_offset, 16) - bootloader_size-start_offset)+'\n')




    outdata_size_before = len(outdata)
    to_read_file=1
    filename=part_name+'_'+part_type+'.bin'

    if part_name == 'nvs' or part_name == 'ota_1':

        filename=part_name
        to_read_file=0

    else:
        if part_name == 'otadata':

            filename='ota_data_initial.bin'
            
        else:
            if part_name == 'ota_0' or part_name == 'ota' or part_name == 'factory':

                filename=firmware_filename

    if to_read_file:

        f=open(filename, 'rb')
        fdata=f.read()
        outdata.extend(fdata)
        f.close()

        extra_dummy_size = int(part_size, 16) - len(fdata)
        outdata.extend(bytes().ljust(extra_dummy_size, b'\xFF'))

    else:

        extra_dummy_size = 0
        outdata.extend(bytes().ljust(int(part_size, 16), b'\xFF'))

        filename += '(dummy 0xFF)'

    log.write(filename+', '+hex(outdata_size_before)+', '+part_size+'\n')

log.write('\ntotal image size: '+hex(len(outdata))+'\n')

if extra_dummy_size > 0:
    log.write(hex(extra_dummy_size) + ' empty bytes at the end were ignored\n')

    while extra_dummy_size > 0:
        outdata.pop()
        extra_dummy_size -= 1

    log.write('result image size: ' + hex(len(outdata)) + '\n')


os.chdir('..')

out = open('out.bin', 'wb')
out.write(outdata)
out.close()



partitions.close()
log.close()