import pyautogui
from pychroma import Sketch

class Test_01(Sketch):
    config_path = './config.json'

    def setup(self):
        self.frame_rate = 15
        self.keyboard.color_mode('hsv')
        self.main_color = (240,100,100)#HSV Color Blue
        self.main_color_F = (58,82,94)#HSV Color Yellow
    
    def update(self):
        self.activeWindow = pyautogui.getActiveWindowTitle()
        print(self.activeWindow)
    
    def getKey(self,key):
        map = {
            'ESC':(1,0),
            
            'F1':(3,0),
            'F2':(4,0),
            'F3':(5,0),
            'F4':(6,0),
            'F5':(7,0),
            'F6':(8,0),
            'F7':(9,0),
            'F8':(10,0),
            'F9':(11,0),
            'F10':(12,0),
            'F11':(13,0),
            'F12':(14,0),
            
            'PRINT':(15,0),
            'ROLL':(16,0),
            'PAUSE':(17,0),
            
            'MM_BACK':(18,0),
            'MM_PPAUSE':(19,0),
            'MM_FWD':(20,0),
            'MM_VOLUME':(21,0),
            
            '^':(1,1),
            '1':(2,1),
            '2':(3,1),
            '3':(4,1),
            '4':(5,1),
            '5':(6,1),
            '6':(7,1),
            '7':(8,1),
            '8':(9,1),
            '9':(10,1),
            '0':(11,1),
            'ß':(12,1),
            '´':(13,1),
            'BACKSPACE':(14,1),
            
            'PUT':(15,1),
            'POS1':(16,1),
            'PUP':(17,1),
            
            'NUM':(18,1),
            'NUM_DIV':(19,1),
            'NUM_MULT':(20,1),
            'NUM_MINUS':(21,1),
            
            'TAB':(1,2),
            'Q':(2,2),
            'W':(3,2),
            'E':(4,2),
            'R':(5,2),
            'T':(6,2),
            'Z':(7,2),
            'U':(8,2),
            'I':(9,2),
            'O':(10,2),
            'P':(11,2),
            'Ü':(12,2),
            '+':(13,2),
            
            'DEL':(15,2),
            'END':(16,2),
            'PDOWN':(17,2),
            
            'NUM_7':(18,2),
            'NUM_8':(19,2),
            'NUM_9':(20,2),
            'NUM_PLUS':(21,2),
            
            'CAPS':(1,3),
            'A':(2,3),
            'S':(3,3),
            'D':(4,3),
            'F':(5,3),
            'G':(6,3),
            'H':(7,3),
            'J':(8,3),
            'K':(9,3),
            'L':(10,3),
            'Ö':(11,3),
            'Ä':(12,3),
            '#':(13,3),
            'ENTER':(14,3),
            
            'NUM_4':(18,3),
            'NUM_5':(19,3),
            'NUM_6':(20,3),
            
            'SHIFT_L':(1,4),
            '<':(2,4),
            'Y':(3,4),
            'X':(4,4),
            'C':(5,4),
            'V':(6,4),
            'B':(7,4),
            'N':(8,4),
            'M':(9,4),
            ',':(10,4),
            '.':(11,4),
            '-':(12,4),
            'SHIFT_R':(14,4),
            
            'UP':(16,4),
            'NUM_1':(18,4),
            'NUM_2':(19,4),
            'NUM_3':(20,4),
            'NUM_ENTER':(21,4),
            
            'CTRL_L':(1,5),
            'WIN':(2,5),
            'ALT':(3,5),
            'SPACE':(7,5),
            'ALTGR':(11,5),
            'FN':(12,5),
            'MENU':(13,5),
            'CTRL_R':(14,5),
            
            'LEFT':(15,5),
            'DOWN':(16,5),
            'RIGHT':(17,5),
            
            'NUM_0':(19,5),
            'NUM_,':(20,5),
            

        }
        return(map[key.upper()])
    
    def render(self):
        self.keyboard.clear()
        self.keyboard.set_grid(self.getKey('ESC'),self.main_color)
        self.keyboard.set_grid(self.getKey('MM_VOLUME'),self.main_color)
        
        self.keyboard.set_grid(self.getKey('^'),self.main_color)
        self.keyboard.set_grid(self.getKey('NUM_MINUS'),self.main_color)
        
        self.keyboard.set_grid(self.getKey('TAB'),self.main_color)
        self.keyboard.set_grid(self.getKey('NUM_PLUS'),self.main_color)
        
        self.keyboard.set_grid(self.getKey('CAPS'),self.main_color)
                
        self.keyboard.set_grid(self.getKey('SHIFT_L'),self.main_color)
        self.keyboard.set_grid(self.getKey('NUM_ENTER'),self.main_color)
        
        self.keyboard.set_grid(self.getKey('CTRL_L'),self.main_color)
        
        
        
        