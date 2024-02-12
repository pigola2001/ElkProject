import time
import elkpy.sushicontroller as sc
from elkpy.sushi_info_types import PluginType
from elkpy.sushi_info_types import ProcessorState
from elkpy import sushierrors

#connect to the board with a controller (parameters: ip and port, path of the proto file)
sushi = sc.SushiController('192.168.0.249:51051', sushi_proto_def='C:/Users/pietr/OneDrive/Desktop/Uni/Magistrale/Research_Project/sushi-gui/venv/Lib/site-packages/sushi_rpc.proto')

sushi.audio_graph.create_track('buddy_623', 2)
sushi.audio_graph.create_track('buddy_101', 2)

time.sleep(1)
#get all the tracks
alltracks = sushi.audio_graph.get_all_tracks()
print(alltracks)

#filter all the track with the name buddy
for i in range(0,len(alltracks)):
    buddy_tid = [t.id for t in alltracks if 'buddy' in t.name][i]
    print(buddy_tid)

    #get the three final numbers of the buddy track and use them to get the muter processor
    trackParam=sushi.audio_graph.get_track_info(buddy_tid)
    buddy_name=trackParam.name
    finalNumbers=buddy_name[-3:]
    testid=sushi.audio_graph.get_processor_id('muter_buddy_'+finalNumbers)

    #create the processor on the track
    sushi.audio_graph.create_processor_on_track('mda_buddy', None, '/home/mind/plugins/mda-vst2/mdaLeslie.so',
                                            PluginType.VST2X, buddy_tid, testid, False)


