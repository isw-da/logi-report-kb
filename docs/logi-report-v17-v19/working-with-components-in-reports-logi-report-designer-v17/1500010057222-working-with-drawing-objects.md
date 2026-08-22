---
title: "Working with Drawing Objects"
id: 1500010057222
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057222-Working-with-Drawing-Objects
updated_at: 2021-07-23T19:14:45Z
---

# Working with Drawing Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094861-Working-with-Subreports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057462-Working-with-UDOs)

# Working with Drawing Objects

You can add arcs, ovals, boxes, round boxes, and lines to banded objects in page reports, and add lines to banded objects in web reports. This topic describes how you can insert drawing objects in a report.

**To insert a drawing object into a report:**

1. Select **Insert** > **Drawing Objects**, then select the drawing object you want to insert on the submenu: Line, Box, Arc, Oval, or Round Box.
2. Move your mouse pointer to the insertion point, drag the mouse button till you are satisfied with the drawing object's size and proportions. Designer then inserts the selected drawing object at the specified position. Note that Page Report Studio can only presents boxes, horizontal, or vertical lines.

An interesting attribute of a box is that if it spans a group, the box automatically grows in size to encompass the objects in the group. For example, you draw a box starting in a group header panel through the detail panel and ending in the group footer panel. At runtime, the box will grow to include all of the detail items inside the box.

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the drawing object example, open `<install_root>\Demo\Reports\SampleComponents\ForDrawingObject.cls`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094861-Working-with-Subreports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057462-Working-with-UDOs)
