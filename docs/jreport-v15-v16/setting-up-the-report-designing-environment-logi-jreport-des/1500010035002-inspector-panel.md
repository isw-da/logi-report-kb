---
title: "Inspector Panel"
id: 1500010035002
section: "Setting Up the Report Designing Environment - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010035002-Inspector-Panel
updated_at: 2021-07-24T10:37:41Z
---

# Inspector Panel

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034982-Data-Panel) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010071041-Components-Panel)

# Inspector Panel

The Inspector panel (also referred to as the Report Inspector) lists all the objects contained in a report in a tree structure (to display it, check **Inspector** on the Home or View menu tab). You can edit the object properties in the panel to change the appearance of your report.

![Inspector panel](https://devnet.logianalytics.com/hc/article_attachments/4404901114903/rptenv_inspctr.gif)

**Toolbar**

A page report may contain one or more report tabs, and each report tab contains a report body. You can use the toolbar to focus on one of the three levels, namely the report, report tab, and report body.

* ![Home button](https://devnet.logianalytics.com/hc/article_attachments/4404901115159/btn_home.gif)**Home**  
   Only shows the current report tab and its contents (including TOC of the report tab and datasets used in the report tab) in the report structure tree.
* ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4404901115415/btn_down.gif)**Down**  
   Goes down a level, that is, selecting this button will switch from the report level to the report tab level, or from the report tab to the report body.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404901115671/btn_up.gif)**Up**  
   Goes up a level, that is, selecting this button will switch from the report body level to the report tab level, or from the report tab to the report.

**Report structure tree**

All the objects in the current report are listed in a tree structure.

By selecting an object in the tree you also select it in the report design area. When an object is marked invisible, you will not see it in the design area but you can still select it from the tree and change it's invisible property to false. You can use CTRL select and SHIFT select to select multiple objects, then the Properties sheet will show only the properties that are common among the selected objects and you can change the property values for all the selected objects at a time. It is usually a much easier and faster way of selecting multiple objects in the tree than trying to select them one by one in the design area.

The display name of each object in this tree can be edited. To do this, select the object in the tree, after 2 or 3 seconds, select it again and the name will become editable, then give the object a new name and press **Enter** on the keyboard to confirm. End users will see the display name of data components such as banded objects, charts, crosstabs and tables when they choose to filter or sort. It is recommended to change the name of these objects so the users can easily understand which component they are choosing.

**Properties sheet**

This sheet lists all the properties of the object selected in the report structure tree. It
has two columns: Name and Value, which can be resized by dragging the boundary between them. You can change how an object
appears and behaves by changing its value in the Value column. By hovering the mouse pointer over a property name in the Property column, you can get a brief description about what the property can do, the data type of its value and how to set the property value. selecting the button **?** on the tooltip title and you will be directed to the help document about all properties of the selected object.

Each type of object has its own
set of properties. Depending on the object type, the properties that a certain object holds may greatly differ from those of another. For details about properties of each object, see [Report Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010034982-Data-Panel) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010071041-Components-Panel)
