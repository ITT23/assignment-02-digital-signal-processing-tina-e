import pyaudio


def setup(chunk_size, format, channels, rate):
    '''
    sample code to set up audio stream coming from chosen input device
    :return: stream
    '''
    # Set up audio stream
    p = pyaudio.PyAudio()

    # print info about audio devices
    # let user select audio device
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')

    for i in range(0, num_devices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

    print('select audio device:')
    input_device = int(input())

    # open audio input stream
    return p.open(format=format,
                  channels=channels,
                  rate=rate,
                  input=True,
                  frames_per_buffer=chunk_size,
                  input_device_index=input_device)
