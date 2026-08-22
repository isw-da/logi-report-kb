---
title: "Developing Reports from HDS"
id: 1500009584761
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584761-Developing-Reports-from-HDS
updated_at: 2021-07-24T05:55:51Z
---

# Developing Reports from HDS

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564202-Connection-Plugins)

# Developing Reports from HDS

When you use hierarchical data sources to create reports, you need to be aware of its limitations and unique features. For example, reports created from an HDS are automatically grouped, and an HDS cannot be directly used to create charts and crosstabs. That is to say, if you want to create a chart or crosstab from an HDS, you will need to put it in a banded object, which is created on the HDS, and make the chart/crosstab inherit the [dataset](https://devnet.logianalytics.com/hc/en-us/articles/1500009592421-Creating-and-Managing-Datasets) of the banded object.

Hierarchical data sources can only be used to create page reports.

The following are two specific examples about developing reports from HD:

> * [Example 1: Developing a Report from an HDS with Dynamic XML URI](#Example1)
> * [Example 2: Developing a Report from a Parallel HDS](#Example2)

## Example 1: Developing a Report from an HDS with Dynamic XML URI

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, expand the data source to which to add the HDS.
3. Right-click the **Parameters** node and select **New Parameter** from the shortcut menu.
4. In the New Parameter dialog, enter a name for the parameter, choose **String** as the Value Type, and in the Prompt Values box, type in the URI of the XML file from which you HDS will be imported (for details, see [Creating a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter)).
5. Right-click the data source node in the Catalog Manager, and then select **New XML Hierarchical Data Source**. The New XML Hierarchical Data Source dialog appears.
6. In the XML URI box, type in **@ParameterName**. For example, if you named the parameter in step 2 as XML\_URI, here you should type in @XML\_URI. In the XSD URI box, specify the URI of the corresponding XSD file. Then select **OK** (for details, see [Importing the XML format HDS to a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog#XML)).
7. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) with the imported HDS. When you view the report, type in the URI of the XML file which matches the XSD file in the parameter. The report will then display the corresponding data.

In addition, you can also use another way to develop report with dynamic XML URI as explained below:

1. In the Catalog Manager, import an XML HDS with an XSD file, and then create a report with the imported HDS.
2. Create a parameter using the above method.
3. In the Catalog Manager, go to the node of the imported HDS, expand the Properties sheet, and then change the property URI to @ParameterName.
4. Now you can view the report with dynamic XML file.

## Example 2: Developing a Report from a Parallel HDS

The method for developing a report from a [parallel HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009584721-Hierarchical-Data-Sources#Parallel) is the same as from a general HDS. However, take note of the following when building reports from parallel HDSs.

**Groups in parallel HDS**

When you insert a group by field, its children will also be inserted.

The parallel structure in the parallel HDS is represented as groups in Logi JReport Designer. So, when you develop a report from a parallel HDS, it will automatically be grouped. By default, Logi JReport Designer will use the first found field as the group by field. Note that you can neither add a new group by field nor remove the group by fields that are automatically added. However, if there is more than one field available to with which to group the sub-tables, you can replace the group by field with one of the other available fields.

**Rules for inserting an object**

* Objects in different branches should be placed in the banded object panel they belong to. That is, a banded object panel cannot hold objects which belong to different branches.
* The children of a branch, including the columns, formulas, summaries, sub-branches, and children of the sub-branches, can be inserted into any of their parent panels. If the parent panel is shared by more than one branch, that is, if the parent panel works as a trunk (global panel), it can be shared by the children of all the branches it holds. However, note that each instance of a panel, such as a report/page/group header/footer panel, and detail panel, can only hold the children from the same branch. If you want to insert the children of different branches into the shared global panel, you will have to create as many instances of this panel as per the number of branches, and then insert the children of each branch into these panels.
* Where a formula/summary can be inserted depends on the branch attributes of the formula/summary. Generally speaking, when a formula/summary creates relationships with a column, it will obtain the same branch attributes as those of the related column, and it can be placed in the panels where the column can be placed.

  A global formula, which is not associated with any branch columns, can be placed to any position of the report.

  + When you remove a branch using the report wizard, the related panel will also be removed.
  + A chart based on a field can only be placed in its own panels, which include most of the global panels, except for the detail panel.
  + A crosstab must be built upon data of the same branch, and it should be placed in the location where the branch data resides.
  + Where a text box object can be inserted depends on the branch attributes of the columns (formulas/summaries) that it contains. A text box object can hold only the data of the same branch.

**Notes:**

* Since reports created from HDS are automatically grouped, in the Group screen of the banded wizard, you can neither add more groups by fields nor remove the existing ones. However, you can make changes to the existing group criteria. For example, you can replace a group by field with another one.
* When you want to publish reports created from [XML format hierarchical data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog#XML) to Logi JReport Server, the following method is recommended:
  1. In the Catalog Manager, select the HDS that is used by the report from the **Hierarchical** node, and then expand the Properties sheet.
  2. Change the URI property of the HDS to a relative path, for example, leaving only the name of the XML file.
  3. Create a new folder, and copy the report, the catalog, the XML file and the XSD file (if any) to the newly created folder.
  4. Select **File** > **Publish** > **Publish to Server** to publish the folder (for details, see [Publishing resources remotely](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Remotely)).
  5. Start Logi JReport Server. You will now be able to run the report on it.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564202-Connection-Plugins)
