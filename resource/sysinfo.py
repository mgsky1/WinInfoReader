#读取操作系统名称、CPU型号、内存大小(GB)，硬盘大小(GB)、显卡及显存(GB)
import wmi
import easygui as gui

def reader():
    #获取wmi对象
    c = wmi.WMI()
    #读取系统操作系统
    for os in c.Win32_OperatingSystem():
        exp = '操作系统：'+os.caption + '\n'
    #读取CPU型号
    for cpu in c.Win32_Processor():
        exp += 'CPU：'+cpu.Name.strip()+'\n'
    #读取内存大小,GB为单位
    for memory in c.Win32_PhysicalMemory():
        exp += '安装内存：'+str(int(memory.Capacity) // 1024 ** 3)+'GB\n'
    #获取硬盘类型
    types = {0:'未知',1:'非根目录',2:'移动磁盘',3:'本地磁盘',4:'网络磁盘',5:'光盘',6:'虚拟盘'}
    count = 0
    _type = ''
    for drive in c.Win32_LogicalDisk():
        type = drive.DriveType
        if type != _type:
            exp += '硬盘类型'+str(count)+'：'+types[type] + '\n'
            _type = type
            count += 1
    #读取硬盘大小,GB为单位
    total = 0
    for disk in c.Win32_LogicalDisk(DriveType=3):
        total += int(disk.Size) // 1024 ** 3 
    exp += '本地硬盘大小：'+str(total) + 'GB\n'
    #检测显卡，读取显存，GB为单位
    #计数
    count = 0
    #这个查询语句比较复杂，具体的参考MSDN
    wql = 'Select * from Win32_VideoController'#查询语句参考度娘
    for graph in c.query(wql):
        name = graph.caption
        memory = abs(int(graph.AdapterRAM)) // 1024 ** 3#用abs取反，我原始读出来是负数
        exp += 'GPU'+str(count)+'：'+name+' 显存：'+str(memory)+'GB\n'
        count += 1
    return exp

gui.msgbox(reader(), '电脑信息', image = 'computer.gif')