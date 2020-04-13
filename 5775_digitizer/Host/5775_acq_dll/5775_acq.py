

#Config Settings
dll_path = r"C:\Users\kalyan\Desktop\5775_digitizer\Host\5775_acq_dll\SharedLib.dll"
bitfile_path = r"C:\Users\kalyan\Desktop\5775_digitizer\Host\PXIe_5775_KU035.lvbitx"


from ctypes import *
import ctypes
from sys import exit
import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.6f}".format(x)})

def get_5775_data(bitfile_path = '',device_name ='RIO0', channel_names = 'AI0', num_samples = 320):
    try:
        
        if not bitfile_path:
            raise Exception(" Input bitfile path is empty")

        _acq_sess           = cdll.LoadLibrary(dll_path)
        c_bitfile_path      = c_char_p(bitfile_path.encode('utf-8'))
        c_device_name       = c_char_p(device_name.encode('utf-8'))
        c_channel_names     = c_char_p(channel_names.encode('utf-8'))
        c_num_samples       = c_uint64(num_samples)
        c_FirstChannel      = (c_double *num_samples)()
        c_SecondChannel     = (c_double *num_samples)()
        c_FirstChannel_ptr  = pointer(c_FirstChannel)
        c_SecondChannel_ptr = pointer(c_SecondChannel)
        c_dt                = c_double(0)
        c_dt_ptr            = pointer(c_dt)

        status              = _acq_sess.GettingStarted_5775_Host_Basic_pn_SH(c_bitfile_path, c_device_name, c_channel_names, c_num_samples, c_FirstChannel_ptr, c_int32(num_samples), c_SecondChannel_ptr, c_int32(num_samples), c_dt_ptr)

        if status != 0:
            raise Exception(" LabVIEW DLL Status Error reported as {}".format(status))

        FirstChannel        = np.array(np.fromiter(c_FirstChannel, dtype=np.double, count=num_samples))
        SecondChannel       = np.array(np.fromiter(c_SecondChannel, dtype=np.double, count=num_samples))
        dt = c_dt.value
        return FirstChannel, SecondChannel, dt, status

    except Exception as e:
        print('Error in function get_5775_data :', e)
        return None, None, None, None


try:
    FirstChannel, SecondChannel, dt, status = get_5775_data(bitfile_path, 'PXI1Slot5')
    print("First Channel : {} ".format(FirstChannel))
    print("Smaple Period : ", dt)

except Exception as e:
    print('Error :', e)

