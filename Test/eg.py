import sublime, sublime_plugin

class moos(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                self.view.run_command("insert_snippet",{"name":"../Date-now.sublime-snippet"})
            else:
            	self.view.run_command('left_delete')
                self.view.run_command("insert_snippet",{"name":"../Date-now.sublime-snippet"})
