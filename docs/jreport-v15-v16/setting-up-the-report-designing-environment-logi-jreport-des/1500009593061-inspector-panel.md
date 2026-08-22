---
title: "Inspector Panel"
id: 1500009593061
section: "Setting Up the Report Designing Environment - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009593061-Inspector-Panel
updated_at: 2021-07-24T05:53:44Z
---

# Inspector Panel

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571102-Data-Panel)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593021-Components-Panel)

# Inspector Panel

The Inspector panel (also referred to as the Report Inspector) lists all the objects contained in a report in a tree structure (to display it, check **Inspector** on the Home or View menu bar). You can edit the object properties in the panel to change the appearance of your report.

![Inspector panel](https://devnet.logianalytics.com/hc/article_attachments/4404893798807/rptenv_inspctr.gif)

**Toolbar**

A page report may contain one or more report tabs, and each report tab contains a report body. You can use the toolbar to focus on one of the three levels, namely the report, report tab, and report body.

* ![Home button](https://devnet.logianalytics.com/hc/article_attachments/4404889282711/btn_home.gif)**Home**  
   Only shows the current report tab and its contents (including TOC of the report tab and datasets used in the report tab) in the report structure tree.
* ![Down button](https://devnet.logianalytics.com/hc/article_attachments/4404893799063/btn_down.gif)**Down**  
   Goes down a level, that is, selecting this button will switch from the report level to the report tab level, or from the report tab to the report body.
* ![](https://devnet.logianalytics.com/hc/article_attachments/4404889282967/btn_up.gif)**Up**  
   Goes up a level, that is, selecting this button will switch from the report body level to the report tab level, or from the report tab to the report.

**Report structure panel**

This panel shows all the objects in the current report in a tree structure.

By selecting an object in the tree you also select it in the report design area. When an object is marked invisible, you will not see it in the design area but you can still select it from the tree and change it's invisible property to false. You can use CTRL select and SHFT select to select multiple objects, then the Properties sheet will show only the properties that are common among the selected objects and you can change the property values for all the selected objects at a time. It is usually a much easier and faster way of selecting multiple objects in the tree than trying to select them one by one in the design area.

The display name of each object in this tree can be edited. To do this, select the object in the tree, after 2 or 3 seconds, select it again and the name will become editable, then give the object a new name and press **Enter** on the keyboard to confirm. End users will see the display name of data components such as banded objects, charts, crosstabs and tables when they choose to filter or sort. It is recommended to change the name of these objects so the users can easily understand which component they are choosing.

**Properties sheet**

This sheet lists all the properties of the object selected in the report structure tree. Each type of object has its own
set of properties. Depending on the object type, the properties that a certain object holds may greatly differ from those of another. The Properties sheet
has two columns: Name and Value. You can change how an object
appears and behaves by changing its value in the Value column. In addition, you can select the button ![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404889283223/btn_help1.gif) on the title bar to get detailed explanation about each property. For details about properties of each object, see [Properties in the Report Inspector](https://devnet.logianalytics.com/hc/en-us/articles/1500009590661-Report-Object-Properties).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009571102-Data-Panel)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009593021-Components-Panel)
