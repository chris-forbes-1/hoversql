import sublime
import sublime_plugin
import re
import ast
import csv
class HoverSql(sublime_plugin.EventListener):
	def on_activated(self, view):
		self.view = view

	def on_hover(self, view, point, hover_zone):
		if(hover_zone == sublime.HOVER_TEXT):
			if "SQL" in self.view.settings().get("syntax"):
				region = view.full_line(point)
				line = view.substr(sublime.Region(view.word(region).a, view.word(region).b))
			
				test = re.findall(r'\((.*?)\)',line)
				if len(test) is 2:
					columns = test[0]
					values = test[1]
					
					column_val = columns.split(',')		
					values_val = values.split(',')
					
					
					print ("col len:" + str(len(column_val)))
					print ("val len:" + str(len(values_val)))
					
					if len(column_val) == len(values_val):
						message = ""
						for i in range(0,len(column_val)):
							message += str(column_val[i]) + "=" + str(values_val[i]) + "<br>\n"
						view.show_popup(message,flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY,location=point, max_width=1024, max_height=1024)
					elif len(column_val) > len(values_val):
						view.show_popup("There are more columns than values, no_cols: %s no_vals: %s" %(str(len(column_val)),str(len(values_val))) , flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY, location=point)
					elif len(values_val) > len(column_val):
						view.show_popup("There are more values than columns,no_cols: %s no_vals: %s" %(str(len(column_val)),str(len(values_val))), flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY, location=point)
		
