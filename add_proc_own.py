import time
import elkpy.sushicontroller as sc
from elkpy.sushi_info_types import PluginType
from elkpy.sushi_info_types import ProcessorState
from elkpy import sushierrors

#connect to the board with a controller (parameters: ip and port, path of the proto file)
sushi = sc.SushiController('192.168.0.249:51051', sushi_proto_def='C:/Users/pietr/OneDrive/Desktop/Uni/Magistrale/Research_Project/sushi-gui/venv/Lib/site-packages/sushi_rpc.proto')

#get own track id
own_id = sushi.audio_graph.get_track_id('own')

#get muter processor id (needed to create the new processor)
muter_own_id = sushi.audio_graph.get_processor_id('muter_own')

#create new processor on own (parameters: name of the processor, uid of the sushi proc (not requested for vst2 and vst3), internal path of the proc,
# plugin type, id of the track to create the proc on, id of the proc immediately after the one we want to create (used to specify position),
# whether or not create the proc on the back of the chain (False if no, True if yes)
sushi.audio_graph.create_processor_on_track('mda_own', None, '/home/mind/plugins/mda-vst2/mdaLeslie.so',
                                            PluginType.VST2X, own_id, muter_own_id, False)

