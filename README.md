subl-read-only is an extremely simple Sublime Text plugin to toggle the read-only status of the current view.  Unlike other plugins that do this, it doesn't mess with the file permissions in the OS; it just sets Sublime's "read only" status on the view and puts "%%" in the status bar at the bottom left of the screen when the view is read-only.  

To install
===========

Navigate to Sublime Text's package directory (on a Mac that's in ~/Library/Application Support/Sublime Text 3/Packages) and git clone https://github.com/del82/subl-read-only.git.  

The default toggle key is F13, which I've mapped to the CapsLock key on my machine.  You can also toggle read-only using the command palette (Command+Shift+P on Mac), in the Edit menu (Edit -> Toggle Read Only), or by right-clicking in the view and selecting "Toggle read-only."


