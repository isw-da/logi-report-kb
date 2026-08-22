---
title: "Saving a Page Report"
id: 1500009571042
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009571042-Saving-a-Page-Report
updated_at: 2021-07-24T05:53:47Z
---

# Saving a Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592901-Making-High-efficiency-Reports)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571002-Opening-a-Page-Report)

# Saving a Page Report

After you have created or modified a page report, you should then save it in order to be able to load it the next time.

By default, page report files contain a .cls suffix. This is the format that provides optimal performance in the Logi JReport toolset. Page report files can also be stored in the following formats:

* **Report Template (.rpt)**  
   It is a file saved in text format, which can be edited in any text editor.
* **Self Contained Page Report (.clx)**  
   It is a binary report file, which contains not only the report's layout but also the catalog with its own resources.
* **Page Report XML Format (.cls.xml)**  
   It follows the XML standard, which can be edited with both Logi JReport Designer and external XML editors. Page reports that contain customized [User Defined Objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009563782-UDOs) (UDO) cannot be saved to XML format. Using the XML format is better for checking into source code control systems than using the binary formats. The XML feature for page reports is under license control. To obtain the special key, contact Jinfonet Support ([support@jinfonet.com](mailto:support@jinfonet.com)).

Below is a list of the sections covered in this topic:

> * [Saving a Page Report in its Current Format](#Format)
> * [Saving a Page Report in a Different Name in the Current Directory](#Name)
> * [Saving a Page Report to a Different Catalog](#SaveTo)

## Saving a Page Report in its Current Format

To save a page report in its current format, select **Home**/**File** > **Save**. If the page report to be saved is new, the Save Report As dialog will appear for you to input a name.

This operation can also be accomplished by pressing the Ctrl + S keys.

## Saving a Page Report in a Different Name in the Current Directory

1. Select **File** > **Save As**.
2. In the [Save Report As](https://devnet.logianalytics.com/hc/en-us/articles/1500009589041-Save-Report-As-Dialog-for-Page-Report-) dialog, type a new file name in the Report Name field.

   ![Save Report As dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893806231/svrptas.gif)
3. Select a report type from the Report of Type drop-down list.
4. Select **Save** to save the page report in the new name. The new report is now the current report in Logi JReport Designer.

## Saving a Page Report to a Different Catalog

Since the resources for a catalog file are shared by all reports based on it, if you have different developers develop reports at the same time, and you want to use the same catalog in order for all the resources to be reused, you can have them save their reports with their related resources to a "universal" catalog file. In this way, the to-be-saved report's resources such as queries, formulas, and parameters will be merged into the target "universal" catalog file.

**To save a page report to a different catalog:**

1. Select **File** **>****Save To**.
2. Browse to the location of the target catalog, then select **Save**. The target catalog must have the same name as the current catalog.
3. In the Warning message box, select **Yes**.

   This saves your report into a target catalog file, which means:

   * The report and the relevant files alike will be copied to the directory where the target catalog file is located.
   * The resources (query, formulas, parameters, and so on) that are referenced by this report in the current catalog will be merged to the target catalog. If there are any conflicts they will be identified according to the Merge Catalog Option settings in File > Options > Catalog. There are three options: Identify all differences, Identify critical differences (default) or Ignore differences.
   * If the connection does not exist yet in the target catalog, it will be added using the same connection information as in the source catalog.

In this way, even while users work with their own individual catalog files, they can still publish their reports and associated resources to the target "universal" catalog file. Note that Logi JReport does not handle concurrency issues. Two people cannot update the "universal" catalog at the same time.

See also [Merging Catalogs](https://devnet.logianalytics.com/hc/en-us/articles/1500009562762-Merging-Catalogs) for more information about the Save To command.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592901-Making-High-efficiency-Reports)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571002-Opening-a-Page-Report)
