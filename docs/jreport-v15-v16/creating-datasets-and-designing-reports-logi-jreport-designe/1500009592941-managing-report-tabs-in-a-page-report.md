---
title: "Managing Report Tabs in a Page Report"
id: 1500009592941
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592941-Managing-Report-Tabs-in-a-Page-Report
updated_at: 2021-07-24T05:53:46Z
---

# Managing Report Tabs in a Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592961-Previewing-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592901-Making-High-efficiency-Reports)

# Managing Report Tabs in a Page Report

This topic demonstrates how to manage report tabs in a page report with the report tab bar as follows:

* **Inserting a new report tab into a page report**
  1. On the report tab bar, right-click any report tab and select **Insert** from the shortcut menu.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4404889286039/rpt_pgrpt_tab.gif)
  2. In the Select Component for Page Report Tab dialog, specify the title and layout of the new report tab, then select **OK**.
  3. [Create the report tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009571062-Creating-Report-Tabs-in-a-Page-Report) according to your requirements.
* **Renaming a report tab** 
  1. On the report tab bar, right-click the report tab with the name you want to change and select **Rename** on the shortcut menu.
  2. In the Input Report Tab Name dialog, enter a new name for the report tab.
  3. Select **OK** to confirm the name.
* **Importing report tabs into a page report**

  Logi JReport enables you to import report tabs to a page report from another page report in the same catalog, and specify [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets) for the imported [components](https://devnet.logianalytics.com/hc/en-us/articles/1500009583241-Working-with-Components-in-Reports) according to your requirements.

  1. Select **File** > **Import From** > **Logi JReport Page Report**.
  2. In the Open Report dialog, specify the page report that contains the report tabs you want to import, then select **Open**.

     The [Select Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009567542-Select-Report-Tab-Dialog) dialog appears.

     ![Select Report Tab dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889288087/slctrpt.gif)
  3. Select the report tabs that you want to import.
  4. If you want to customize datasets used by components within the to be imported report tabs, check the **Customize Dataset for Components** option. Then select **OK** and the [Customize Dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009586221-Customize-Dataset-Dialog) dialog appears.

     ![Customize Dataset dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889288343/cstmzdtst.gif)
  5. All components in the selected report tabs, which have self-bound datasets, will be listed in the dialog. Specify which dataset you want the component to use by selecting its Dataset Name cell and choosing from the drop-down list.
  6. Select **OK** to import the report tabs with specified datasets to their components. The imported report tabs will be listed after the existing report tabs in the page report.
* **Copying a report tab**

  To copy a report tab, on the report tab bar, right-click the report tab you want to copy and select **Copy** on the shortcut menu. Then,

  + If you want to make a copy of the report tab within the current report, right-click any report tab and select **Paste** from the shortcut menu. You will then be prompt to give the report tab a new name. Specify the name as required.
  + If you want to copy the report tab to another page report of the same catalog, open the report to which the report tab will be copied, then right-click any report tab and select **Paste** from the shortcut menu. The report that you are copying from must still be open in Designer.
* **Moving a report tab to another page report**
  1. On the report tab bar, right-click the report tab you want to move and select **Cut** on the shortcut menu.
  2. Open the page report where the report tab will be moved.
  3. Right-click any report tab and select **Paste** on the shortcut menu.
* **Duplicating a report tab** 

  To make a duplicate report tab in the current page report, right-click the report tab on the report tab bar, and then select **Duplicate** on the shortcut menu.

**Removing a report tab**

To remove a report tab from a page report, right-click the report tab on the report tab bar, and then select **Remove** on the shortcut menu.

**Note:** Since a page report cannot be empty, you will not be able to remove all of the report tabs in the page report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592961-Previewing-a-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592901-Making-High-efficiency-Reports)
