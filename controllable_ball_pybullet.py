import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadSDF("stadium.sdf")
p.setGravity(0,0,-10)
objects = p.loadMJCF("sphere.xml")
sphere = objects[0]
p.resetBasePositionAndOrientation(sphere,[0,0,1],[0,0,0,1])
p.changeDynamics(sphere,-1,linearDamping=0.9)
p.changeVisualShape(sphere,-1,rgbaColor=[1,0,0,1])
forward = 0
left = 0
turn = 0

cameraDistance = 1 
cameraYaw = 0
cameraPitch = -35

while (1):

	spherePos, orn = p.getBasePositionAndOrientation(sphere)
	
	cameraTargetPosition = spherePos
	p.resetDebugVisualizerCamera(cameraDistance,cameraYaw,cameraPitch,cameraTargetPosition)
	camInfo = p.getDebugVisualizerCamera()
	camForward = camInfo[5]

	
	keys = p.getKeyboardEvents()
	for k,v in keys.items():
		
		if (k == p.B3G_F3 and (v&p.KEY_WAS_TRIGGERED)):
			turn = -0.5
		if (k == p.B3G_F3 and (v&p.KEY_WAS_RELEASED)):
			turn = 0
		if (k == p.B3G_F2 and (v&p.KEY_WAS_TRIGGERED)):
			turn = 0.5
		if (k == p.B3G_F2 and (v&p.KEY_WAS_RELEASED)):
			turn = 0
		
		if (k == p.B3G_UP_ARROW and (v&p.KEY_WAS_TRIGGERED)):
			forward=1
		if (k == p.B3G_UP_ARROW and (v&p.KEY_WAS_RELEASED)):
			forward=0
		if (k == p.B3G_DOWN_ARROW and (v&p.KEY_WAS_TRIGGERED)):
			forward=-1
		if (k == p.B3G_DOWN_ARROW and (v&p.KEY_WAS_RELEASED)):
			forward=0

		if (k == p.B3G_RIGHT_ARROW and (v&p.KEY_WAS_TRIGGERED)):
			left=1
		if (k == p.B3G_RIGHT_ARROW and (v&p.KEY_WAS_RELEASED)):
			left=0
		if (k == p.B3G_LEFT_ARROW and (v&p.KEY_WAS_TRIGGERED)):
			left=-1
		if (k == p.B3G_LEFT_ARROW and (v&p.KEY_WAS_RELEASED)):
			left=0

	force  = [forward*camForward[0],forward*camForward[1],0]
	force1  = [left*camForward[1],left*camForward[0],0]	

	cameraYaw = cameraYaw+turn
	
	if (forward):
		p.applyExternalForce(sphere,-1, force , spherePos, flags = p.WORLD_FRAME )
	if (left):
		p.applyExternalForce(sphere,-1, force1 , spherePos, flags = p.WORLD_FRAME )

		
	p.stepSimulation()
	time.sleep(1./240.)
