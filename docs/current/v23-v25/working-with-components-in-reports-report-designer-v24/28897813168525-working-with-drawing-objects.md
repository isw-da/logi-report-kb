---
title: "Working with Drawing Objects"
id: 28897813168525
section: "Working with Components in Reports - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897813168525-Working-with-Drawing-Objects
updated_at: 2024-09-30T09:08:56Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# Working with Drawing Objects

You can add arcs, ovals, boxes, round boxes, and lines to banded objects in page reports, and add lines to banded objects in web reports. This topic describes how you can insert drawing objects in a report.

To insert a drawing object into a report

- Position the mouse pointer at the allowed report location where you want to insert the drawing object.
				

- Navigate to Insert > Drawing Objects, then select the drawing object you want to insert on the submenu: Line, Box, Arc, Oval, or Round Box.

- Move your mouse pointer to the insertion point, drag the mouse button till you are satisfied with the drawing object's size and proportions. Designer then inserts the selected drawing object  at the specified position.

 An interesting attribute of a box is that if it spans a group, the box automatically grows in size to encompass the objects in the group. For example, you draw a box starting in a group header panel through the detail panel and ending in the group footer panel. At runtime, the box grows to include all of the detail items inside it.

- A drawing object can cross banded panels. You can set its geometry properties to specify its relative position in the involved panel, including Bottom Attach Pos X, Bottom Attach Pos Y, Top Attach Pos X, and Top Attach Pos Y.

- Although you can insert all the drawing objects in a page report, at runtime, Page Report Studio can only display boxes and horizontal/vertical lines (a horizontal line has the same Bottom Attach Pos Y and Top Attach Pos Y property values and a vertical line has the same Bottom Attach Pos X and Top Attach Pos X).

- If you need to export a report to HTML, the lines in it should be either  horizontal or vertical lines; otherwise, they cannot display properly in the HTML output.

- Round boxes cannot display in the HTML or PostScript output; ovals cannot display in the HTML or RTF output.

See an example: The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the drawing object example, open <install_root>\Demo\Reports\SampleComponents\ForDrawingObject.cls.

Previous Topic  Next Topic
