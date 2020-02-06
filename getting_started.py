from nifpga import Session
from nifpga_dll_calls import *
import matplotlib.pyplot as plt

bitfile_path =  r'C:\Program Files (x86)\National Instruments\LabVIEW 2018\examples\FlexRIO\IO Modules\NI 5772\NI 5772 (DC) - Getting Started\FPGA Bitfiles\NI5772DCGe_PXIe-7976R.lvbitx'



channel_select = 0
range = 2.0
num_bits =12
gain = (range/ (2**num_bits))
num_samples = 1000
stream_index = 0
with Session(bitfile= bitfile_path, resource="RIO0") as session:
    session.run()
    init_done_reg       = session.registers["IO Module\Initialization Done"]
    #channel_sel_reg     = session.registers["ChannelSelect"]

    #Wait until module is initialized
    init_done_status = poll_reg(init_done_reg)
    print(init_done_status)

    #Select Channel
    #channel_sel_reg.write(channel_select)

    #Start FPGA FIFO
    target_to_host = session.fifos['To Host FIFO']
    target_to_host.buffer_size = num_samples
    target_to_host.start()

    #Start Stream Session
    stream_session = nifpga_stream(session)
    stream_session.clear_stream(stream_index)
    stream_session.start_finite_stream(stream_index, num_samples)

    # Get the data from FPGA
    read_value = target_to_host.read(num_samples, timeout_ms=10000)
    # read_value is a tuple containing the data and elements remaining
    print(read_value.elements_remaining)  # prints 0

    #Print Data
    #print(read_value.data)
    #scaled_data = gain* (read_value.data)
    scaled_data = [gain * value for value in read_value.data]
    print(scaled_data)

    
