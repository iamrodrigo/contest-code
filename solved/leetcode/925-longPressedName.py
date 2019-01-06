class Solution(object):
    def isLongPressedName(self, name, typed):
        pointerName = 0
        pointerTyped = 0
        
        while pointerName < len(name) and pointerTyped < len(typed):
            if name[pointerName] == typed[pointerTyped]:
                pointerName += 1
                pointerTyped += 1
            elif pointerTyped > 0 and typed[pointerTyped - 1] == typed[pointerTyped]:
                pointerTyped += 1
            else:
                return False
            
        if len(name) == pointerName and len(typed) > pointerTyped:
            lastChar = name[-1]
            while len(typed) > pointerTyped:
                if lastChar != typed[pointerTyped]:
                    return False

                pointerTyped +=1
        elif len(name) > pointerName and len(typed) == pointerTyped:
            return False
        
        return True