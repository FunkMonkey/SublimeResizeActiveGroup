SublimeResizeActiveGroup
========================

Sublime Plugin for resizing the active layout group when the user switches groups. Resize the groups once as usual using the sliders. Whenever you activate a different group now, the selected group will be resized to have the most space.

It currently works with the following layouts:
* Rows: 2
* Columns: 2
* Grid: 4

If you have any ideas how 3/4 row/column resizing should work, just post an issue...

Installing
----------

**With the Package Control plugin:** The easiest way to install SublimeResizeActiveGroup is through Package Control, which can be found at this site: http://wbond.net/sublime_packages/package_control

Once you install Package Control, restart ST2 and bring up the Command Palette (`Command+Shift+P` on OS X, `Control+Shift+P` on Linux/Windows). Select "Package Control: Install Package", wait while Package Control fetches the latest package list, then select `Resize Active Group` when the list appears. The advantage of using this method is that Package Control will automatically keep SublimeResizeActiveGroup up to date with the latest version.

**Without Git:** Download the latest source from [GitHub](https://github.com/FunkMonkey/SublimeResizeActiveGroup) and copy the SublimeResizeActiveGroup folder to your Sublime Text "Packages" directory.

**With Git:** Clone the repository in your Sublime Text "Packages" directory:

    git clone https://github.com/FunkMonkey/SublimeResizeActiveGroup.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/
		
_This nice installation guide was stolen from the [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) readme. Thanks!_