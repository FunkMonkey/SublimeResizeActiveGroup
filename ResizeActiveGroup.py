import sublime_plugin


class ResizeActiveGroup(sublime_plugin.EventListener):

    # based on the active group we calculate the cols/rows array
    def get_big(self, arr, activeGroup):
        return [arr[0], arr[1] if (activeGroup == 1) ^ (arr[1] > 0.5) else 1 - arr[1], arr[2]]

    # called when a different view is activated
    def on_activated(self, view):
        window = view.window()
        if window:
            activeGroup = window.active_group()
            oldLayout = window.get_layout()

            # 2 cells
            if len(oldLayout["cells"]) == 2:
                # Columns: 2
                if len(oldLayout["rows"]) == 2:
                    oldLayout["cols"] = self.get_big(oldLayout["cols"], activeGroup)
                    window.set_layout(oldLayout)
                # Rows: 2
                else:
                    oldLayout["rows"] = self.get_big(oldLayout["rows"], activeGroup)
                    window.set_layout(oldLayout)

            # 3 cells
            elif len(oldLayout["cells"]) == 3:
                pass

            # 4 cells
            elif len(oldLayout["cells"]) == 4:
                # Grid: 4
                if len(oldLayout["rows"]) == 3 and len(oldLayout["cols"]) == 3:
                    if activeGroup == 0:
                        oldLayout["cols"] = self.get_big(oldLayout["cols"], activeGroup)
                        oldLayout["rows"] = self.get_big(oldLayout["rows"], activeGroup)
                        window.set_layout(oldLayout)
                    elif activeGroup == 1:
                        oldLayout["cols"] = self.get_big(oldLayout["cols"], activeGroup)
                        oldLayout["rows"] = self.get_big(oldLayout["rows"], activeGroup - 1)
                        window.set_layout(oldLayout)
                    elif activeGroup == 2:
                        oldLayout["cols"] = self.get_big(oldLayout["cols"], activeGroup - 2)
                        oldLayout["rows"] = self.get_big(oldLayout["rows"], activeGroup - 1)
                        window.set_layout(oldLayout)
                    elif activeGroup == 3:
                        oldLayout["cols"] = self.get_big(oldLayout["cols"], activeGroup - 2)
                        oldLayout["rows"] = self.get_big(oldLayout["rows"], activeGroup - 2)
                        window.set_layout(oldLayout)
