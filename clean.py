import time
import elkpy.sushicontroller as sc
from elkpy.sushi_info_types import PluginType
from elkpy.sushi_info_types import ProcessorState
from elkpy import sushierrors

IP_ADDRESS = '192.168.1.59'           #'192.168.0.249'      
PORT = '51051'
SUSHI_PROTO_FILE_PATH = 'C:/Users/pietr/OneDrive/Desktop/Uni/Magistrale/Research_Project/sushi-gui/venv/Lib/site-packages/sushi_rpc.proto'

sushi = sc.SushiController(IP_ADDRESS+':'+PORT, sushi_proto_def=SUSHI_PROTO_FILE_PATH)

#CLEAN ALL PREVIOUSLY CREATED TRACKS AND PROCESSORS

#delete previously created tracks

alltracks = sushi.audio_graph.get_all_tracks()

for track in alltracks:
    if "x_" in track.name:
        track_id=track.id
        sushi.audio_graph.delete_track(track.id)

#delete previously created processors

own_ret=sushi.audio_graph.get_processor_id('x_return_own')
own_id=sushi.audio_graph.get_track_id('own')

sushi.audio_graph.delete_processor_from_track(own_ret, own_id)


