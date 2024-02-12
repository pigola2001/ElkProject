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
sushi.audio_graph.create_processor_on_track('cimil_track_send', 'sushi.testing.send', None,
                                           PluginType.INTERNAL, cimil_id, None, True)

#get the id of the send plugin
sendId=sushi.audio_graph.get_processor_id('cimil_track_send')

#create the new plugin on the source track
sushi.audio_graph.create_processor_on_track('mda', None, '/home/mind/plugins/mda-vst2/mdaLeslie.so',
                                            PluginType.VST2X, cimil_id, sendId, False)
