import sublime, sublime_plugin

class ToggleReadOnlyCommand(sublime_plugin.TextCommand):
    status_name = "1-read-only" # try to make key alphabetically first
    def run(self, edit):
        if self.view.is_read_only():
            self.view.set_read_only(False)
            self.view.erase_status(self.status_name)
        else:
            self.view.set_read_only(True)
            self.view.set_status(self.status_name, "%%")

