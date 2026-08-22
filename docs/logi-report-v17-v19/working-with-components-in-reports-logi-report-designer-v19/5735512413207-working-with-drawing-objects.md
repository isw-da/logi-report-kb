---
title: "Working with Drawing Objects"
id: 5735512413207
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735512413207-Working-with-Drawing-Objects
updated_at: 2022-11-02T04:13:07Z
---

# Working with Drawing Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507452311-Working-with-UDOs)

# Working with Drawing Objects

You can add arcs, ovals, boxes, round boxes, and lines to banded objects in page reports, and add lines to banded objects in web reports. This topic describes how you can insert drawing objects in a report.

**To insert a drawing object into a report**

1. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the drawing object.
2. Navigate to **Insert** > **Drawing Objects**, then select the drawing object you want to insert on the submenu: **Line**, **Box**, **Arc**, **Oval**, or **Round Box**.
3. Move your mouse pointer to the insertion point, drag the mouse button till you are satisfied with the drawing object's size and proportions. Designer then inserts the selected drawing object at the specified position.

An interesting attribute of a box is that if it spans a group, the box automatically grows in size to encompass the objects in the group. For example, you draw a box starting in a group header panel through the detail panel and ending in the group footer panel. At runtime, the box grows to include all of the detail items inside it.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* A drawing object can cross banded panels. You can set its [geometry properties](https://devnet.logianalytics.com/hc/en-us/articles/5735516870935-Arc-Shape-Properties#Geometry) to specify its relative position in the involved panel, including Bottom Attach Pos X, Bottom Attach Pos Y, Top Attach Pos X, and Top Attach Pos Y.
* Although you can insert all the drawing objects in a page report, at runtime, Page Report Studio can only display boxes and horizontal/vertical lines (a horizontal line has the same Bottom Attach Pos Y and Top Attach Pos Y property values and a vertical line has the same Bottom Attach Pos X and Top Attach Pos X).
* If you need to export a report to HTML, the lines in it should be either horizontal or vertical lines; otherwise, they cannot display properly in the HTML output.
* Round boxes cannot display in the HTML or PostScript output; ovals cannot display in the HTML or RTF output.

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the drawing object example, open `<install_root>\Demo\Reports\SampleComponents\ForDrawingObject.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735507452311-Working-with-UDOs)
