from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.camera.setPos(0, 0, 0)
        self.camera.setHpr(0, 0, 0)

        self.boxModel = loader.loadModel("models/box")
        self.boxModel.setScale(3, 3, 3)
        self.boxModel.setPos(0,3,0)
        self.boxModel.reparentTo(self.render)

    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

app = MyApp()
app.run()