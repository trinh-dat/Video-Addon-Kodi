from win32com.client import Dispatch
eg = Dispatch("EventGhost")
eg.TriggerEvent(u"EventFromMyApplication")
eg.TriggerEvent(u"EventWithPayload", 12345)