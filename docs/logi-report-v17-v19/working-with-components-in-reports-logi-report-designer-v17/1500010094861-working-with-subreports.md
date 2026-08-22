---
title: "Working with Subreports"
id: 1500010094861
section: "Working with Components in Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010094861-Working-with-Subreports
updated_at: 2021-07-23T19:14:48Z
---

# Working with Subreports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094981-Working-with-Text-Boxes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057222-Working-with-Drawing-Objects)

# Working with Subreports

Logi Report refers to the report that is inserted into another report as a subreport. This topic describes how you can insert subreports in a report and define the relationships between the primary report and the subreports.

The main reasons to consider a subreport are as follows: to insert the subreport into different primary reports, namely, you do not need to create it again and again for every primary report; to show different data information in different subreports and then insert them into the primary reports for comparison.

You can manage the subreports of a primary report in the way you do with other components in the primary report, but a subreport itself is created and managed as a primary report. A primary report can have more than one subreport.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You can use subreports in page reports only.

This topic contains the following sections:

* [Inserting Subreports in a Page Report](#Insert)
* [Creating Sublinks Between Primary Report and Subreport](#Link)
* [Setting Up Parameter Links Between Primary Report and Subreport](#Parameter)
* [Returning Values from Subreport to Primary Report](#Value)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the subreport examples, open `<install_root>\Demo\Reports\SampleComponents\Subreport_*.cls`.

## Inserting Subreports in a Page Report

1. Open the primary page report.
2. Position the mouse pointer at the destination where you want to insert the subreport. You can insert a subreport in the page report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010094261-Working-with-Components-in-Reports#Relationship).
3. Select **Insert** > **Subreport**, **Home** > **Insert** > **Subreport**, or drag the **Subreport** icon ![Subreport icon](https://devnet.logianalytics.com/hc/article_attachments/4404857039767/icon_sbrpt.gif) from the Basic category in the **Components** panel. Then,
   * If the destination is the report body or a tabular cell, Designer displays the [Subreport dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010060682-Subreport-Dialog-Box).
   * If the destination is a banded panel, select the mouse button in the panel to open the Subreport dialog box.

   ![Subreport dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856892055/subrpt_fld.gif)
4. Select the **Browse** button to select the report which contains the report tab you want to use as the subreport. This report must belong to the same catalog as the primary report.
5. Select the required report tab as the subreport from the **Report Tab** drop-down list, which contains the names of all the report tabs in the specified report.
6. In the **Field** tab, select the **Add** button, then in the Choose Component dialog box, add the components in the subreport you want to be interlinked with the primary report with conditions. If the required components use different datasets, you need to add them respectively; however, as long as the components are based on the same dataset, you can add them all at the same time.
   After adding the components, you can change them by selecting the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404857040023/btn_ellipsis2.gif) on the right and then selecting new components.

   ![Choose Component dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857040279/cmpnt_sbrpt_chscmpnt.gif)
7. From the **Component in Report Tab** box, select a component and [set up links](#Link) between the primary report and the component as required. Repeat this to define the link condition between other components in the subreport and the primary report.
8. If the subreport has parameters and you do not want to specify values for them at runtime, select the **Parameter** tab to [assign values to the parameters](#Parameter).
9. If you want the subreport to [return values](#Value) to the parameters of the primary report, select the **Return Value** tab and specify the settings according to your requirements.
10. Select **OK** to insert the subreport.

After you have inserted a subreport into a report, you can further format the subreport settings. To do this, right-click the subreport and select **Format Subreport** on the shortcut menu. In the Subreport dialog box, edit the settings according to your requirements.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* When you have inserted a report into another report as a subreport, if you later modify this report, it is recommended that you go to the primary report and use the Format Subreport command to save the subreport settings again.
* When inserting subreports, you need to avoid link loops. For example, if you have inserted report B into report A as its subreport, then you cannot insert report A into report B as its subreport again. It is the same case when creating sub-links, for example, if you set the links between the primary report A and subreport B (report A -> report B), you cannot set the link back to report A (report A -> report B -> report A).
* When passing values between the subreport and the primary report, you should avoid parameter loop, which may occur as this case: you assign parameter A of the primary report to parameter B of the subreport in the Parameters tab, while in the Return Value tab, you assign B to A. In this case, the values of A and B depend on the default values and the position relationship between the two parameters.
* Only the page level formula placed in a container below the subreport such as a banded panel or the report page footer panel can get the parameter values returned from the subreport. To use the return value parameter in a formula, you need to add "PageNumber" in the first line in the formula. For more information, see [Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/1500010061022-Formula-Levels).

  For example, all the formulas which referenced the return value parameter should be like:

  PageNumber;  
   ... ... ...  
   ... ... ...
* If the subreport crosses pages, the result of the formula may not be the value you expect, because Logi Report Engine only calculates the return value when finishing laying out the subreport.
* You can use the option "Show real view of subreport" in the General category of the Options dialog box (File > Options > General) to specify whether or not to show the detailed subreport structure in the primary report in design mode. However,
  + For subreport with multiple pages, Designer only shows the report body in the first page in the primary report.
  + For cascading subreports, Designer only shows the first layer of the subreport in the primary report.

## Creating Sub-links Between Primary Report and Subreport

A sub-link is a way to connect the primary report and the subreport. When you define a sub-link, Logi Report Engine matches the records with equal relationships within the subreport and the primary report. You can apply one or more links to make the subreport and the primary report interlinked.

The following example explains the use of sub-links in detail.

Assume that you have two reports in the same catalog: one contains a customer report tab which has a banded object inside and displays information of customer ID, country, city, and phone; the other contains an order report tab which contains a crosstab showing information of customer ID, product name, and quantity. Now you want to insert the order report tab as subreport into the customer report tab, and set up a link between them, so that when the report users views the customer report tab, Logi Report Engine can build a subreport for each customer based on the order report tab, showing order records for only the specified customer.

To achieve this, take the following steps:

1. Open the report that contains the customer report tab.
2. Select the detail panel of the banded object and select **Insert** > **Subreport**. A box is then attached to the mouse pointer to indicate it is ready to place the subreport.
3. Select in the panel. Designer displays the Subreport dialog box.
4. Select the **Browse** button to select the report that contains the order report tab as the subreport.
5. In the **Field** tab, select the **Add** button.
6. Select **CTCrossTab** in the Choose Component dialog box, then select **OK**. Designer adds the component in the **Component in Report Tab** box.
7. From the resource tree in the left box, add the **Customers\_CustomerID** field in the customer report tab to the **Field** box, Designer then automatically sets up a link as follows:

   | Fields(Primary) | OP | Fields(Subreport) |
   | --- | --- | --- |
   | Customers\_Customer ID | = | CUSTOMERS\_CUSTOMERS ID |
8. Select **OK** to apply the settings.
9. Select the **View** tab to preview the customer report tab. You can find that Designer generates a crosstab for each customer based on the customer ID as follows:

   ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/4404857040535/cmpnt_sbrpt_link.gif)

## Setting Up Parameter Links Between Primary Report and Subreport

If a subreport contains parameters, the report users must supply the values at runtime. You can map the subreport parameters to fields which are contained in the dataset of the component where you insert the subreport in the primary report, and are of the same data type as the subreport parameters, so that the subreport parameters can obtain values from the mapped fields automatically. While, if you map a subreport parameter to another parameter in the primary report, Logi Report Engine still prompts the report users to specify the value at runtime, but the parameter name is that of the mapping parameter.

The following example shows how to set up parameter links between a primary report and a subreport.

Assume that you have two reports in the same catalog: Report A (with Report Tab A in it) and Report B (with Report Tab B in it). Report Tab B has a parameter PToday (Date type). Then, you insert Report Tab B as subreport into Report Tab A. When you preview Report Tab A, Designer prompts you to specify a value for its subreport parameter PToday. However, you do not want to specify the value each time you run Report Tab A and instead want to give it a fixed value. To achieve this, follow the steps below:

1. Right-click the inserted subreport in Report Tab A and select **Format Subreport**.
2. In the Subreport dialog box, select the **Parameters** tab (Designer disables this tab if the subreport does not contain any parameters).
3. In the **Parameters** column, you can see Designer lists **PToday** there and assigns a same name parameter to it by default in the **Value** column.
4. Select the drop-down list in the Value column which lists the available fields of Date type in the dataset of Report Tab A. Here, we select **MYTODAY** which is a predefined formula and returns a value *CurrentDate()*.

   ![Set a Value for the Supreport Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404848669335/cmpnt_sbrpt_prmtr.gif)
5. Select **OK** to apply the settings.
6. Select the **View** tab to preview Report Tab A. Designer prompts no parameter dialog box to specify the value since it passes the formula value to PToday.

## Returning Values from Subreport to Primary Report

[Similarly](#Parameter), you can also make values of the subreport fields return to parameters of the primary report, so that the report users do not need to specify values for the primary report parameters at runtime. To do this:

1. In the Subreport dialog box, select the **Return Value** tab.

   ![Subreport dialog box - Return Value](https://devnet.logianalytics.com/hc/article_attachments/4404856892311/subrpt_value.gif)
2. In the **Component in Report Tab** box, select the component in the subreport, the fields of which you want to use to return value to parameters of the primary report, the **Field in Subreport** box then lists the available fields in the selected component.
3. Select the field that you want to assign to a parameter in the primary report, select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848391191/btn_addarrow.gif). Designer then adds a parameter in the primary report of the same data type in the **Parameters** column of the **Return Value** box. If the automatically assigned parameter is not what you need, select the required one from the drop-down list in the Parameter column.
4. You can select another component in the Component in Report Tab box and set more mapping fields for parameters in the primary report.
5. Select **OK** to apply the settings.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010094981-Working-with-Text-Boxes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057222-Working-with-Drawing-Objects)
