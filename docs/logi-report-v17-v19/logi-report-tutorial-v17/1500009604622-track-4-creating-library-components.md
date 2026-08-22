---
title: "Track 4: Creating Library Components"
id: 1500009604622
section: "Logi Report Tutorial v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009604622-Track-4-Creating-Library-Components
updated_at: 2021-07-24T16:05:35Z
---

# Track 4: Creating Library Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009604762-Track-3-Creating-Web-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604502-Track-5-Publishing-Running-and-Administering-Resources)

# Track 4: Creating Library Components

Library components are used by end users to [build dashboards](https://devnet.logianalytics.com/hc/en-us/articles/1500009628121-Track-1-Self-service-Dashboard-with-Logi-Report) using JDashboard which is a separately licensed product in Logi Report Server. Library components are created and edited in Logi Report Designer, and then published along with their catalog to the component library in Logi Report Server for use in dashboards.

In this track, you will create two library components in Logi Report Designer as the role of a report developer, based on the business view WorldWideSalesBV created in the [previous track](https://devnet.logianalytics.com/hc/en-us/articles/1500009604602-Track-2-Creating-Business-Views). One library component contains a table that shows each product's order details, including order ID, quantity, unit price, and the total sales for each order. Another library component contains a chart that demonstrates the total sales of each product. We will apply some features that are specific to library components only, such as Message, Slider, and Configuration Panel.

**Note:** A JDashboard license for Logi Report Designer is required in order to perform this track. If you do not have the license, please contact your Logi Analytics account manager to obtain it first.

This track contains the following tasks:

* [Task 1: Create Two Library Components](#Task1)
* [Task 2: Deliver a Message Between the Library Components](#Task2)
* [Task 3: Insert a Slider to Filter Data](#Task3)
* [Task 4: Use Text Field in the Configuration Panel to Change Property Value](#Task4)

## Task 1: Create Two Library Components

First, we will create two library components, including a table and a chart.

1. Select **Logi Report Designer** in the Logi Report folder on the Start menu to start Logi Report Designer.

   The Logi Report Designer window appears, with the Start Page shown by default. Close the Start Page.
2. Select **File** > **Open Catalog**.
3. In the Open Catalog File dialog box, browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select the **Open** button.

   The Catalog Manager is displayed. Close it since we will not use it in the lesson.
4. Select **File** > **New** > **Library Component**. The Select Component for Library Component dialog box appears.
5. Type **Product Order Details** in the Library Component Title text field, keep the default selected component type **Table (Group Above)**, then select **OK**.

   ![New Library Component](https://devnet.logianalytics.com/hc/article_attachments/4404904580375/lc_new.gif)

   The Table Wizard appears.
6. In the Data screen of the Table Wizard, select **WorldWideSalesBV** and select **Next**.
7. In the Display Screen, drag the following fields to be displayed in the table: **Order ID**, **Quantity**, **Unit Price**, and **Total** one by one. Select **Next**.

   ![Add Table Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4404904580631/lc_tbldsply.gif)
8. In the Group screen, add **Product Name** as the group-by field.
9. Select **Style** to switch to the screen and select **Commercial** from the style list. Select **Finish** to create the table.
10. Resize the group-by field to make sure all the product names can be shown completely. The table displays as follows:

    ![Table Component](https://devnet.logianalytics.com/hc/article_attachments/4404916879511/lc_tbl.gif)
11. Select **File** > **Save** to save the library component as **ProductOrderDetails.lc**.

Next, we will create the second library component that contains the chart.

1. Select **File** >  **New** > **Library Component**.
2. In the Select Component for Library Component dialog box, type **Product Sales** in the Library Component Title text field, select **Chart** as the component type and select **OK**. The Chart Wizard is displayed.
3. In the Data screen of the wizard, select **WorldWideSalesBV**, then select **Next**.
4. Keep the default selections in the Type screen. Select **Next**.
5. In the Display Screen, add **Product Name** to the X-Axis box and **Total Sales** to the Bar Length box.

   ![Add Chart Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4404904580887/lc_chtdsply.gif)
6. Select **Style** to switch to the creen, select **Classic** as the chart style. Then select **Finish**.
7. Double-click any bar of the chart. In the Format Bar dialog box, switch to the **Fill** tab and select **Vary Colors by Color List** to make each bar filled with a different color schema.

   ![Format Bar Fill Color](https://devnet.logianalytics.com/hc/article_attachments/4404916879767/lc_barcolor.gif)
8. Select **OK** to apply the setting and close the dialog box. The chart displays as follows:

   ![Chart Component](https://devnet.logianalytics.com/hc/article_attachments/4404904581399/lc_cht.gif)
9. Select **File** > **Save** to save the library component as **ProductSales.lc**.

## Task 2: Deliver a Message Between the Library Components

In order for end users to view sales information by order ID in the table, we will define to deliver a built-in message 0002-Sort between the two library components. We will use the chart to send the message, and the table to receive the message.

1. Double-click any bar in the chart. The Format Bar dialog box appears.
2. Switch to the **Behaviors** tab, select **Select** from the drop-down list in the Events column, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404916880023/btn_chsr.gif) in the Actions column.

   ![Add Web Behavior to Bar](https://devnet.logianalytics.com/hc/article_attachments/4404916880535/lc_barbhvr.gif)
3. In the Web Action List dialog box, select the **\*SendMessage** action and select **OK**.
4. In the Send Message - Web Action Builder dialog box, select the built-in message **0002 - Sort** from the drop-down list, then in the Value column, select **Descending** from the drop-down list for Sort Order.

   ![Send Message](https://devnet.logianalytics.com/hc/article_attachments/4404904581655/lc_sndmsg.gif)
5. Select **OK** to close the Send Message - Web Action Builder dialog box.
6. Select **OK** in the Format Bar dialog box to finish defining the message.
7. Select **File** > **Save** to save the library component.

Next, we will define to make the table receive the sort message that will be sent out from the chart once the select action is triggered on the chart bars.

1. Select **Window** > **Switch Windows** > **ProductOrderDetails.lc** to switch to the table library component.
2. Select the table, right-click on it and select **Receive Message** from the shortcut menu.
3. In the Receive Message dialog box, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904581911/btn_add.gif) to add a message line, select the built-in message **0002 - Sort** from the drop-down list of the Message ID column, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404916880023/btn_chsr.gif) in the Actions column.

   ![Receive Message](https://devnet.logianalytics.com/hc/article_attachments/4404916880791/lc_rcvmsg.gif)
4. In the Sort dialog box, select **Order ID** from the Sort On column and **Descending** from the Sort Value column. Select **OK** to close the dialog box.

   ![Edit Sort](https://devnet.logianalytics.com/hc/article_attachments/4404904582167/lc_sort.gif)
5. Select **OK** in the Receive Message dialog box to finish defining the message.
6. Select **File** > **Save** to save the library component.

By now, the message between the chart and table is created and it is defined as follows: when any bar on the chart is selected at runtime, the built-in message 0002 - Sort will be sent out from the chart to the table, and when the table receives the message, it will make the order IDs sort descending as a response to the message.

## Task 3: Insert a Slider to Filter Data

To help end users easily get product sales information in a specific time period, we will insert a slider to filter on the Order Date field for the table.

1. Select **Insert** > **Web Controls** > **Filter Control**.
2. In the Insert Filter Control dialog box, select **Range Slider** as the control type, from the Select Fields drop-down list select **Order Date**, then select outside of the field drop-down list in the dialog box to finish selecting field.

   ![Insert Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4404904582423/lc_instsldr.gif)

   You can also select Customize Initial Values to customize the values you want to show on the slider. Here, we will use all the values in the Quantity field on the slider.
3. Select **OK** to insert the slider. The slider displays as follows in the library component:

   ![Table Library Component with Slider](https://devnet.logianalytics.com/hc/article_attachments/4404904582679/lc_sldr.gif)
4. Select **File** > **Save** to save the library component.

## Task 4: Use Text Field in the Configuration Panel to Change Property Value

In this task, we will insert a text field into the configuration panel of the table library component and bind the Change Property web behavior to it so that end users can use the text field to dynamically change the background color of the Quantity field at runtime.

1. Select the **Display Configuration Panel** checkbox on the top-right corner to display the panel.
2. Select **Insert** > **Web Controls** > **Text Field** to insert it in the configuration panel.
3. Right-click the text field and select **Web Behaviors** > **Change Property** from the shortcut menu. The Change Property - Web Behavior dialog box appears.
4. Select **Quantity** from the Apply Action To drop-down list, **Background**  from the Properties drop-down list, and **TextField** from the Value drop-down list, then select **OK**.

   ![Chnage Property by Text Field](https://devnet.logianalytics.com/hc/article_attachments/4404904582935/lc_chgpty.gif)

   Then at runtime, end users can type a hexadecimal RGB value in the text field to change the background color of the Quantity field in JDashboard.

Next we will add a label ahead of the text field to help end users identify what it is used for.

1. Select **Insert** > **Label** to add a label ahead of the text field.
2. Double-click the label and edit its text to **Background Color of Quantity**. Resize the label to make the whole text in it shown.

   The label and text field display as follows in the configuration panel:

   ![Configuration Panel](https://devnet.logianalytics.com/hc/article_attachments/4404916881559/lc_cnfgpnl.gif)
3. Select **File** > **Save** to save the library component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009604762-Track-3-Creating-Web-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604502-Track-5-Publishing-Running-and-Administering-Resources)
