import sublime, sublime_plugin

class ToggleReadOnlyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        if self.view.is_read_only():
            self.view.set_read_only(False)
            self.view.erase_status("read-only")
            print("read-only: False")
            self.dump_settings()
        else:
            self.view.set_read_only(True)
            self.view.set_status("read-only", "%%")
            print("read-only: True")  
            self.dump_settings()

    def dump_settings(self):
        from pprint import pprint
        pprint(dir(self.view.settings()))