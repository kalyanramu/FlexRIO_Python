import time
from ctypes import *

def poll_reg(reg, time_out_sec = 5):
    try:
        init_done = reg.read()
        #print(init_done)
        loop_time = 0.5
        num_polls = time_out_sec/ loop_time
        while init_done == False:
            init_done = reg.read()
            #print(init_done)
            time.sleep(0.5)  # wait a bit between retries
            num_polls -= 1
            if num_polls == 0:
                raise Exception('Error: IO Module not configured before the specified timeout.')
        return init_done
    except Exception as error:
        print('Exception in function --> init_done :', error)
        return None

class nifga_dll():
    dll_path = r"C:\Windows\System32\niflexrioapi.dll"

    def __init__(self, session):
        try:
            
            self.nifpga_dll = cdll.LoadLibrary(self.dll_path)
            self.nifpga_session = session._session
            
        except Exception as error:
            print('Error Initializing NI FPGA DLL :', error)
            raise
    
    def wait_for_io_done(self, timeout =5):
        #int32_t niFlexRIO_WaitForIoReady(uint32_t session in, int32_t timeoutInMs, uint32_t *ioReady, int32_t *ioError);
        time_out = c_uint32(timeout)
        io_ready = c_uint32(0)
        io_error = c_int32(0)
        io_ready_ptr = POINTER(io_ready)
        io_error_ptr = POINTER(io_error)
        try:
            status = self.nifpga_dll.niFlexRIO_WaitForIoReady(self.nifpga_session,time_out,io_ready_ptr, io_error_ptr)
            if status < 0:
                raise Exception

        except Exception as error:
            print('Error during Wait IO Done function call ', error)
            raise

    

class nifpga_stream():
    dll_path = r"C:\Program Files (x86)\National Instruments\LabVIEW 2018\resource\nistreaming.dll"
    
    def __init__(self, session):
        try:
            self.nifpga_stream_dll = cdll.LoadLibrary(self.dll_path)
            self.nifpga_session = session._session
            
        except Exception as error:
            print('Error Initializing NI FPGA Stream :', error)
            raise

    def clear_stream(self, stream_index):
        
        try:
            c_stream_index = c_int32(stream_index)
            status = self.nifpga_stream_dll.niInstrStreaming_ClearStream(self.nifpga_session, c_stream_index)
            return status
    
        except Exception as error:
            print('Error Initializing NI FPGA Stream :', error)
            raise

    def start_finite_stream(self,stream_index, num_samples):
        try:
            c_stream_index =  c_int32(stream_index)
            c_num_samples   = c_uint64(num_samples)
            status = self.nifpga_stream_dll.niInstrStreaming_StartFinite(self.nifpga_session, c_stream_index, c_num_samples)
            return status
    
        except Exception as error:
            print('Error in Start Finite Stream:', error)
            raise

    # def wait_finite_stream(self,stream_index, num_samples):
    #     try:
    #         status = self.nifpga_stream_dll.niInstrStreaming_WaitForTransferLv(self.nifpga_session, stream_index, num_samples)
    #         return status
    
    #     except Exception as error:
    #         print('Error in Start Finite Stream:', error)
