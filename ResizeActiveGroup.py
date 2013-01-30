import sublime_plugin
from copy import deepcopy

class ResizeActiveGroup(sublime_plugin.EventListener):

    def __init__(self):
        self.currentLayoutID = ""
        self.cellOrder = []
        #self.maxItemsInQueue = 0
        
    # based on the active group we calculate the cols/rows array
    def get_big(self, arr, activeGroup):
        return [arr[0], arr[1] if (activeGroup == 1) ^ (arr[1] > 0.5) else 1 - arr[1], arr[2]]
    
    # initialize all necessary layout information
    def init_layout_info(self, currentLayout, activeGroup):
        
        # handling change of layouts
        currLayoutID = "" + len(currentLayout["cells"]) + "-" + len(currentLayout["cols"]) + "-" + len(currentLayout["rows"])
        if(self.currentLayoutID != currLayoutID):
            self.cellOrder = []
            self.currentLayoutID = currLayoutID
            #self.maxItemsInQueue = len(currentLayout["cells"])
        
        # setting up the order
        try:
            self.cellOrder.remove(activeGroup)
        except ValueError:
            pass
        
        self.cellOrder.append(activeGroup)
    
    def get_size_by_order(self, arr)
        pass

    # called when a different view is activated
    def on_activated(self, view):
        
        window = view.window()
        if window:
            currentLayout = window.get_layout()
            activeGroup = window.active_group()
            self.init_layout_info(currentLayout, activeGroup)
            
            newLayout = deepcopy(currentLayout)
            
            # 2 cells
            if len(currentLayout["cells"]) == 2:
                # Columns: 2
                if len(currentLayout["rows"]) == 2:
                    newLayout["cols"] = self.get_big(currentLayout["cols"], activeGroup)
                # Rows: 2
                else:
                    newLayout["rows"] = self.get_big(currentLayout["rows"], activeGroup)

            # 3 cells
            elif len(currentLayout["cells"]) == 3:
                if len(currentLayout["rows"] == 4)
                    pass
                else
                    pass

            # 4 cells
            elif len(currentLayout["cells"]) == 4:
                # Grid: 4
                if len(currentLayout["rows"]) == 3 and len(currentLayout["cols"]) == 3:
                    if activeGroup == 0:
                        newLayout["cols"] = self.get_big(currentLayout["cols"], activeGroup)
                        newLayout["rows"] = self.get_big(currentLayout["rows"], activeGroup)
                    elif activeGroup == 1:
                        newLayout["cols"] = self.get_big(currentLayout["cols"], activeGroup)
                        newLayout["rows"] = self.get_big(currentLayout["rows"], activeGroup - 1)
                    elif activeGroup == 2:
                        newLayout["cols"] = self.get_big(currentLayout["cols"], activeGroup - 2)
                        newLayout["rows"] = self.get_big(currentLayout["rows"], activeGroup - 1)
                    elif activeGroup == 3:
                        newLayout["cols"] = self.get_big(currentLayout["cols"], activeGroup - 2)
                        newLayout["rows"] = self.get_big(currentLayout["rows"], activeGroup - 2)

            if currentLayout != newLayout:
                window.set_layout(newLayout)
            
