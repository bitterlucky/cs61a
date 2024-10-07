def draw(hand, positions):
    """Remove and return the items at positions from hand.
    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    return list(reversed([hand.pop(value) for value  in reversed(sorted(positions))]))

LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
class Caps_Lock:
    def __init__(self):
        self.pressed = 0
    def press(self):
        self.pressed += 1
class Button:
    """A button on a keyboard.
    >>> f = lambda c: print(c, end='') # The end='' argument avoids going to a new line
    >>> k, e, y = Button('k', f), Button('e', f), Button('y', f)
    >>> s = e.press().press().press()
    eee
    >>> caps = Button.caps_lock
    >>> t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]
    keyEEKeyeYEE
    >>> u = Button('a', print).press().press().press()
    A
    A
    A
    """
    caps_lock = Caps_Lock()
    def __init__(self, letter, output):
        self.letter = letter
        self.output = output
        self.pressed = 0
    def press(self):
        self.pressed += 1
        if self.caps_lock.pressed % 2 != 0:
            self.output(self.letter.upper())
        else:
            self.output(self.letter)
        return self
class Keyboard:
    """A keyboard.

    >>> Button.caps_lock.pressed = 0  # Reset the caps_lock key
    >>> bored = Keyboard()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o']
    >>> bored.keys['l'].pressed
    2

    >>> Button.caps_lock.press()
    >>> bored.type('hello')
    >>> bored.typed
    ['h', 'e', 'l', 'l', 'o', 'H', 'E', 'L', 'L', 'O']
    >>> bored.keys['l'].pressed
    4
    """
    def __init__(self):
        self.typed = []
        self.keys = {s:Button(s, self.typed.append) for s in LOWERCASE_LETTERS}
        
    def type(self, word):
        for s in word:
            self.keys[s].press()
            
        

class Eye:
    """An eye.

    >>> Eye().draw()
    '•'
    >>> print(Eye(False).draw(), Eye(True).draw())
    • -
    """
    def __init__(self, closed= False):
        self.closed = closed
        
    def draw(self):
        if self.closed == False:
            return '•'
        else:
            return '-'

    

class Bear:
    """A bear.

    >>> Bear().print()
    ʕ •ᴥ•ʔ
    """
    def __init__(self, closed = False):
        self.eye = Eye()
    def print(self):
        print(f"ʕ {self.eye.draw()}ᴥ{self.eye.draw()}ʔ")
    

class SleepyBear(Bear):
    """A bear with closed eyes.

    >>> SleepyBear().print()
    ʕ -ᴥ-ʔ
    """
    def __init__(self):
        self.eye = Eye(True)
    
        
    

class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ʕ -ᴥ•ʔ
    """
    def print(self):
        print("ʕ -ᴥ•ʔ")

    
