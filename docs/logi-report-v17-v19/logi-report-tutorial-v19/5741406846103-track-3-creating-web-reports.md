---
title: "Track 3: Creating Web Reports"
id: 5741406846103
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741406846103-Track-3-Creating-Web-Reports
updated_at: 2022-11-30T02:36:32Z
---

# Track 3: Creating Web Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741379967255-Track-2-Creating-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741406645527-Track-4-Creating-Library-Components)

# Track 3: Creating Web Reports

Logi Report provides the web reporting solution that is aimed at easier and faster report creation and design, faster report execution, easier customization, and better presentation style using the newest Web technology. Web reports are viewed using a new interactive viewer called Web Report Studio, which provides a much nicer end user experience with many powerful features for interfacing with a report such as changing parameters without rerunning the report.

In Designer, report developers can create, open, and edit web reports; web reports end users create on Server can also be downloaded to Designer for further editing.

In this track, you have been asked to create a web report as the role of a report developer, based on the business view WorldWideSalesBV created in the [previous track](https://devnet.logianalytics.com/hc/en-us/articles/5741379967255-Track-2-Creating-Business-Views). The report should show each product's sales information, including order ID, order date, quantity, unit price, discount, and the total sales for each order. In order for end users to get sales information within a specific range conveniently, such as country or product name, you also need to add filter controls for dynamically filtering the data according to their requirements.

This track contains the following tasks:

* [Task 1: Create the Initial Report](#Task1)
* [Task 2: Improve the Report Layout](#Task2)
* [Task 3: Format the Report Components](#Task3)
* [Task 4: Preview the Report in Web Report Studio](#Task4)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif) To perform this track, you should have a Live license for Designer. If you need more information, contact [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.).

## Task 1: Create the Initial Report

1. Select **Logi Report Designer** in the **Logi Report** folder on the Start menu to open Designer.
2. Designer displays the main window and shows the Start Page by default. Close the Start Page.
3. Navigate to **File** > **Open Catalog**.
4. In the Open Catalog File dialog box, browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select **Open**.
5. Select **Yes** in the Warning dialog box. Designer displays the Catalog Manager. Close it because we do not use it in this lesson.
6. Navigate to **File** > **New** > **Web Report**. Designer creates a blank web report with a one-cell tabular.
7. Right-click the report body, select **Split** from the shortcut menu.

   ![Split Cell](https://devnet.logianalytics.com/hc/article_attachments/9905862258583/wbrpt_split.gif)
8. In the Split Cell dialog box, set both numbers to **2**, then select **OK**.

The report body is now hosted by four tabular cells. We want to put the filter controls in the left cells, and place a chart and a table in the right cells. First we create a chart to demonstrate the total sales of each product.

1. Select the right cell in the first tabular row, then navigate to **Insert** > **Chart**. Designer displays the Create Chart dialog box.
2. In the **Data** screen, select **WorldWideSalesBV**. Select **Next**.
3. In the **Type** screen, keep the default chart type **Clustered Bar 2-D** and select **Next**.
4. In the **Display** Screen, drag **Product Name** from the **Resources** box to the **X-Axis** box and **Total Sales** to the **Bar Length** box.

   ![Chart Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9905874062743/wbrpt_chtdsply.gif)
5. Select **Style** on the screen navigation bar to switch to the screen, select **Classic** as the chart style.
6. Select **Finish** to create the chart.

Next, we create a table to display the sales information just below the chart.

1. Select the right cell in the second tabular row, then navigate to **Insert** > **Table**.
2. In the Table Type dialog box, keep the default selection and select **OK**. Designer displays the Create Table dialog box.
3. In the **Data** screen, select **WorldWideSalesBV** and select **Next**.

   You can also select **More Option** and select the dataset the chart applies from the existing dataset list to [share the same dataset](https://devnet.logianalytics.com/hc/en-us/articles/5741393465495-Lesson-7-Creating-a-Tabular-Report#Dataset) between both components.

   ![Select Data Source for Table](https://devnet.logianalytics.com/hc/article_attachments/9905862315543/wbrpt_tbldt.gif)
4. In the **Display** Screen, drag the following objects from the **Resources** box to display in the table one by one: **Order ID**, **Order Date**, **Quantity**, **Unit Price**, **Discount**, and **Total**. Select **Next**.

   ![Table Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9905862351639/wbrpt_tbldsply.gif)
5. In the **Group** screen, add **Country** and **Product Name** as the group-by fields (Country is the higher group level).
6. Select **Style** to switch to the screen, then select **Classic** as the table style too.
7. Select **Finish** to create the table.

Next, we add two Text List filter controls to the report, so that at runtime end users can select one or more values in the filter controls to dynamically filter the chart and table.

1. Select the tabular cell on the left of the chart, navigate to **Insert** > **Web Controls** > **Filter Control**.
2. In the Insert Filter Control dialog box, keep the default filter control type in the **Control Type** drop-down list, select the group object **Country** from the **Select Fields** drop-down list, select outside the field drop-down list in the dialog box to finish selecting field, then select **OK** to insert the filter control.

   ![Insert Filter Control](https://devnet.logianalytics.com/hc/article_attachments/9905862373015/wbrpt_fltrcntrl.gif)
3. Select the tabular cell on the left of the table and insert another filter control in the cell, based on the field **Product Name** using the same way.

We also want to add a navigation control to help end users deal with the filter applying status in both filter controls in the report: go back to the previous filter applying status, go forward to the next, or clear all the filter applying histories. We place the navigation control above the chart in the report.

1. Right-click the blank area in the cell containing the chart and select **Insert Row Above** from the shortcut menu.
2. Select the right cell in the newly added tabular row, then navigate to **Insert** > **Web Controls** > **Navigation Control**.

Lastly, we insert an image to show the title of the report in the report page header panel.

1. Select the blank cell above the navigation control, then navigate to **Insert** > **Image**.
2. In the Select an Image dialog box, double-click **ProductSalesHeader.gif** to insert the image.

   By now, we have added all the components we need in separate tabular cells.

   ![Initial Report](https://devnet.logianalytics.com/hc/article_attachments/9905874166167/wbrpt_initiallrpt.gif)

## Task 2: Improve the Report Layout

In this task, we make some changes to the position and size of the components to improve the report layout.

1. Select **Tabular Cell 1** (the cell holding the image) in the report structure tree in the Report Inspector and edit its **Height** property to **0.9**.

   ![Edit Tabular Cell Height Property](https://devnet.logianalytics.com/hc/article_attachments/9905874197015/wbrpt_cellhght.gif)
2. Change the height of the image to make it fully occupy the cell it is in.
3. Select the tabular cell holding the navigation control, then drag the bottom border of the cell to make its height fit the height of the navigation control.

   ![Drag Tabular Cell Border to Change Height](https://devnet.logianalytics.com/hc/article_attachments/9905874229143/wbrpt_drgbrdr.gif)
4. Select the tabular cell that contains the table and drag its left border to widen the cell.
5. Select the table and drag its right border to fully display all columns in it.
6. Resize the chart to make it fully occupy the cell it is in.

The cell above the Country filter control is empty, so next we merge it with the cell that holds the Country filter control.

1. Select the empty cell and the cell containing the Country filter control, then right-click and select **Merge** from the shortcut menu.
2. Resize the two filter controls to make them fully occupy the cells they are in.

   The report shows as follows in design view now:

   ![Resize Components](https://devnet.logianalytics.com/hc/article_attachments/9905862506519/wbrpt_rpt.gif)

## Task 3: Format the Report Components

To improve the report appearance, we need to further format the components in the report. Let's start with the chart.

1. Right-click on the chart and select **Hide Legend** from the shortcut menu.
2. Right-click on any bar, then navigate to **Format Axes** > **Format Value (Y) Axis** on the shortcut menu.
3. In the Format Value (Y) Axis dialog box, go to the **Format** tab, select **Number** in the **Category** box, select **$#,##0** in the **Format** box, then select **Add** to add the format to the **Stack** box. Select **OK** to exit the dialog box.

   ![Change Value Format](https://devnet.logianalytics.com/hc/article_attachments/9905862550423/wbrpt_fmty.gif)

Next, we format the table by editing its object properties in the Report Inspector.

1. In the report structure tree of the Report Inspector, select the **Table Header** node and edit its **Background** property to **0x7da1d1**.

   ![Edit Table Header Color](https://devnet.logianalytics.com/hc/article_attachments/9905874312727/wbrpt_tblcolor.gif)
2. Select the **Table Group Header** node and set its **Background** property to **0xd9d9d9**, then select **Table Group Header 1** and set its **Background** property to **0xeeeeee**.
3. In the table, select the two group-by fields in the group headers (GH), resize them horizontally to make sure the country and product names do not get truncated, then in the Report Inspector, set the **Foreground** property of the two fields to **0x7da1d1**.
4. Select the **Order Date** DBField in the detail row (TD), then change its **Format** property to **MM/dd/yyyy** in the Report Inspector.
5. Select the **Unit Price** and **Total** DBFields in the detail row and edit their **Format** property to **$#,###.00**.
6. Select the **Discount** DBField in the detail row, then type **#,##0.00** in the value cell of its **Format** property.

   The chart and table now look as follows:

   ![Chart and Table](https://devnet.logianalytics.com/hc/article_attachments/9905862604183/wbrpt_chttbl.gif)

Next, we format the two filter controls and the navigation control.

1. Select the two filter controls in the report, then in the Report Inspector, set their **Border Color** property to **0x7ca2cf**, and edit **Background** and **Foreground** in the **Title** property group to **0x7ca2cf** and **White**.

   ![Edit Filter Control Properties](https://devnet.logianalytics.com/hc/article_attachments/9905874375831/wbrpt_fltrprpty.gif)
2. Select the three buttons in the navigation control, then edit their **Bold** property to **true**, **Background** to **0x7ca2cf**, and **Foreground** to **White**.

   The report applies the formatting and displays as follows in design view:

   ![Report in Design View](https://devnet.logianalytics.com/hc/article_attachments/9905874400535/wbrpt_fmtrpt.gif)
3. Navigate to **File** > **Save** to save the report as **Products.wls**.

## Task 4: Preview the Report in Web Report Studio

In this task, we use the Preview as Web Report Result command of Designer to preview the report and test the filter controls in the report. However, this command is enabled only if you have selected the option Server for Previewing Reports when installing Designer.

1. Navigate to **View** > **Preview As** > **Web Report Result**. The report runs in Web Report Studio in your default web browser.

   You may find that the report layout is not so perfect because Web Report Studio adopts responsive view by default to suit different mobile devices. To close responsive view, select **Customize Toolbar Items**![Customize Toolbar Items button](https://devnet.logianalytics.com/hc/article_attachments/9905874426519/btn_cstmz.gif) on the toolbar and select **Close Responsive Mode** from the menu list. The Close Responsive Mode button ![Close Responsive Mode button](https://devnet.logianalytics.com/hc/article_attachments/9905874462359/btn_rspnsvcls.gif) then appears on the toolbar. Select the button to close responsive view.

   ![Preview in Web Report Studio](https://devnet.logianalytics.com/hc/article_attachments/9905862762647/wbrpt_prvw.gif)

We can use the filter controls to dynamically change the report data. Since the chart and table apply the same business view and the filter controls use fields from this business view, Web Report Studio applies the filters created via the filter controls to both of them at the same time. First, we want to view the sales in Canada.

1. Select **Canada** in the **Country** filter control. Web Report Studio refreshes the chart and table to display the data for Canada only.

   ![View Data in Canada](https://devnet.logianalytics.com/hc/article_attachments/9905874526359/wbrpt_canada.gif)
2. To further view the product Kona Mountain's sales in Canada, select **Kona Mountain** in the **Product Name** filter control. Web Report Studio refreshes the report to show the corresponding data.

   ![Data for Kona Mountain](https://devnet.logianalytics.com/hc/article_attachments/9905874568215/wbrpt_prdct.gif)

Next, we want to view the sales of Blue Mountain, Breakfest Blend, and French Roast in all countries. Since the current report data is for Kona Mountain's sales in Canada, we need to remove the filters first.

1. Select **Clear**![Remove Filter button](https://devnet.logianalytics.com/hc/article_attachments/9905874609943/btn_clear.gif) on the title bar of each filter control to clear the value selection in them.

   You can also use the navigation control in the report to achieve the same goal: select **Back** twice to undo what you have just done in the previous two steps, or select **Clear** to simply clear the filter conditions in all filter controls.
2. Select and hold the **Ctrl** key, then select **Blue Mountain**, **Breakfest Blend**, and **French Roast** in the **Product Name** filter control. The report now shows as follows:

   ![Data for Three Product Names](https://devnet.logianalytics.com/hc/article_attachments/9905862918167/wbrpt_prdct1.gif)
3. Exit Web Report Studio.

   You can go to [Creating a Web Report Using the Quick Start Method](https://devnet.logianalytics.com/hc/en-us/articles/5741362698391-Lesson-1-Creating-a-Web-Report-Using-the-Quick-Start-Method) and [Creating a Web Report Using the Wizard](https://devnet.logianalytics.com/hc/en-us/articles/5741407392791-Lesson-2-Creating-a-Web-Report-Using-the-Wizard) to get more information about working with Web Report Studio.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741379967255-Track-2-Creating-Business-Views)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741406645527-Track-4-Creating-Library-Components)
