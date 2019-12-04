import wx  # Import the GUI module wx
import sys  # Import the standard library module sys
import pyping  # Import the ICMP Ping Module
import socket  # Import the standard library module socket
from time import gmtime, strftime  # import time functions


def pingScan(event):
    if hostEnd.GetValue() < hostStart.GetValue():

        dlg = wx.MessageDialog(mainWin, "Invalid Local Host Selection", "Confirm", wx.OK | wx.ICON_EXCLAMATION)
        result = dlg.ShowModal()
        dlg.Destroy()
        return


    mainWin.StatusBar.SetStatusText('Executing Ping Sweep .... Please Wait')


    utcStart = gmtime()
    utc = strftime("%a, %d %b %Y %X +0000", utcStart)
    results.AppendText("\n\nPing Sweep Started: " + utc + "\n\n")

    baseIP = str(ipaRange.GetValue()) + '.' + str(ipbRange.GetValue()) + '.' + str(ipcRange.GetValue()) + '.'

    ipRange = []

    for i in range(hostStart.GetValue(), (hostEnd.GetValue() + 1)):
        ipRange.append(baseIP + str(i))

    for ipAddress in ipRange:

        try:

            mainWin.StatusBar.SetStatusText('Pinging IP: ' + ipAddress)


            delay = pyping.ping(ipAddress, timeout=5, count=1)

            results.AppendText(ipAddress + '\t')

            if delay != None:
                results.AppendText('   Response Success')
                results.AppendText('   Response Time: ' + str(delay.avg_rtt) + ' Seconds')
                results.AppendText("\n")
            else:
                results.AppendText('   Response Timeout')
                results.AppendText("\n")

        except socket.error, e:
            results.AppendText(ipAddress)
            results.AppendText('   Response Failed: ')
            results.AppendText(e.message)
            results.AppendText("\n")
    utcEnd = gmtime()
    utc = strftime("%a, %d %b %Y %X +0000", utcEnd)
    results.AppendText("\nPing Sweep Ended: " + utc + "\n\n")
    mainWin.StatusBar.SetStatusText('')


def programExit(event):
    sys.exit()

app = wx.App()
mainWin = wx.Frame(None, title="pingSweep v1.0", size=(1200, 800))
panelAction = wx.Panel(mainWin)
scanButton = wx.Button(panelAction, label='Scan')
scanButton.Bind(wx.EVT_BUTTON, pingScan)

exitButton = wx.Button(panelAction, label='Exit')
exitButton.Bind(wx.EVT_BUTTON, programExit)

results = wx.TextCtrl(panelAction, style=wx.TE_MULTILINE | wx.HSCROLL)

ipaRange = wx.SpinCtrl(panelAction, -1, '')
ipaRange.SetRange(0, 255)
ipaRange.SetValue(127)

ipbRange = wx.SpinCtrl(panelAction, -1, '')
ipbRange.SetRange(0, 255)
ipbRange.SetValue(0)

ipcRange = wx.SpinCtrl(panelAction, -1, '')
ipcRange.SetRange(0, 255)
ipcRange.SetValue(0)
ipLabel = wx.StaticText(panelAction, label="IP Base: ")

# Next, I want to provide the user with the ability to set the host range
# they wish to scan.  Maximum is 0 - 255

hostStart = wx.SpinCtrl(panelAction, -1, '')
hostStart.SetRange(0, 255)
hostStart.SetValue(1)

hostEnd = wx.SpinCtrl(panelAction, -1, '')
hostEnd.SetRange(0, 255)
hostEnd.SetValue(10)
HostStartLabel = wx.StaticText(panelAction, label="Host Start: ")
HostEndLabel = wx.StaticText(panelAction, label="Host End: ")

cb1 = wx.CheckBox(panelAction, label='Stealth Mode')

actionBox = wx.BoxSizer()
actionBox.Add(scanButton, proportion=1, flag=wx.LEFT, border=5)
actionBox.Add(exitButton, proportion=0, flag=wx.LEFT, border=5)

actionBox.Add(ipLabel, proportion=0, flag=wx.LEFT | wx.CENTER, border=5)

actionBox.Add(ipaRange, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipbRange, proportion=0, flag=wx.LEFT, border=5)
actionBox.Add(ipcRange, proportion=0, flag=wx.LEFT, border=5)

actionBox.Add(HostStartLabel, proportion=0, flag=wx.LEFT | wx.CENTER, border=5)
actionBox.Add(hostStart, proportion=0, flag=wx.LEFT, border=5)

actionBox.Add(HostEndLabel, proportion=0, flag=wx.LEFT | wx.CENTER, border=5)
actionBox.Add(hostEnd, proportion=0, flag=wx.LEFT, border=5)

actionBox.Add(cb1, proportion=1, flag=wx.RIGHT, border=5)

vertBox = wx.BoxSizer(wx.VERTICAL)
vertBox.Add(actionBox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vertBox.Add(results, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
mainWin.CreateStatusBar()

panelAction.SetSizer(vertBox)


mainWin.Show()


app.MainLoop()
