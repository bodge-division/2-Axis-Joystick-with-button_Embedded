ThisFile = 'PwdOled.py'
# ----- Date        : 23/06/2021
# ----- Author      : Simon Bird
# ----- Version
Pwversion = '0v40'
# ----- IDE         : Thonny
# ----- Programmer  : pico
# ----- Total time 
totalTime = ['xx','xx']
dayMultiplier = 'xx'


#------------Current edit--------------#
# need selective print of segments
current_edit_pos = "line 351"


from machine import Pin , I2C

#------------------ CLASS JOY --------------- #  ---  26,27,16
class __joystick:
       
    def __init__(self, pin_v , pin_h , pin_b , adc_voltage_in ):
        self.verticalJoyAdc = machine.ADC(pin_v)                 #vertical
        self.horizontialJoyAdc = machine.ADC(pin_h)              #horizontal
        self.buttonJoyDIO = Pin( pin_b , Pin.IN , Pin.PULL_UP )  #button        
        
        self.all_current_reads = [ 0 , 0 , 0 , 0 , 0]# up , down , left , right , button
         
    def poll(self):     
        r_valuev=self.verticalJoyAdc.read_u16();        v=r_valuev>>11;      
        r_valueh=self.horizontialJoyAdc.read_u16();     h=r_valueh>>11;      
        
        utime.sleep(0.01)      # delay for read, ie fetch ADC   
        
        up=0;        down=0;        left=0;         right=0;
        #Order needs to be preserved 0 - max
        if(v==0):       down=3;up=0;
        if(v>0):        down=2;up=0;
        if(v>9):        down=1;up=0;
        if(v==15):      up=0;down=0;
        if(v>15):       up=1;down=0;
        if(v>=22):      up=2;down=0;   
        if(v>30):       up=3;down=0;
            
        if(h==0):       left=3;right=0;
        if(h>0):        left=2;right=0;
        if(h>9):        left=1;right=0;
        if(h==15):      left=0;right=0;
        if(h>15):       left=0;right=1;
        if(h>=22):      left=0;right=2;   
        if(h>30):       left=0;right=3;
                 
        self.all_current_reads[0]= up;        self.all_current_reads[1]= down
        self.all_current_reads[2]= left;      self.all_current_reads[3]= right
        self.all_current_reads[4]= not self.buttonJoyDIO.value() 
        return self.all_current_reads
      
    def button(self):
        return ( not self.buttonJoyDIO.value() )
    #PLACEHOLDER AS POLL STILL POLLS ALL
    # if only one axis needed can slim down ADC
    def checkup(self):
        return self.all_current_reads[0]
    def checkdown(self):
        return self.all_current_reads[1]
    def checkleft(self):
        return self.all_current_reads[2]
    def checkright(self):
        return self.all_current_reads[3]
   
# ----- ----- ----- END JOY CLASS ----- ----- ----- #
