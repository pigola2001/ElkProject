import time
import elkpy.sushicontroller as sc
from elkpy.sushi_info_types import PluginType
from elkpy.sushi_info_types import ProcessorState
from elkpy import sushierrors

#connect to the board with a controller (parameters: ip and port, path of the proto file)
sushi = sc.SushiController('192.168.0.249:51051', sushi_proto_def='C:/Users/pietr/OneDrive/Desktop/Uni/Magistrale/Research_Project/sushi-gui/venv/Lib/site-packages/sushi_rpc.proto')


#get all the tracks
alltracks = sushi.audio_graph.get_all_tracks()

#get all the tracks with the name buddy
buddy_tracks = []
for track in alltracks:
    if "buddy" in track.name:
        buddy_tracks.append(track)

#iterate on all the buddy tracks to delete the proc
for i in range(0,len(buddy_tracks)):
    buddy_tid = int(buddy_tracks[i].id)

    #get the three final numbers of the buddy track and use them to get id of the proc to be deleted
    trackParam=sushi.audio_graph.get_track_info(buddy_tid)
    buddy_name=trackParam.name
    finalNumbers=buddy_name[-3:]
    procid=sushi.audio_graph.get_processor_id('return_buddy_'+finalNumbers)

    #delete the buddy proc
    sushi.audio_graph.delete_processor_from_track(procid,buddy_tid)

#get own track id
own_id=sushi.audio_graph.get_track_id('own')

#get the id of the proc to be deleted from own
procid=sushi.audio_graph.get_processor_id('return_own')

#delete the proc
sushi.audio_graph.delete_processor_from_track(procid,own_id)

#delete the created track
sushi.audio_graph.delete_track("source")

