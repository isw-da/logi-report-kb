---
title: "Defining Hierarchies"
id: 1500009583021
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009583021-Defining-Hierarchies
updated_at: 2021-07-24T05:56:14Z
---

# Defining Hierarchies

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562682-Modifying-the-Joins-Between-Data-Resources)

# Defining Hierarchies

Hierarchies can be defined in a business view to allow users to drill report data up and down to particular groups at runtime. A hierarchy is defined as a hierarchy category holding one group of group elements sharing a hierarchical relationship, following the order from the highest level to the lowest. For example, these group elements can be added into one hierarchy called Dates: Sales Year, Sales Quarter, Sales Month, and Sales Date. When any of these group elements are used for grouping data in a table, crosstab or chart, end users can use the context menu to drill up or down to the next level. You can create any number of hierarchies such as dates, times, geography, product types, and so on.

The group elements added in a hierarchy are just references to the real group elements and therefore cannot be edited.

**To create hierarchies in a business view:**

1. In the Business View Editor, do any of the following:
   * Select **New Hierarchy** on the toolbar.
   * Select **Menu** > **New** > **Hierarchy**.
   * Right-click the business view root node or any category in the Business View panel and select **New Hierarchy** from the shortcut menu.

   **Tip:** Hierarchies can be added into any category in a business view and it does not make any difference where it is placed. For easy look-up, you can put them under the root category.
2. In the New Hierarchy dialog, provide a name for the hierarchy and select **OK**. A blank hierarchy is added to the business view resource tree.
3. You can now add group elements into the hierarchy as a hierarchical group by dragging and dropping. From the business view resource tree, select a required group element and then drop it into the hierarchy. Where the group will be placed in the hierarchy depends on the dropped position:
   * When you drop on the hierarchy root node, it will be placed to the bottom level of the hierarchy.
   * When on an existing hierarchical group, it will be placed below this hierarchical group.
   * When between two hierarchical groups, it will be placed between them.

   You can also drag objects from the Resource Objects panel to the hierarchy. Then those that have not been added as group elements in the business view will be automatically added to the business view and placed at the bottom of the business view resource tree.

   To adjust the position of the groups in the hierarchy, make use of the ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif) button. The higher a group is placed, the higher its level is in the hierarchy.

   To remove a group from the hierarchy, select it, then right-click and select **Remove from Hierarchy** on the shortcut menu, or drag and drop it to the Resource Objects panel.
4. Repeat the above three steps to create more hierarchies in the business view.

   To rename a hierarchy, select it from the business view resource tree, then right-click it and select **Rename** on the shortcut menu, or select on the hierarchy name twice. When the name text field becomes editable, input a new name and select outside of the text field to accept the change.

   To remove a hierarchy, select it from the business view resource tree, then right-click it and select  **Delete** on the shortcut menu, or select the **Delete** on the toolbar. You can select multiple hierarchies and remove them all at a time.
5. Save the business view to save the hierarchies into it.

You can also add and manage hierarchies in a business view from the Catalog Manager as follows:

* **Adding a hierarchy**
  1. In the Catalog Manager resource tree, right-click a category in the business view and select **New Hierarchy** from the shortcut menu.
  2. Provide a name in the New Hierarchy dialog and then select **OK**.
  3. A hierarchy will be added in the business view.
  4. Right-click the business view and select **Edit** on the shortcut menu to open the Business View Editor.
  5. [Drag and drop group elements](#Drag) to the hierarchy to define its hierarchical groups.
  6. Save the business view to save the hierarchy.
* **Removing a hierarchical group from a hierarchy**In the Catalog Manager resource tree, locate the group in the hierarchy, then right-click it and select **Remove from Hierarchy** on the shortcut menu.
* **Renaming a hierarchy**In the Catalog Manager resource tree, locate the hierarchy in the business view, right-click it and select **Rename** on the shortcut menu, or select on the hierarchy name twice. When the name text field becomes editable, input a new name and select outside of the text field to accept the change.
* **Removing a hierarchy**In the Catalog Manager resource tree, locate the hierarchy in the business view, then right-click it and select  **Delete** on the shortcut menu, or select **Delete** on the Catalog Manager toolbar.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562662-Creating-Predefined-Filters)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562682-Modifying-the-Joins-Between-Data-Resources)
