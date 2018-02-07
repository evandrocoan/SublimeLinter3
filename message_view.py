import sublime
import sublime_plugin

PANEL_NAME = "SublimeLinter Messages"


class SublimeLinterDisplayPanelCommand(sublime_plugin.WindowCommand):
    def run(self, msg=""):
        panel_view = sublime.active_window().create_output_panel(PANEL_NAME, True)
        panel_view.set_read_only(False)
        panel_view.run_command('append', {'characters': msg})
        panel_view.set_read_only(True)
        panel_view.show(0)
        sublime.active_window().run_command("show_panel", {"panel": "output.{}".format(PANEL_NAME)})


class SublimeLinterRemovePanelCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.active_window().destroy_output_panel(PANEL_NAME)
