---
title: "Page Report Manager"
id: 1500009592921
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592921-Page-Report-Manager
updated_at: 2021-07-24T05:53:48Z
---

# Page Report Manager

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570942-Setting-Filter-Options-for-an-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports)

# Page Report Manager

All created page report files (.cls) are physically placed in the same directory where the catalog file resides. Due to this, you will not be able to get detailed information about a page report until it is opened in Logi JReport Designer. For example, if you want to find a page report with a special condition, you will have to load each page report. For just a few page reports, this is not a problem. However, the case is different when there are many reports.

Logi JReport provides you with a tool for managing page reports by means of adding them into folders with the Page Report Manager. You can build folder items in the manager, helping you to divide the page reports into different types at your disposal. Then, the reports can be added to the folder, and worked on just like processing files in a file system--add, open, delete, move, rename and search items. In all, the feature of report folder implemented in catalogs enables you to manage your page reports in a way that can better satisfy your requirements.

The following are some concepts used in the Page Report Manager:

* **Folder Item**: A container in which you can operate page report items or sub folder items.
* **Report Item**: This represents a page report. You can edit name, keywords and description properties of this item.

To display the Page Report Manager, select **Report** > **Manage Page Reports**.

![Manage Page Reports](https://devnet.logianalytics.com/hc/article_attachments/4404889288599/rpt_pgrpt_mngr.gif)

You can manage your page reports in the current catalog with the Page Report Manager as follows:

> * [Adding an Item](#Add)
> * [Editing the Properties of an Item](#Edit)
> * [Searching for a Report or Folder Item](#Search)
> * [Exporting the Report Information to a Table](#Export)
> * [Moving an Item to Another Folder](#Move)
> * [Deleting Items](#Delete)

## Adding an Item

**To add a folder item to the Page Report Manager:**

1. Select a folder and select **New Folder** on the toolbar or right-click a folder and select **New Folder** from the shortcut menu.

   Now, a new folder is added as a sub node, and the default name for the folder is Folder1, Folder2.... You can rename the folder as required.
2. Select the folder and select **Rename** on the toolbar or right-click it and select **Rename** from the shortcut menu.
3. Type a new name in the name box, and then select outside the box (or just press **Enter** on the keyboard).

**To add report items to the Page Report Manager:**

1. Select the folder to which you want to add the page reports and select **Add Page Reports** on the toolbar, or right-click the folder and select **Add Page Reports** from the shortcut menu.
2. In the [Choose Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009564702-Choose-Page-Report-Dialog) dialog, all the page reports in the current catalog are listed. Select the required ones.

   ![Choose Page Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893807255/chsrptst.gif)
3. Select the **Add** button to add the selected page reports to the folder. The default names of the report items are the file names of the reports. You can rename the report items as you would with a folder item.

A report can be added to multiple folders in case you want to include it in multiple categories. You can double-click any report item in the Page Report Manager to open the report.

## Editing the Properties of an Item

Select the item the properties of which you want to edit, select **Show Properties** on the toolbar, then edit its property values in the Properties sheet. After editing a value, press **Enter** on the keyboard to confirm the change. You can make use of the quick search toolbar to search for the desired properties (to display the toolbar, select the **Search** button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404893807511/btn_srch.gif) at the upper right corner of the Properties sheet). The search toolbar is closed when you select another item.

![Qiuck Search Toolbar button](https://devnet.logianalytics.com/hc/article_attachments/4404889288855/btn_srchtlbr.gif)

* **Text box**  
   The quick search toolbar treats resource names as strings and searches by consecutive text. Type in the text you want to search for in the text box and the resources containing the matched text will be listed.
* **X**  
   Clear the text in the text box.
* ![More Search Option button](https://devnet.logianalytics.com/hc/article_attachments/4404889289239/btn_srchtlbr_adv.gif)  
   Lists more search options.
  + **Highlight All**   
     Specifies whether to highlight all matched text.
  + **Match Case**   
     Specifies whether to search for text that meets the case of the typed text.
  + **Match Whole Word**   
     Specifies whether to search for text that looks the same as the typed text.

The properties of a folder item are:

| Property Name | Description |
| --- | --- |
| Description | Specifies the description of the folder. Data type: String |
| Name | Specifies the name of the folder. Data type: String |

The properties of a report item are:

| Property Name | Description |
| --- | --- |
| Author | Specifies the author of the report. Data type: String |
| Description | Specifies the description of the report. Data type: String |
| File Name | Specifies the name of the report. Data type: String |
| Keywords | Specifies the keywords of the report. Data type: String |
| Last Modified Time | Specifies the last time at which the report was modified. Data type: String |
| Last Print Time | Specifies the last time at which the report was printed. Data type: String |
| Last Run Time | Specifies the last time at which the report ran. Data type: String |
| Name | Specifies the display name of the report. Data type: String |
| Query Name | Specifies the query used by the report. Data type: String |
| Value Type | Specifies the type of the report. Data type: String |

## Searching for a Report or Folder Item

Wildcard searches for report name or folder name in the Page Report Manager are supported. To search a report or folder item, follow the steps below:

1. Select a folder item and right-click it.
2. Select **Search** on the shortcut menu to display the [Search Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009588941-Search-Reports-Dialog) dialog.

   ![Search Reports dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889289495/srchrpt.gif)
3. In the Find what text box, input the report or folder name, or report keywords you have specified for the Keywords property of the report in the Properties sheet, then select the corresponding search criteria from the By drop-down list, which can be by name, by keywords or by name or keywords.

   If you just input part of the report or folder name, or report keywords, use \* to replace the other part of the name or keywords. For example, if you want to search for the report EmployeeInformation, you should input *\*Info\** instead of *info* in the text box.
4. Specify what you want to find: a folder, a report or both.
5. Enter the search path in the Look in text box.
6. Specify whether to limit the search to text that exactly matches the case of the search text.
7. Specify whether to find the folder or report also in the sub folders of the search path.
8. Select the **Search Now** button to start searching. Matched results will be listed in the search result box.
9. If you want to start another search, select the **New Search** button and set the condition using the method described above.

## Exporting the Report Information to a Table

You can export report information in the Page Report Manager to a table in a DBMS. The default name of the table is ReportsInfo. You can change the name as required. Each row of the table is a report description. To do this:

1. Select the root folder **Reports** and right-click it.
2. On the shortcut menu, select **Export**. The [Get JDBC Connection Information](https://devnet.logianalytics.com/hc/en-us/articles/1500009587701-Get-JDBC-Connection-Information-Dialog) dialog appears.
3. Fill in the required fields for connecting to the DBMS, and then select the **OK** button.
4. Give a name for the table, and then select **OK** in the Input dialog. The report information is added to the table in the DBMS.

You can then [set up a JDBC connection](https://devnet.logianalytics.com/hc/en-us/articles/1500009584941-Setting-Up-a-JDBC-Connection) in a catalog to connect with the DBMS and [add the table](https://devnet.logianalytics.com/hc/en-us/articles/1500009584821-Tables-Views-Synonyms#Add) to the catalog via the JDBC connection for use.

**Note:** If a table already exists, it will be replaced. So you must be sure that there are no duplicate names in the DBMS.

## Moving an Item to Another Folder

Any items added to the Page Report Manager can be moved to another folder if required. You can use either of the following methods to move an item:

* **Using shortcut menu**  
  1. Right-click the item that you want to move and select **Move To** from the shortcut menu.
  2. The Move Report/Folder dialog appears. All the available folders are listed in the dialog.

     ![Move Report dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893807767/rpt_pgrpt_mngr_move.gif)
  3. Select the folder you want the item to be moved to, and select **OK**. The item will then be moved to that folder.
* **By dragging and dropping**  

  Drag the item to the destination folder.

## Deleting Items

Using the Page Report Manager, you can delete reports from the file system.

**To delete items from the Page Report Manager:**

1. Select the items on the Reports tree, and then take either of the following ways:
   * Press the **Delete** key on the keyboard.
   * Select the **Delete** button on the Page Report Manager toolbar.
   * Right-click and select **Delete** from the shortcut menu.
2. A Warning message box is displayed. Check the option **Also delete report files from file system** if you want to remove them from your local directory permanently. Otherwise leave the option unchecked and only remove the items from the virtual tree.
3. Select **Yes** in the box. If a report is selected, the report will be deleted. If a folder is selected, the folder and all its contents will be removed.

If a report is deleted manually from the local file system, later when you open the Page Report Manager, you will see the node icon that represents the report is marked with a red cross. You can use the above method to remove the unused node.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009570942-Setting-Filter-Options-for-an-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports)
