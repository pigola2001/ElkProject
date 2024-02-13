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

#iterate on all the buddy tracks to create the proc on them
for i in range(0,len(buddy_tracks)):
    buddy_tid = int(buddy_tracks[i].id)

    #get the three final numbers of the buddy track and use them to get the muter processor
    trackParam=sushi.audio_graph.get_track_info(buddy_tid)
    buddy_name=trackParam.name
    finalNumbers=buddy_name[-3:]
    testid=sushi.audio_graph.get_processor_id('muter_buddy_'+finalNumbers)

    #create the return processor on the track
    sushi.audio_graph.create_processor_on_track('return_buddy'+finalNumbers, 'sushi.testing.return', None,
                                            PluginType.INTERNAL, buddy_tid, testid, False)



