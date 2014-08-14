import wx
import sys

class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(1280,400))

        wx.FutureCall(2000, self.DrawBipmap)

        self.Centre()
        self.Show()

    def DrawBipmap(self):
        dc = wx.ClientDC(self)
        bgcolor_red = 0x00
        bgcolor_green = 0x00
        bgcolor_blue = 0xff
        f = open(bmpname, 'rb')
        print "opened"
        x=0;y=0
        while(1):
        #for i in range(100):
          try:
            (b,g,r,a) = f.read(4)
            print ord(a)
            if ord(a) == 0 : 
                color = '#' + '%02x'%bgcolor_red + '%02x'%bgcolor_green + '%02x'%bgcolor_blue
            elif ord(a) == 255 :
                color = '#' + '%02x'%ord(r) + '%02x'%ord(g) + '%02x'%ord(b)
            else:
                rate = ord(a) / 255.0
                red = bgcolor_red * (1-rate) + ord(r)*rate
                green = bgcolor_green * (1-rate) + ord(g)*rate
                blue = bgcolor_blue * (1-rate) + ord(b)*rate
                color = '#' + '%02x'%red + '%02x'%green + '%02x'%blue
                #print color
            dc.SetPen(wx.Pen(color))
            dc.DrawPoint(x, y)
            if x == max_idx_x:
                x = 0; y = y + 1
            else:
                x = x + 1
          except Exception, msg:
            print "error :"+ msg
            break

        f.close()
        print "closed"


if __name__ == '__main__':
    app = wx.App()
    print "argument: " + str(sys.argv)
    bmpname = sys.argv[1]
    max_idx_x = int(sys.argv[2]) - 1
   
    print "max index " + str(max_idx_x) 
    Example(None, bmpname)
    app.MainLoop()
