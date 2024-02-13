import time
import elkpy.sushicontroller as sc
from elkpy.sushi_info_types import PluginType
from elkpy.sushi_info_types import ProcessorState
from elkpy import sushierrors

sushi = sc.SushiController('192.168.0.249:51051', sushi_proto_def='C:/Users/pietr/OneDrive/Desktop/Uni/Magistrale/Research_Project/sushi-gui/venv/Lib/site-packages/sushi_rpc.proto')

#create a new track
sushi.audio_graph.create_track('source', 2)

#get the id of the new track
cimil_id = sushi.audio_graph.get_track_id('source')

#create the send plugin on the source track
sushi.audio_graph.create_processor_on_track('cimil_track_send_own', 'sushi.testing.send', None,
                                           PluginType.INTERNAL, cimil_id, None, True)

#get the id of the send plugin
sendId=sushi.audio_graph.get_processor_id('cimil_track_send_own')

#create the new plugin on the source track
sushi.audio_graph.create_processor_on_track('mda', None, '/home/mind/plugins/mda-vst2/mdaLeslie.so',
                                            PluginType.VST2X, cimil_id, sendId, False)

destId=sushi.parameters.get_property_id(sendId, 'destination_name')

sushi.parameters.set_property_value(sendId, destId, "return_own")

#get all the tracks
alltracks = sushi.audio_graph.get_all_tracks()

#get all the tracks with the name buddy
buddy_tracks = []
for track in alltracks:
    if "buddy" in track.name:
        buddy_tracks.append(track)


for i in range(0,len(buddy_tracks)):
    buddy_tid = int(buddy_tracks[i].id)

    #get the three final numbers of the buddy track and use them to get the muter processor
    trackParam=sushi.audio_graph.get_track_info(buddy_tid)
    buddy_name=trackParam.name
    finalNumbers=buddy_name[-3:]
    testid=sushi.audio_graph.get_processor_id('muter_buddy_'+finalNumbers)

    #create the send plugin on the source track
    sushi.audio_graph.create_processor_on_track('cimil_track_send'+finalNumbers, 'sushi.testing.send', None,
                                           PluginType.INTERNAL, cimil_id, None, True)
    
    #get the id of the send plugin
    sendId=sushi.audio_graph.get_processor_id('cimil_track_send_'+finalNumbers)
    
    destId=sushi.parameters.get_property_id(sendId, 'destination_name')

    sushi.parameters.set_property_value(sendId, destId, "return_buddy"+finalNumbers)
    
