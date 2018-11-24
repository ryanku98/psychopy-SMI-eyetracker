
tracker_connected = False
config_file = expInfo['Eye tracker config']
from psychopy.iohub import util, client
io_config = util.readConfig(config_file)

io = client.ioHubConnection(io_config)

if io.getDevice('tracker'):
    eye_tracker = io.getDevice('tracker')
    tracker_connected = True
    win.winHandle.minimize()
    eye_tracker.runSetupProcedure()
    win.winHandle.activate()
    win.winHandle.maximize()

if not tracker_connected:
    print("Error: could not connect to eye tracking equipment")
    core.quit()
