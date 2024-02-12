import time
import elkpy.sushicontroller as sc
from elkpy.sushi_info_types import PluginType
from elkpy.sushi_info_types import ProcessorState
from elkpy import sushierrors

sushi = sc.SushiController('192.168.0.249:51051', sushi_proto_def='C:/Users/pietr/OneDrive/Desktop/Uni/Magistrale/Research_Project/sushi-gui/venv/Lib/site-packages/sushi_rpc.proto')

#get the own track id
own_id=sushi.audio_graph.get_track_id('own')

#print the processors on the own track
print(sushi.audio_graph.get_track_processors(own_id))
