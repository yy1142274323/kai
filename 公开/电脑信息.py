import psutil
import platform
import wmi

# ----------------------------------------------------------------------------------------------------------------


# import psutil

# 系统的内存利用率
free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2))+'GB'
total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2))+'GB'
memory_use_percent = str(psutil.virtual_memory().percent)+' %'
# print('可用内存：',free) # 可用内存： 8.14GB
print('总内存',total) # 总内存 15.73GB
print('内存占用率',memory_use_percent) # 内存占用率 48.2%
# cpu1秒内的占用率，和任务管理器显示的不一样，大概管理器里面的为一半
# print('cpu占用率', str(psutil.cpu_percent(interval=1))+' %') # cpu占用率 31.5%
print('物理cpu个数',psutil.cpu_count(logical=False)) # 物理cpu个数 4


# ----------------------------------------------------------------------------------------------------------------
# import platform

# print("您的系统为:" + platform.system())  # Windows
print("您的操作系统名称及版本号:" + platform.platform()) # Windows-10-10.0.19041-SP0
# print("您的操作系统版本号:" + platform.version()) # 10.0.19041
# print("您的CPU生产商为:" + platform.machine()) # AMD64
# print("您的CPU信息为:" + platform.processor()) # Intel64 Family 6 Model 140 Stepping 1, GenuineIntel
# print("获取操作系统的位数:" ,platform.architecture()) # ('64bit', 'WindowsPE')
print("计算机的网络名称:" + platform.node()) # DESKTOP-K2Q78MR
# print("包含上面所有的信息汇总:" , platform.uname())

# ----------------------------------------------------------------------------------------------------------------
# pip install wmi
# pip install pypiwin32
# import wmi
cpuinfo = wmi.WMI()
for cpu in cpuinfo.Win32_Processor():

    # print("您的CPU序列号为:" + cpu.ProcessorId.strip()) # BFEBFBFF0999906C1
    print("您的CPU名称为:" + cpu.Name) # 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz
    print("您的CPU已使用:%d%%" % cpu.LoadPercentage) # 17%
    print("您的CPU核心数为:%d" % cpu.NumberOfCores) # 4
    # print("您的CPU时钟频率为:%d" % cpu.MaxClockSpeed) # 1690
# ----------------------------------------------------------------------------------------------------------------
def get_fs_info():
    """
    获取文件系统信息
    包含分区的大小、已用量、可用量、使用率、挂载点信息
    """
    tmplist = []
    c = wmi.WMI()
    for physical_disk in c.Win32_DiskDrive():
        # print(physical_disk)
        for partition in physical_disk.associators("Win32_DiskDriveToDiskPartition"):
            # print(partition)
            for logical_disk in partition.associators("Win32_LogicalDiskToPartition"):
                # print(logical_disk)
                tmpdict = {}
                tmpdict["Caption"] = logical_disk.Caption
                tmpdict["DiskTotal"] = int(logical_disk.Size) / 1024 / 1024 / 1024
                tmpdict["UseSpace"] = (int(logical_disk.Size) - int(logical_disk.FreeSpace)) / 1024 / 1024 / 1024
                tmpdict["FreeSpace"] = int(logical_disk.FreeSpace) / 1024 / 1024 / 1024
                tmpdict["Percent"] = int(
                    100.0 * (int(logical_disk.Size) - int(logical_disk.FreeSpace)) / int(logical_disk.Size))
                tmplist.append(tmpdict)
    return tmplist
# testPlatform()
# 获取磁盘信息
fs = get_fs_info()
for f in fs:
  disk_name = f['Caption']  # 磁盘名
  DiskTotal = f['DiskTotal']  # 磁盘大小 单位G
  disk_UseSpace = f['UseSpace']  # 已用磁盘大小 单位G
  disk_FreeSpace = f['FreeSpace']  # 剩余可用磁盘大小 单位G
  print('磁盘名：{}  磁盘大小：{}G   已用空间：{}G  剩余可用空间：{}G !!'.format(disk_name, round(DiskTotal, 2), round(disk_UseSpace, 2),round(disk_FreeSpace, 2)))
