import time
import elkpy.sushicontroller as sc
from elkpy.sushi_info_types import PluginType
from elkpy.sushi_info_types import ProcessorState
from elkpy import sushierrors

sushi = sc.SushiController('192.168.0.249:51051', sushi_proto_def='C:/Users/pietr/OneDrive/Desktop/Uni/Magistrale/Research_Project/sushi-gui/venv/Lib/site-packages/sushi_rpc.proto')

alltracks = sushi.audio_graph.get_all_tracks()

buddy_tracks = []
for track in alltracks:
    if "buddy" in track.name:
        buddy_tracks.append(track)

for i in range(0,len(buddy_tracks)):
    buddy_tid = int(buddy_tracks[i].id)
    
    trackParam=sushi.audio_graph.get_track_info(buddy_tid)
    buddy_name=trackParam.name

    print("Track id: "+buddy_name)
    print(sushi.audio_graph.get_track_processors(buddy_tid))
    print("\n \n ")

