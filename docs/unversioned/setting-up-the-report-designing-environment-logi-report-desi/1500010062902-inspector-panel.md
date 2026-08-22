---
title: "Inspector Panel"
id: 1500010062902
section: "Setting Up the Report Designing Environment - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010062902-Inspector-Panel
updated_at: 2021-07-23T19:16:53Z
---

# Inspector Panel

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101501-Data-Panel)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062882-Components-Panel)

# Inspector Panel

The Inspector panel (also referred to as the Report Inspector) lists all the objects contained in a report in a tree structure (to display it, select **Home**/**View** > **Inspector**). You can edit the object properties in the panel to change the appearance of your report. This topic introduces the usages of the toolbar icons, report structure tree, and Properties sheet that comprise the panel.

![Inspector panel](https://devnet.logianalytics.com/hc/article_attachments/4404856799127/rptenv_inspctr.gif)

**Toolbar**

* ![Home button](https://devnet.logianalytics.com/hc/article_attachments/4404848374167/btn_home.gif)**Home**  
  Select to show the main structure nodes of the web report or the current report tab for a page report in the report structure tree, which includes Report Body, TOC, and Datasets (only for page report tab).
* ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856799767/btn_down1.gif)/![Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848374679/btn_up.gif)**Down**/**Up**  
  A page report contains one or more report tabs, and each report tab contains a report body. By default, the root node in the report structure tree represents the current report tab. You can use the two buttons to show one of the three levels as the root node: the report, report tab, or report body. For a web report, you can use the buttons to show the web report or report body as the root node.

**Report structure tree**

Designer lists all the objects in the current report in a tree structure.

By selecting an object in the tree, you also select it in the report design area. When an object is set invisible, you cannot see it in the design area but you can still select it from the tree and change it's Invisible property to false. You can use "CTRL + select" and "SHIFT + select" to select multiple objects, then the Properties sheet shows only the properties that are common among the selected objects and you can change the property values for all the selected objects at a time. It is usually a much easier and faster way of selecting multiple objects in the tree than trying to select them one by one in the design area.

You can edit the display name of each object in this tree: select the object in the tree, after two or three seconds, select it again and the name becomes editable, then give the object a new name and press **Enter** on the keyboard to confirm. The report users see the display name of data components such as banded objects, charts, crosstabs, and tables when they perform filter or sort at runtime. It is recommended to change the name of these objects, so the report users can easily understand which component they are choosing.

**Properties sheet**

This sheet lists all the properties of the object that you select in the report structure tree. It
has two columns: Name and Value, which you can resize can by dragging the boundary between them. You can change how an object
appears and behaves by changing its value in the Value column.

Each type of object has its own
set of properties. Depending on the object type, the properties that a certain object holds can greatly differ from those of another. For more information about properties of each object, see [Report Object Properties](https://devnet.logianalytics.com/hc/en-us/articles/1500010061682-Report-Object-Properties).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010101501-Data-Panel)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010062882-Components-Panel)
