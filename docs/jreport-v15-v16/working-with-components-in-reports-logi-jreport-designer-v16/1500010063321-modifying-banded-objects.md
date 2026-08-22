---
title: "Modifying Banded Objects"
id: 1500010063321
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010063321-Modifying-Banded-Objects
updated_at: 2021-07-24T10:39:30Z
---

# Modifying Banded Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063301-Inserting-a-Banded-Object) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028642-Embedding-Data-Components-in-a-Banded-Object)

# Modifying Banded Objects

For any banded object in a report, you can further modify it at any time. For example you can change the data displayed in the banded object, add and remove the panels in the banded object, and so on.

**Tip:** You can use the [Expand/Collapse Group web control](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Expand) in a banded object of a page report so that end users in Page Report Studio can use the web control to expand/collapse records in the groups of the banded object.

This topic introduces modifying a banded object as follows:

* [Editing a Banded Object with Wizard](#Wizard)
* [Managing the Banded Panels](#Panel)

## Editing a Banded Object with Wizard

Once a banded object has been created, you can further modify it by accessing its shortcut menu wizard which is composed by a set of screens that are similar to the wizard screens used to create the banded object. For example, you can change the data or even the dataset used by the banded object, apply group and sort criteria to the banded object, and so on.

1. Right-click the banded object and select **Banded Wizard** from the shortcut menu to display the [Banded Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500010029822-Banded-Wizard-Dialog).
2. In the Data screen, specify a new data source for the banded object if required.
3. Define the data displayed in the banded object in the Display and Group screens accordingly.
   Use the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404901173527/btn_replace.gif) to replace any current field. For details about how to define a banded object, see [Inserting Banded Objects in a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010063301-Inserting-a-Banded-Object).
4. In the Style screen, select the style you want to apply to the banded object.
5. Select **Finish** to accept the changes.

## Managing the Banded Panels

By default, a banded object consists of these panels: a Banded Header (BH) panel, a Banded Page Header (BPH) panel, a Detail (DT) panel, a Parallel Detail (PDT, this is only for the banded objects which are created on HDS) panel, a Banded Page Footer (BPF) panel, a Banded Footer (BF) panel, and several Group Header (GH) and Group Footer (GF) panels if the data in the banded object is grouped.

Logi JReport Designer allows you to perform the following tasks related to the banded panels.

* **Adding a banded panel**  
   Select a panel of the same type, right-click it and select **Insert Panel Before** or **Insert Panel After**. A blank panel of the same type will be inserted into the banded object.
* **Deleting a banded panel**  
   To delete a banded panel from a banned object, right-click the panel and select **Delete**. Note that you cannot delete a panel of a certain type if it is the only one of that type.
* **Hiding a banded panel**  
   To hide a banded panel from view, right-click the panel, and then select **Hide**.
* **Showing a hidden banded panel**
  1. Check the item **Hidden Objects** on the View tab, and the hidden panel will then be displayed and marked with two triangles.
  2. Right-click the banded panel, and select **Show** on the shortcut menu to release its hidden state.
  3. Turn off **Hidden Objects** on the View menu as it will not show you a true view of your report.
* **Resizing a banded panel**
  + For a vertical or cross (mailing label) banded object, drag the boundary below the banded panel until the panel is at the required height.
  + For a horizontal banded object, drag the boundary on the right side of the banded panel until the panel is at the required width.

You can also make use of the properties Invisible and Width/Height of a banded panel in the Inspector to show/hide, and resize the panel.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010063301-Inserting-a-Banded-Object) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010028642-Embedding-Data-Components-in-a-Banded-Object)
