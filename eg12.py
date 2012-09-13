import sublime, sublime_plugin

path = "Packages/Mootools/"

class moos12(sublime_plugin.TextCommand):
    def run(self, edit):
    	sublime.status_message(sublime.installed_packages_path())
        for region in self.view.sel():
            if region.empty():
                line = self.view.line(region)
                self.view.run_command("insert_snippet",{"name":path+"Class/Class.sublime-snippet"})
            else:
            	self.view.run_command('left_delete')
                self.view.run_command("insert_snippet",{"name":path+"Class/Class.sublime-snippet"})

class moo1(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message(sublime.installed_packages_path())