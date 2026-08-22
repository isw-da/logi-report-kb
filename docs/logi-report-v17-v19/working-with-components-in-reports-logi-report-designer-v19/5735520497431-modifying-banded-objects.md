---
title: "Modifying Banded Objects"
id: 5735520497431
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735520497431-Modifying-Banded-Objects
updated_at: 2022-11-02T04:12:40Z
---

# Modifying Banded Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511901079-Inserting-Banded-Objects-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735506771991-Embedding-Data-Components-in-a-Banded-Object)

# Modifying Banded Objects

For any banded object in a report, you can further modify it at any time. This topic describes how you can edit a banded object using the banded wizard and modify the banded panels.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can use the [Expand/Collapse Group web control](https://devnet.logianalytics.com/hc/en-us/articles/5735527778327-Using-Advanced-Web-Controls#Expand) in a banded object of a page report, so that Page Report Studio users can use the web control to expand/collapse records in the groups of the banded object.

This topic contains the following sections:

* [Editing a Banded Object with Wizard](#Wizard)
* [Managing the Banded Panels](#Panel)

## Editing a Banded Object with Wizard

You can further modify a banded object by accessing its shortcut menu wizard which contains a set of screens that are similar to the wizard screens that you use to create the banded object. For example, you can change the data the banded object applies, specify group and sort criteria to the banded object, and apply a new style to the banded object.

1. Right-click the banded object and select **Banded Wizard** from the shortcut menu to display the [Banded Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735499848471-Banded-Wizard-Dialog-Box).
2. In the **Data** screen, you can specify a new data source for the banded object.
3. In the **Display** and **Group** screens, specify the data to display in the banded object accordingly.
   Use ![](https://devnet.logianalytics.com/hc/article_attachments/9898460510743/btn_replace.gif) to replace any current field. For more information about how to define a banded object, see [Inserting Banded Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/5735511901079-Inserting-Banded-Objects-in-a-Report).
4. In the **Style** screen, select the style you want to apply to the banded object.
5. Select **Finish** to accept the changes.

## Managing the Banded Panels

By default, a banded object contains these panels: a Banded Header (BH) panel, a Banded Page Header panel (BPH) , a Detail panel (DT), a Parallel Detail panel (PDT, which is only available for the banded objects that use hierarchical data sources), a Banded Page Footer panel (BPF), a Banded Footer panel (BF), and several Group Header (GH) and Group Footer (GF) panels if the data in the banded object is grouped.

You can perform the following operations on banded panels:

* **Adding a banded panel**  
  Select a panel of the same type, right-click it and select **Insert Panel Before** or **Insert Panel After**. Designer then inserts a blank panel of the same type into the banded object.
* **Deleting a banded panel**  
  Right-click the panel and select **Delete**. You cannot delete a panel of a certain type if it is the only one of that type.
* **Hiding a banded panel**  
  Right-click the panel and select **Hide**.
* **Showing a hidden banded panel**
  1. Select **Hidden Objects** in the **View** ribbon. Designer then displays the hidden panel and marks them with two triangles.
  2. Right-click the banded panel and select **Show** on the shortcut menu to release its hidden state.
  3. You may want to select Hidden Objects in the View ribbon again, because it does not show you a true view of your report.
* **Resizing a banded panel**
  + For a vertical or cross (mailing label) banded object, drag the boundary below the banded panel until the panel is at the required height.
  + For a horizontal banded object, drag the boundary on the right side of the banded panel until the panel is at the required width.

You can also use the properties Invisible and Width/Height of a banded panel in the Report Inspector to show/hide, and resize the panel.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735511901079-Inserting-Banded-Objects-in-a-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735506771991-Embedding-Data-Components-in-a-Banded-Object)
