#C:\Program Files (x86)\National Instruments\Shared\ExternalCompilerSupport\C\include
from ctypes import *

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
            return status

        except Exception as error:
            print('Error during Wait IO Done function call ', error)
            raise

    def configure_stream_finite(self, stream_instance, num_samples):
        #int32_t niFlexRIO_ConfigureStreamFinite(uint32_t session in, uint32_t instance, const uint64_t num samples);
        c_stream_instance   = c_uint32(stream_instance)
        c_num_samples       = c_uint64(num_samples)

        try:
            status = self.nifpga_dll.niFlexRIO_ConfigureStreamFinite(self.nifpga_session,c_stream_instance,c_num_samples)
            if status < 0:
                raise Exception
            return status

        except Exception as error:
            print('Error during Stream Finite call ', error)
            raise

    def configure_stream_EnabledChannels(self, stream_instance, channel_list, channel_count):
        #int32_t niFlexRIO_ConfigureStreamEnabledChannels(uint32_t session in, uint32_t instance, const char* channelsEnabled, int32_t* channelCount);
        c_stream_instance   = c_uint32(stream_instance)
        c_channel_list      = c_char_p(channel_list)
        c_channel_count     = c_int32(channel_count)

        try:
            status = self.nifpga_dll.niFlexRIO_ConfigureStreamEnabledChannels(self.nifpga_session,c_stream_instance,c_channel_list, pointer(c_channel_count))
            if status < 0:
                raise Exception
            return status

        except Exception as error:
            print('Error during Stream Enabled Channels ', error)
            raise

    def commit(self):
        #int32_t niFlexRIO_Commit(uint32_t session in);
        try:
            status = self.nifpga_dll.niFlexRIO_Commit(self.nifpga_session)
            if status < 0:
                raise Exception
            return status

        except Exception as error:
            print('Error during Commit ', error)
            raise


    def clear_stream(self, stream_number):

        #int32_t niFlexRIO_ClearStream(uint32_t session, uint32_t stream number);
        c_stream_number = c_uint32(stream_number)
        try:
            status = self.nifpga_dll.niFlexRIO_ClearStream(self.nifpga_session, c_stream_number)
            if status < 0:
                raise Exception
            return status

        except Exception as error:
            print('Error during Clear Stream ', error)
            raise

    def start_stream(self, stream_number):

        #int32_t niFlexRIO_StartStream(uint32_t session, uint32_t stream number);
        c_stream_number = c_uint32(stream_number)
        try:
            status = self.nifpga_dll.niFlexRIO_StartStream(self.nifpga_session, c_stream_number)
            if status < 0:
                raise Exception
            return status

        except Exception as error:
            print('Error during Clear Stream ', error)
            raise

    
    def read_data(self, stream_instance, time_out, samples_per_wfm, num_Wfms = 1):
        #int32_t niFlexRIO_ReadStream2DF64(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs,
        #                  size_t numberOfWfms, size_t numberOfElements, double* elementArray, FlexRIO_WfmInfo* wfmInfoArray);

        c_stream_instance   = c_int32(stream_instance)
        c_timeout           = c_int32(time_out)
        c_numWfms           = c_size_t(num_Wfms)
        c_numElements       = c_size_t(samples_per_wfm)
        c_elementArray      = c_double * (num_Wfms * samples_per_wfm)()

        try:
            status = self.nifpga_dll.niFlexRIO_StartStream(self.nifpga_session, c_stream_instance, c_timeout, c_numWfms, c_numElements, c_elementArray, None)
            if status < 0:
                raise Exception

            return c_elementArray
        except Exception as error:
            print('Error during Clear Stream ', error)
            raise
