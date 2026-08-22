---
title: "Lesson 5: Creating a Table Report"
id: 1500010056182
section: "Logi Report Tutorial v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010056182-Lesson-5-Creating-a-Table-Report
updated_at: 2021-07-23T19:14:19Z
---

# Lesson 5: Creating a Table Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093221-Lesson-4-Creating-a-Chart-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093241-Lesson-6-Creating-a-Crosstab-Report)

# Lesson 5: Creating a Table Report

The Jinfonet Gourmet Java company receives orders from customers in different territories around the world, and by reviewing this shipping information the Shipping Department can receive bids from various shipping vendors. You are assigned the task of creating a shipment information report. In the report, the shipment details, including order ID, order date, ship date, shipping cost, whether the payment has been received, and the shipping vendor, need to be reported for each territory.

The following prototype of the report has been given to you:

![Report Sketch](https://devnet.logianalytics.com/hc/article_attachments/4404857149079/rpt_lsn5_model.gif)

This report will be run online by employees in the Shipping Department. The interactive functionalities of Logi Report page reports enable end users to change the view of the reports, filter the data, change the sort order, search the report, and so on. Each end user can get the data he needs from a single report.

Follow the tasks below to finish creating the report:

* [Task 1: Create the Table](#Task1)
* [Task 2: Add a Web Control to the Report](#Task2)
* [Task 3: Add Objects and Edit Properties](#Task3)

## Task 1: Create the Report

Before taking this task, make sure you have enabled the Insert field name label with field option in the Options dialog box as [described at the last step of Lesson 3](https://devnet.logianalytics.com/hc/en-us/articles/1500010093201-Lesson-3-Creating-a-Mailing-Label-Report#Options). Otherwise, the name labels will not be inserted together with the fields when you add fields to the table.

1. In Designer, select **File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog box, select **Table (Group Above)** and select **OK**.

   Be sure that JinfonetGourmetJava.cat is specified as the current catalog because it is the catalog we use in this track. For information about specifying this catalog, see [Task 1, Step 2 and 3](https://devnet.logianalytics.com/hc/en-us/articles/1500010056142-Lesson-1-Creating-a-Standard-Banded-Report#SelectCat) of Lesson 1.
3. In the Data screen of the Table Wizard dialog box, select **<New Query...>** in the Queries node of Data Source 1, type **ShipmentDetailsbyCustomer** in the Enter Query Name dialog box and select **OK**.
4. In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the **Tables** node, then select the tables **Customers** and **Orders** and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848768535/btn_addarw.gif) to add them to the query. Select **OK** to close the dialog box.
5. In the Query Editor dialog box,
   the two tables are joined together automatically on the Customers\_Customer ID and CustomerID\_FK1 columns.

   ![Join Between Tables](https://devnet.logianalytics.com/hc/article_attachments/4404857149335/rpt_lsn5_addtbl.gif)
6. Select all the columns in the Orders table by selecting the **\*** checkbox. For the Customers table, select the following columns: **Customer Name**, **Customers\_State**, **Customers\_Country**, **Customers\_Territory** and **Customers\_Region**.
7. Select **OK** to create the query.
8. Select **Next** in the Table Wizard dialog box.
9. In the Display screen, add the fields **Orders\_Order ID**, **Order Date**, **Ship Date**, **Ship Via**, **Payment Received** and **Shipping Cost** to the table by selecting them and selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848768535/btn_addarw.gif) one by one.

By default, Designer displays the records in a table in the order they are returned from the fetch operation. You can specify to sort the records in a table, and also within the groups in table if any. In this lesson, we will make the records in the table sorted by order ID ascendingly.

1. Select the **Sort Fields By** button at the right bottom corner of the Display screen. In the Sort Fields By dialog box, select **Orders\_Order ID** in the Resources box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848768535/btn_addarw.gif) to add it as the sort by field, then select **OK** to return back to the Table Wizard dialog box.

   ![Add Sort-by Field](https://devnet.logianalytics.com/hc/article_attachments/4404857149591/rpt_lsn5_srtfld.gif)
2. Select **Next** in the Table Wizard dialog box to display the Group screen.

Since the report is required to display shipment details of each customer in specific territory, we will add two groups to it: first group the report by territory and then by customer name.

1. In the Group screen, add the DBFields **Customers\_Territory** as the first group-by field and **Customer Name** the second one.

   ![Add Groups](https://devnet.logianalytics.com/hc/article_attachments/4404857149847/rpt_lsn5_grptb.gif)
2. Select **Style** to switch to the screen and select to display the report in the **Classic** style vertically.
3. Select **Finish** to create the report.
4. Select the **View** tab to preview the report. Designer displays the report as follows:

   ![Preview Report Draft](https://devnet.logianalytics.com/hc/article_attachments/4404857150103/rpt_lsn5_draft.gif)

The required report has been created, but it is cumbersome to locate the shipment details of specific territories. So our next task is to add web controls to the report so that the end user can easily filter the results of the report.

## Task 2: Add a Web Control to the Report

Web controls empower end users of interactive reports to easily modify the report results they are viewing, and are defined by a trigger event, such as select, and a resulting web action.

In this task, we add a Drop-down List web control to the page header panel of the report. It will be used to filter the report records by territory.

1. Select **View** > **Page Header** to display the page header panel.
2. In the Report Inspector, select the **Page Header Panel** node and change its Height property to **1.25**.
3. Select **Insert** > **Web Controls** > **Drop-down List** to insert a web control into the panel.

1. Right-click the web control and select **Display Type** from the shortcut menu.
2. In the Display Type dialog box, select in the **Value** column and then select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848766999/btn_chsr.gif) in it to display the Insert Fields dialog box.
3. Select **Customers\_Territory**  in the Customers table in the DBField List box and select the **Insert** button to add it as value of the drop-down list.
4. In the Web Behaviors box, select **Data Change** from the drop-down list in the Events column, then select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404848766999/btn_chsr.gif) in the **Actions** column.

   ![Edit Display Type](https://devnet.logianalytics.com/hc/article_attachments/4404857150359/rpt_lsn5_optn.gif)
5. In the Web Action List dialog box, select the **\*Filter** action and select **OK**.
6. In the Filter - Web Action Builder dialog box, specify to apply the action to **TableComp**, select the **Filter On** cell and select **CUSTOMERS\_TERRITORY** from the drop-down list, then select the **Value** cell and select **MultiValueContainer**. Select **OK** to apply the settings.

   ![Define the Filter Web Action](https://devnet.logianalytics.com/hc/article_attachments/4404848778519/rpt_lsn5_bldr.gif)
7. Select **OK** in the Display Type dialog box to confirm the settings.
8. Resize the drop-down list horizontally to make sure the territory name can be displayed completely.

## Task 3: Add Objects and Edit Properties

In this task we will add more labels in the report, one as the report title and the other for data identification. We will also edit the properties of some objects to improve the report appearance.

1. Drag and drop the **Label** icon ![Label button](https://devnet.logianalytics.com/hc/article_attachments/4404857144983/btn_label.gif) twice from the Basic group in the Components panel to the page header panel to add two labels in it. Resize them and edit their text as follows:

   ![Add Label](https://devnet.logianalytics.com/hc/article_attachments/4404848778775/rpt_lsn5_lbl.gif)
2. Select the two labels by holding the Ctrl key on the keyboard and select **Format** > **Bold**![Bold button](https://devnet.logianalytics.com/hc/article_attachments/4404848779031/btn_bold.gif).
3. Resize the **Shipment Details by Customer** label, set its Font Size property to **18** and Foreground property to **Red** in the Report Inspector.

   ![Set Label Properties](https://devnet.logianalytics.com/hc/article_attachments/4404857150615/rpt_lsn5_red.gif)
4. Select the **Order Date** and the **Ship Date** DBFields by holding the Ctrl key on the keyboard and set their Format property to **M/d/yyyy** in the Report Inspector.
5. Resize the group-by fields in the two GH rows, add two labels ahead of them and edit the text of the labels as "**Territory:**" for the first group-by field and "**Customer Name:**" for the second, then select the two lables and the two group-by fields by holding the Ctrl key on the keyboard and set their Bold property to true.
6. Select the four objects in the two group header rows by holding the Ctrl key on the keyboard, set their Foreground property to **0xcc0000**.

   ![Edit Group Field Properties](https://devnet.logianalytics.com/hc/article_attachments/4404848779543/rpt_lsn5_grpfld.gif)
7. Double-click the **Orders\_Order ID** label in the TH row and edit its text to **Order ID**.
8. Select the **Ship Via** DBField and resize it to make sure no data get truncated. Do the same to the Payment Received label.

Next, we will apply a different background color to the two group header rows and hide the second group footer row to improve the appearance and layout of the report.

1. In the Report Inspector, select the **Table Comp** node from the report structure tree and set its Include Header and Footer property to **false** to cancel the alternating color for the table headers, group headers, and group footers so that we can customize the color for the group headers.
2. In the Report Inspector, select the **Table Group Header** and **Table Group Header 1** nodes from the report structure tree by holding the Ctrl key on the keyboard and set their Background property to **0xc0c0c0**.

   ![Edit Group Header Background Color](https://devnet.logianalytics.com/hc/article_attachments/4404848779799/rpt_lsn5_grphdr.gif)
3. Right-click on the second GF row and select **Hide** from the shortcut menu to hide it.

   ![Hide Group Footer](https://devnet.logianalytics.com/hc/article_attachments/4404848780695/rpt_lsn5_hide.gif)
4. On the report tab bar, right-click the report tab and select **Rename** to rename it to **ShipmentDetails**.

   ![Rename Report Tab](https://devnet.logianalytics.com/hc/article_attachments/4404848769687/renmrpttb.gif)
5. Select **File** > **Save** to save the report as **ShipmentDetailsbyCustomer.cls**.
6. Select the **View** tab to preview the report. Designer displays the report as follows:

   ![Preview Report](https://devnet.logianalytics.com/hc/article_attachments/4404857151255/rpt_lsn5_prvw.gif)

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If the report does not look correct, you can compare it to the final version of the report included in Designer. To do this, save and close your current catalog, and then open the **JinfonetGourmetJava.cat** catalog file located at `<install_root>\Demo\Reports\TutorialReports`.

The web controls are powered by Page Report Studio and therefore cannot work in Designer. We can use the Preview as Page Report Result command of Designer to preview this report, however this command is enabled only if the option Server for Previewing Reports was specified when installing Designer.

Select **View** > **Preview As** > **Page Report Result**. The report is then opened in Page Report Studio in the default web browser. Now we can select values from the drop-down list to dynamically change the report results. In the report below, we choose to view records in the Mexico territory.

![Preview in Page Report Studio](https://devnet.logianalytics.com/hc/article_attachments/4404857151511/rpt_lsn5_dhtml.gif)

You can go to [Creating and Performing Data Analysis on Page Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010093621-Lesson-3-Creating-and-Performing-Data-Analysis-on-Page-Reports) in the Quick Start part to get more information about working with Page Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856777623/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010093221-Lesson-4-Creating-a-Chart-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404848352023/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010093241-Lesson-6-Creating-a-Crosstab-Report)
