---
title: "Working with Subreports"
id: 5735521147415
section: "Working with Components in Reports - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports
updated_at: 2023-01-10T02:48:46Z
---

# Working with Subreports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735512413207-Working-with-Drawing-Objects)

# Working with Subreports

Logi Report refers to the report that you insert into another report as a subreport. The main benefits of using subreports are: you can insert a subreport into different primary reports, namely, you do not need to create it again and again for every primary report; you can show different data information in different subreports and insert them into the primary reports for comparison. A primary report can have more than one subreport. You can manage the subreports of a primary report in the way you do with other components in the primary report, but a subreport itself is created and managed as a primary report. This topic describes how you can insert subreports in a report and define the relationships between the primary report and the subreports.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can use subreports in page reports only.

This topic contains the following sections:

* [Inserting Subreports in a Page Report](#Insert)
* [Creating Links Between Primary Report and Subreport](#Link)
* [Setting Up Parameter Links Between Primary Report and Subreport](#Parameter)
* [Returning Values from Subreport to Primary Report](#Value)

**See an example:** The SampleComponents catalog, included with Designer, contains reports that have examples of how you could use each component type in a report. For the subreport examples, open `<install_root>\Demo\Reports\SampleComponents\Subreport_*.cls`.

## Inserting Subreports in a Page Report

1. Open the primary page report.
2. Position the mouse pointer at the [allowed report location](https://devnet.logianalytics.com/hc/en-us/articles/9898540172311-Component-Placement-in-Different-Report-Type) where you want to insert the subreport.
3. Navigate to **Insert** > **Subreport** or **Home** > **Insert** > **Subreport**, or drag the **Subreport** icon ![Subreport icon](https://devnet.logianalytics.com/hc/article_attachments/9898534523927/icon_sbrpt.gif) from the **Basic** category in the **Components** panel to the destination. If the destination is a banded panel or tabular cell and you use menu command, select in the destination. Designer displays the [Subreport dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735544631319-Subreport-Dialog-Box).

   ![Subreport dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898460670743/subrpt_fld.gif)
4. Select **Browse** to select the report which contains the report tab you want to use as the subreport. This report must belong to the same catalog as the primary report.
5. Select the required report tab as the subreport from the **Report Tab** drop-down list, which contains the names of all the report tabs in the specified report.
6. In the **Field** tab, select **Add**, then in the Choose Component dialog box, add the data components in the subreport that you want to interlink with the primary report. When the required data components apply the same dataset, you can add them all at a time. If they use different datasets, you need to add them respectively.
   After adding the data components, you can also change them by selecting ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9898477814935/btn_ellipsis3.gif) on the right and then selecting the new components.

   ![Choose Component dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898518218519/cmpnt_sbrpt_chscmpnt.gif)
7. From the **Component in Report Tab** box, select a data component and [set up links](#Link) between the primary report and the data component. Repeat this to define the link conditions between other data components in the subreport and the primary report.
8. If the subreport has parameters and you do not want to specify values for them at runtime, select the **Parameter** tab to [assign values to the parameters](#Parameter).
9. If you want the subreport to [return values](#Value) to the parameters of the primary report, select the **Return Value** tab and specify the settings.
10. Select **OK** to insert the subreport.

After you have inserted a subreport into a report, you can further format the subreport settings. To do this, right-click the subreport and select **Format Subreport** on the shortcut menu. In the Subreport dialog box, edit the settings according to your requirements.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* When you have inserted a report into another report as a subreport, if you later modify this report, you should go to the primary report and use the Format Subreport command to save the subreport settings again.
* When inserting subreports, you need to avoid link loops. For example, if you have inserted report B into report A as its subreport, you cannot insert report A into report B as its subreport again. It is the same case when you create the links between primary report and subreport, for example, if you set the links between the primary report A and subreport B (report A -> report B), you cannot set the link back to report A (report A -> report B -> report A).
* When passing values between the subreport and the primary report, you should avoid parameter loop, which may occur as this case: you assign parameter A of the primary report to parameter B of the subreport in the Parameters tab, while in the Return Value tab, you assign B to A. In this case, the values of A and B depend on the default values and the position relationship between the two parameters.
* Only the [page level formula](https://devnet.logianalytics.com/hc/en-us/articles/5735525461399-Formula-Levels) in a container below the subreport such as a banded panel or the report page footer panel can get the parameter values returned from the subreport.
* If the subreport crosses pages, the result of the formula may not be the value you expect, because Logi Report Engine only calculates the return value when it finishes laying out the subreport.
* You can use the "Show real view of subreport" option in the General category of the Options dialog box to specify whether to show the detailed subreport structure in the primary report in design mode. However,
  + For subreport with multiple pages, Designer only shows the report body in the first page in the primary report.
  + For cascading subreports, Designer only shows the first layer of the subreport in the primary report.

## Creating Links Between Primary Report and Subreport

A link is a way to connect the primary report and the subreport. When you define a link, Designer matches the records with equal relationships within the subreport and the primary report. You can apply one or more links to make the subreport and the primary report interlinked.

Assume that you have two reports in the same catalog: one contains a customer report tab which has a banded object inside and displays information of customer ID, country, city, and phone; the other contains an order report tab which contains a crosstab showing information of customer ID, product name, and quantity. Now you want to insert the order report tab as subreport into the customer report tab, and set up a link between them, so that when you view the customer report tab, Designer can build a subreport for each customer based on the order report tab, showing order records for only the specified customer. To achieve this, take the following steps:

1. Open the report that contains the customer report tab.
2. Select the detail panel of the banded object and navigate to **Insert** > **Subreport**. A box is then attached to the mouse pointer to indicate it is ready to place the subreport.
3. Select in the panel. Designer displays the Subreport dialog box.
4. Select **Browse** to select the report that contains the order report tab as the subreport.
5. In the **Field** tab, select **Add**.
6. Select **CTCrossTab** in the Choose Component dialog box, then select **OK**. Designer adds the crosstab in the **Component in Report Tab** box.
7. From the resource tree in the left box, add the **Customers\_CustomerID** field in the customer report tab to the **Field** box, Designer then automatically sets up a link as follows:

   | Fields(Primary) | OP | Fields(Subreport) |
   | --- | --- | --- |
   | Customers\_Customer ID | = | CUSTOMERS\_CUSTOMERS ID |
8. Select **OK** to apply the settings.
9. Select the **View** tab to preview the customer report tab. You can find that Designer generates a crosstab for each customer based on the customer ID.

   ![Preview the Report](https://devnet.logianalytics.com/hc/article_attachments/9898518242967/cmpnt_sbrpt_link.gif)

## Setting Up Parameter Links Between Primary Report and Subreport

If a subreport contains parameters, users must supply the values at runtime. You can map the subreport parameters to fields that are in the dataset of the data component where you insert the subreport in the primary report, and are of the same data type as the subreport parameters, so that the subreport parameters can obtain values from the mapped fields automatically. However, if you map a subreport parameter to another parameter in the primary report, users still need to specify its value at runtime, but the parameter name is that of the mapping parameter.

Assume that you have two reports in the same catalog: Report A (with Report Tab A in it) and Report B (with Report Tab B in it). Report Tab B has a parameter PToday (Date type). Then, you insert Report Tab B as subreport into Report Tab A. When you preview Report Tab A, Designer prompts you to specify a value for its subreport parameter PToday. However, you do not want to specify the value each time you run Report Tab A and instead want to give it a fixed value. You can then set up a parameter link between the primary report and subreport as follows to achieve the goal.

1. Right-click the inserted subreport in Report Tab A and select **Format Subreport**.
2. In the Subreport dialog box, select the **Parameters** tab (Designer disables this tab if the subreport does not contain any parameters).
3. In the **Parameters** column, you can see Designer lists **PToday** there and assigns a same name parameter to it by default in the **Value** column.
4. Select the drop-down list in the Value column which lists the available fields of the Date type in the dataset of Report Tab A. Here, we select **MYTODAY** which is a predefined formula and returns a value *CurrentDate()*.

   ![Set a Value for the Supreport Parameter](https://devnet.logianalytics.com/hc/article_attachments/9898534544535/cmpnt_sbrpt_prmtr.gif)
5. Select **OK** to apply the settings.
6. Select the **View** tab to preview Report Tab A. Designer prompts no parameter dialog box to specify the value since it passes the formula value to PToday.

## Returning Values from Subreport to Primary Report

[Similarly](#Parameter), you can also return values of the subreport fields to parameters of the primary report, so that users do not need to specify values for the primary report parameters at runtime.

1. In the Subreport dialog box, select the **Return Value** tab.

   ![Subreport dialog box - Return Value](https://devnet.logianalytics.com/hc/article_attachments/9898460686871/subrpt_value.gif)
2. In the **Component in Report Tab** box, select the data component in the subreport, the fields of which you want to use to return value to parameters of the primary report, the **Field in Subreport** box then lists the available fields in the selected data component.
3. Select the field that you want to assign to a parameter in the primary report and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif). Designer then adds a parameter in the primary report of the same data type in the **Parameters** column of the **Return Value** box. If the automatically assigned parameter is not what you need, select the required parameter from the drop-down list in the Parameter column.
4. Select other data components in the Component in Report Tab box to set more mapping fields for parameters in the primary report.
5. Select **OK** to apply the settings.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735527727383-Working-with-Text-Boxes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735512413207-Working-with-Drawing-Objects)
