---
title: "Track 4: Creating Library Components"
id: 5741406645527
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741406645527-Track-4-Creating-Library-Components
updated_at: 2022-11-30T02:36:32Z
---

# Track 4: Creating Library Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741406846103-Track-3-Creating-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741379857559-Track-5-Publishing-Running-and-Administering-Resources)

# Track 4: Creating Library Components

Library components are used by end users to [build dashboards](https://devnet.logianalytics.com/hc/en-us/articles/5741385561367-Track-2-Self-Service-Dashboard-with-Logi-Report) using JDashboard, a separately licensed product on Server. Library components are created and edited in Designer, and then published along with their catalog to the component library on Server for use in dashboards.

In this track, you have been asked to create two library components as a report developer, based on the business view WorldWideSalesBV created in the [previous track](https://devnet.logianalytics.com/hc/en-us/articles/5741379967255-Track-2-Creating-Business-Views). One library component should contain a table that shows each product's order details, including order ID, quantity, unit price, and the total sales for each order, and the other library component contains a chart that demonstrates the total sales of each product. You also need to use some features that are specific to library components only, such as Message, Slider, and Configuration Panel.

This track contains the following tasks:

* [Task 1: Create Two Library Components](#Task1)
* [Task 2: Deliver a Message Between the Library Components](#Task2)
* [Task 3: Insert a Slider to Filter Data](#Task3)
* [Task 4: Use Text Field in the Configuration Panel to Change Property Value](#Task4)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/9905614395415/criticalicon.gif) To perform this track, you should have a JDashboard license for Designer. In the meantime, JDashboard is in maintenance mode, and we will not be adding new features to it. If you need more information, contact [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.).

## Task 1: Create Two Library Components

First, we create two library components, including a table and a chart.

1. Select **Logi Report Designer** in the **Logi Report** folder on the Start menu to open Designer.
2. Designer displays the main window and shows the Start Page by default. Close the Start Page.
3. Navigate to **File** > **Open Catalog**.
4. In the Open Catalog File dialog box, browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select **Open**.
5. Select **Yes** in the Warning dialog box. Designer displays the Catalog Manager. Close it because we do not use it in this lesson.
6. Navigate to **File** > **New** > **Library Component**. Designer displays the Select Component for Library Component dialog box.
7. Type **Product Order Details** in the **Library Component Title** text box, keep the default component type **Table (Group Above)**, then select **OK**.

   ![New Library Component](https://devnet.logianalytics.com/hc/article_attachments/9905901079703/lc_new.gif)
8. In the **Data** screen of the Table Wizard dialog box, select **WorldWideSalesBV** and select **Next**.
9. In the **Display** Screen, drag the following fields one by one to display in the table: **Order ID**, **Quantity**, **Unit Price**, and **Total**. Select **Next**.

   ![Add Table Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9905901115799/lc_tbldsply.gif)
10. In the **Group** screen, add **Product Name** as the group-by field.
11. Select **Style** on the screen navigation bar to switch to the screen and select **Commercial** from the style list. Select **Finish** to create the table.
12. Resize the group-by field to make sure all the product names can display completely.

    ![Table Component](https://devnet.logianalytics.com/hc/article_attachments/9905901144215/lc_tbl.gif)
13. Navigate to **File** > **Save** to save the library component as **ProductOrderDetails.lc**.

Next, we create the second library component that contains the chart.

1. Navigate to **File** >  **New** > **Library Component**.
2. In the Select Component for Library Component dialog box, type **Product Sales** as the library component title, select **Chart**from the component type box and select **OK**. Designer displays the Chart Wizard dialog box.
3. In the **Data** screen, select **WorldWideSalesBV**, then select **Next**.
4. Keep the default selections in the Type screen. Select **Next**.
5. In the **Display** Screen, add **Product Name** to the **X-Axis** box and **Total Sales** to the **Bar Length** box.

   ![Add Chart Display Fields](https://devnet.logianalytics.com/hc/article_attachments/9905901172375/lc_chtdsply.gif)
6. Select **Style** on the screen navigation bar to switch to the screen, then select **Classic** as the chart style.
7. Select **Finish** to create the chart.
8. Double-click any bar of the chart. Designer displays the Format Bar dialog box.
9. Switch to the **Fill** tab and select **Vary Colors by Color List** to fill each bar with a different color schema.

   ![Format Bar Fill Color](https://devnet.logianalytics.com/hc/article_attachments/9905901199255/lc_barcolor.gif)
10. Select **OK** to apply the setting and close the dialog box. The chart displays as follows in design view.

    ![Chart Component](https://devnet.logianalytics.com/hc/article_attachments/9905901215511/lc_cht.gif)
11. Navigate to **File** > **Save** to save the library component as **ProductSales.lc**.

## Task 2: Deliver a Message Between the Library Components

In order for end users to view sales information by order ID in the table, we want to deliver a built-in message 0002-Sort between the two library components. We use the chart to send the message, and the table to receive the message.

1. Double-click any bar in the chart. Designer displays the Format Bar dialog box.
2. Switch to the **Behaviors** tab, select **Select** from the drop-down list in the **Events** column, then select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9905879062551/btn_chsr.gif) in the **Actions** column.

   ![Add Web Behavior to Bar](https://devnet.logianalytics.com/hc/article_attachments/9905879086103/lc_barbhvr.gif)
3. In the Web Action List dialog box, select the **\*SendMessage** action and select **OK**.
4. In the Send Message - Web Action Builder dialog box, select the built-in message **0002 - Sort** from the **Message** drop-down list, then in the **Value** column, select **Descending** from the drop-down list for **Sort Order**.

   ![Send Message](https://devnet.logianalytics.com/hc/article_attachments/9905901328407/lc_sndmsg.gif)
5. Select **OK** to close the Send Message - Web Action Builder dialog box.
6. Select **OK** in the Format Bar dialog box to finish defining the message.
7. Navigate to **File** > **Save** to save the library component.

Next, we define to make the table receive the sort message that is sent out from the chart once end users perform the Select action on the chart bars in JDashboard.

1. Navigate to **Window** > **Switch Windows** > **ProductOrderDetails.lc** to switch to the table library component.
2. Select the table, right-click on it and select **Receive Message** from the shortcut menu.
3. In the Receive Message dialog box, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9905901353111/btn_add.gif) to add a message line, select the built-in message **0002 - Sort** from the drop-down list of the **Message ID** column, then select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/9905879062551/btn_chsr.gif) in the **Actions** column.

   ![Receive Message](https://devnet.logianalytics.com/hc/article_attachments/9905901384983/lc_rcvmsg.gif)
4. In the Sort dialog box, select **Order ID** from the **Sort On** column and **Descending** from the **Sort Value** column. Select **OK** to close the dialog box.

   ![Edit Sort](https://devnet.logianalytics.com/hc/article_attachments/9905879219095/lc_sort.gif)
5. Select **OK** in the Receive Message dialog box to finish defining the message.
6. Save the library component.

By now, we have finished defining the message between the chart and table, which applies like this: when end users select any bar on the chart in JDashboard, the chart sends out the built-in message 0002 - Sort to the table, and when the table receives the message, it sorts the order IDs descending.

## Task 3: Insert a Slider to Filter Data

To help end users easily get product sales information in a specific time period, we insert a slider to filter on the Order Date field for the table.

1. Navigate to **Insert** > **Web Controls** > **Filter Control**.
2. In the Insert Filter Control dialog box, select the **Range Slider** control type, from the **Select Fields** drop-down list, select **Order Date**, then select outside the drop-down list in the dialog box to finish selecting field. You can also select **Customize Initial Values** to customize the values you want to show on the slider. Here, we use all values in the Order Date field on the slider.

   ![Insert Filter Control](https://devnet.logianalytics.com/hc/article_attachments/9905879246871/lc_instsldr.gif)
3. Select **OK** to insert the slider.

   ![Table Library Component with Slider](https://devnet.logianalytics.com/hc/article_attachments/9905901485079/lc_sldr.gif)
4. Save the library component.

## Task 4: Use Text Field in the Configuration Panel to Change Property Value

In this task, we insert a text field into the configuration panel of the table library component, then we bind the Change Property web behavior to the text field, so that end users can use it to dynamically change the background color of the Quantity field at runtime.

1. Select **Display Configuration Panel** on the top-right corner to display the panel.
2. Navigate to **Insert** > **Web Controls** > **Text Field** to insert a text field in the configuration panel.
3. Right-click the text field and navigate to **Web Behaviors** > **Change Property** on the shortcut menu. Designer displays the Change Property - Web Behavior dialog box.
4. Select **Quantity** from the **Apply Action To** drop-down list, **Background** from the **Properties** drop-down list, and **TextField** from the **Value** drop-down list, then select **OK**.
   At runtime, users can type a hexadecimal RGB value in the text field to change the background color of the Quantity field in JDashboard.

   ![Chnage Property by Text Field](https://devnet.logianalytics.com/hc/article_attachments/9905879308823/lc_chgpty.gif)

Next, we add a label ahead of the text field to help end users identify what it is used for.

1. Navigate to **Insert** > **Label** to add a label ahead of the text field.
2. Double-click the label and edit its text to **Background Color of Quantity**, then resize the label to display the whole text in it completely.

   ![Configuration Panel](https://devnet.logianalytics.com/hc/article_attachments/9905879326103/lc_cnfgpnl.gif)
3. Save the library component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905613813911/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741406846103-Track-3-Creating-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905613870871/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741379857559-Track-5-Publishing-Running-and-Administering-Resources)
