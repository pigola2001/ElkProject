import time
import elkpy.sushicontroller as sc
from elkpy.sushi_info_types import PluginType
from elkpy.sushi_info_types import ProcessorState
from elkpy import sushierrors

IP_ADDRESS = '192.168.1.60'           #'192.168.0.249'
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

allprocessors = sushi.audio_graph.get_all_processors()

for proc in allprocessors:
    if "x_" in proc.name:
        for track in alltracks:
            if proc.id in track.processors:
                sushi.audio_graph.delete_processor_from_track(proc.id, track.id)

time.sleep(2)

#CREATE RETURN PROCESSOR FOR OWN

#get own track id
own_id = sushi.audio_graph.get_track_id('own')

#get muter processor id (needed to create the new processor)
muter_own_id = sushi.audio_graph.get_processor_id('muter_own')

#create new processor on own (parameters: name of the processor, uid of the sushi proc (not requested for vst2 and vst3), internal path of the proc,
# plugin type, id of the track to create the proc on, id of the proc immediately after the one we want to create (used to specify position),
# whether or not create the proc on the back of the chain (False if no, True if yes)

#create the return processor for own
sushi.audio_graph.create_processor_on_track('x_return_own', 'sushi.testing.return', None,
                                            PluginType.INTERNAL, own_id, muter_own_id, False)

time.sleep(1)

#CREATE RETURN PROCESSOR FOR BUDDY TRACKS

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
    sushi.audio_graph.create_processor_on_track('x_return_buddy_'+finalNumbers, 'sushi.testing.return', None,
                                            PluginType.INTERNAL, buddy_tid, testid, False)
    

#CREATE SOURCE TRACK WITH SEND AND AUDIO PLUGIN
    
#create a new track
sushi.audio_graph.create_track('x_source', 2)

time.sleep(2)

#get the id of the new track
source_id = sushi.audio_graph.get_track_id('x_source')

#create the new plugin on the source track
sushi.audio_graph.create_processor_on_track('x_mda_jx10', None, '/home/mind/plugins/mda-vst2/mdaJX10.so',
                                            PluginType.VST2X, source_id, None, True)

############################################

#create gain plugin
sushi.audio_graph.create_processor_on_track('x_gain', 'sushi.testing.gain', None, 
                                            PluginType.INTERNAL, source_id, None, True)

time.sleep(1)

gainId=sushi.audio_graph.get_processor_id('x_gain')

gainValueId=sushi.parameters.get_parameter_id(gainId, 'gain')

sushi.parameters.set_parameter_value(gainId, gainValueId, 0.8)

############################################


#create the send plugin on the source track
sushi.audio_graph.create_processor_on_track('x_source_track_send_own', 'sushi.testing.send', None,
                                           PluginType.INTERNAL, source_id, None, True)

sendId=sushi.audio_graph.get_processor_id('x_source_track_send_own')

destId=sushi.parameters.get_property_id(sendId, 'destination_name')

sushi.parameters.set_property_value(sendId, destId, "x_return_own")

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
    sushi.audio_graph.create_processor_on_track('x_source_track_send_'+finalNumbers, 'sushi.testing.send', None,
                                           PluginType.INTERNAL, source_id, None, True)
    
    #get the id of the send plugin
    sendId=sushi.audio_graph.get_processor_id('x_source_track_send_'+finalNumbers)
    
    destId=sushi.parameters.get_property_id(sendId, 'destination_name')

    sushi.parameters.set_property_value(sendId, destId, "x_return_buddy_"+finalNumbers)
    



