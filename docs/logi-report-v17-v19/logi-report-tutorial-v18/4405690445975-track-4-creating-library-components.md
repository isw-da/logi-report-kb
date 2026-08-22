---
title: "Track 4: Creating Library Components"
id: 4405690445975
section: "Logi Report Tutorial v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690445975-Track-4-Creating-Library-Components
updated_at: 2022-05-10T09:58:55Z
---

# Track 4: Creating Library Components

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690448919-Track-3-Creating-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683486487-Track-5-Publishing-Running-and-Administering-Resources)

# Track 4: Creating Library Components

Library components are used by end users to [build dashboards](https://devnet.logianalytics.com/hc/en-us/articles/4405690459415-Track-1-Self-service-Dashboard-with-Logi-Report) using JDashboard which is a separately licensed product on Server. Library components are created and edited in Designer, and then published along with their catalog to the component library on Server for use in dashboards.

In this track, you have been asked to create two library components as a report developer, based on the business view WorldWideSalesBV created in the [previous track](https://devnet.logianalytics.com/hc/en-us/articles/4405683492759-Track-2-Creating-Business-Views). One library component should contain a table that shows each product's order details, including order ID, quantity, unit price, and the total sales for each order, and the other library component contains a chart that demonstrates the total sales of each product. You also need to use some features that are specific to library components only, such as Message, Slider, and Configuration Panel.

This track contains the following tasks:

* [Task 1: Create Two Library Components](#Task1)
* [Task 2: Deliver a Message Between the Library Components](#Task2)
* [Task 3: Insert a Slider to Filter Data](#Task3)
* [Task 4: Use Text Field in the Configuration Panel to Change Property Value](#Task4)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif) To perform this track, you should have a JDashboard license for Designer. If you need more information, contact [Customer Service](mailto:CustomerService@LogiAnalytics.com?subject=I%20have%20a%20product%20related%20question.).

## Task 1: Create Two Library Components

First, we create two library components, including a table and a chart.

1. Select **Logi Report Designer** in the **Logi Report** folder on the Start menu to open Designer.

   Designer displays the main window and shows the Start Page by default. Close the Start Page.
2. Navigate to **File** > **Open Catalog**.
3. In the Open Catalog File dialog box, browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select **Open**. Select **Yes** in the Warning dialog box.

   Designer displays the Catalog Manager. Close it because we do not use it in this lesson.
4. Navigate to **File** > **New** > **Library Component**. Designer displays the Select Component for Library Component dialog box.
5. Type **Product Order Details** in the **Library Component Title** text box, keep the default component type **Table (Group Above)**, then select **OK**.

   ![New Library Component](https://devnet.logianalytics.com/hc/article_attachments/4420453746199/lc_new.gif)

   Designer displays the Table Wizard dialog box.
6. In the **Data** screen, select **WorldWideSalesBV** and select **Next**.
7. In the **Display** Screen, drag the following fields one by one to display in the table: **Order ID**, **Quantity**, **Unit Price**, and **Total**. Select **Next**.

   ![Add Table Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4420447424407/lc_tbldsply.gif)
8. In the **Group** screen, add **Product Name** as the group-by field.
9. Select **Style** on the screen navigation bar to switch to the screen and select **Commercial** from the style list. Select **Finish** to create the table.
10. Resize the group-by field to make sure all the product names can be shown completely.

    ![Table Component](https://devnet.logianalytics.com/hc/article_attachments/4420453746583/lc_tbl.gif)
11. Navigate to **File** > **Save** to save the library component as **ProductOrderDetails.lc**.

Next, we create the second library component that contains the chart.

1. Navigate to **File** >  **New** > **Library Component**.
2. In the Select Component for Library Component dialog box, type **Product Sales** as the library component title, select **Chart**from the component type box and select **OK**. Designer displays the Chart Wizard dialog box.
3. In the **Data** screen, select **WorldWideSalesBV**, then select **Next**.
4. Keep the default selections in the Type screen. Select **Next**.
5. In the **Display** Screen, add **Product Name** to the **X-Axis** box and **Total Sales** to the **Bar Length** box.

   ![Add Chart Display Fields](https://devnet.logianalytics.com/hc/article_attachments/4420461808279/lc_chtdsply.gif)
6. Select **Style** on the screen navigation bar to switch to the screen, then select **Classic** as the chart style.
7. Select **Finish** to create the chart.
8. Double-click any bar of the chart. Designer displays the Format Bar dialog box.
9. Switch to the **Fill** tab and select **Vary Colors by Color List** to fill each bar with a different color schema.

   ![Format Bar Fill Color](https://devnet.logianalytics.com/hc/article_attachments/4420453747223/lc_barcolor.gif)
10. Select **OK** to apply the setting and close the dialog box.

    The chart displays as follows in design mode:

    ![Chart Component](https://devnet.logianalytics.com/hc/article_attachments/4420447424663/lc_cht.gif)
11. Navigate to **File** > **Save** to save the library component as **ProductSales.lc**.

## Task 2: Deliver a Message Between the Library Components

In order for end users to view sales information by order ID in the table, we want to deliver a built-in message 0002-Sort between the two library components. We use the chart to send the message, and the table to receive the message.

1. Double-click any bar in the chart. Designer displays the Format Bar dialog box.
2. Switch to the **Behaviors** tab, select **Select** from the drop-down list in the **Events** column, then select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420447424919/btn_chsr.gif) in the **Actions** column.

   ![Add Web Behavior to Bar](https://devnet.logianalytics.com/hc/article_attachments/4420453747479/lc_barbhvr.gif)
3. In the Web Action List dialog box, select the **\*SendMessage** action and select **OK**.
4. In the Send Message - Web Action Builder dialog box, select the built-in message **0002 - Sort** from the **Message** drop-down list, then in the **Value** column, select **Descending** from the drop-down list for **Sort Order**.

   ![Send Message](https://devnet.logianalytics.com/hc/article_attachments/4420447425175/lc_sndmsg.gif)
5. Select **OK** to close the Send Message - Web Action Builder dialog box.
6. Select **OK** in the Format Bar dialog box to finish defining the message.
7. Navigate to **File** > **Save** to save the library component.

Next, we define to make the table receive the sort message that is sent out from the chart once end users perform the Select action on the chart bars in JDashboard.

1. Navigate to **Window** > **Switch Windows** > **ProductOrderDetails.lc** to switch to the table library component.
2. Select the table, right-click on it and select **Receive Message** from the shortcut menu.
3. In the Receive Message dialog box, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420447425431/btn_add.gif) to add a message line, select the built-in message **0002 - Sort** from the drop-down list of the **Message ID** column, then select the **ellipsis**![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420447424919/btn_chsr.gif) in the **Actions** column.

   ![Receive Message](https://devnet.logianalytics.com/hc/article_attachments/4420447425687/lc_rcvmsg.gif)
4. In the Sort dialog box, select **Order ID** from the **Sort On** column and **Descending** from the **Sort Value** column. Select **OK** to close the dialog box.

   ![Edit Sort](https://devnet.logianalytics.com/hc/article_attachments/4420453747735/lc_sort.gif)
5. Select **OK** in the Receive Message dialog box to finish defining the message.
6. Save the library component.

By now, we have finished defining the message between the chart and table, which applies like this: when end users select any bar on the chart in JDashboard, the chart sends out the built-in message 0002 - Sort to the table, and when the table receives the message, it sorts the order IDs descending.

## Task 3: Insert a Slider to Filter Data

To help end users easily get product sales information in a specific time period, we insert a slider to filter on the Order Date field for the table.

1. Navigate to **Insert** > **Web Controls** > **Filter Control**.
2. In the Insert Filter Control dialog box, select the **Range Slider** control type, from the **Select Fields** drop-down list, select **Order Date**, then select outside of the drop-down list in the dialog box to finish selecting field.

   ![Insert Filter Control](https://devnet.logianalytics.com/hc/article_attachments/4420453747991/lc_instsldr.gif)

   You can also select Customize Initial Values to customize the values you want to show on the slider. Here, we use all the values in the Quantity field on the slider.
3. Select **OK** to insert the slider.

   ![Table Library Component with Slider](https://devnet.logianalytics.com/hc/article_attachments/4420453748247/lc_sldr.gif)
4. Save the library component.

## Task 4: Use Text Field in the Configuration Panel to Change Property Value

In this task, we insert a text field into the configuration panel of the table library component, then we bind the Change Property web behavior to the text field, so that end users can use it to dynamically change the background color of the Quantity field at runtime.

1. Select **Display Configuration Panel** on the top-right corner to display the panel.
2. Navigate to **Insert** > **Web Controls** > **Text Field** to insert a text field in the configuration panel.
3. Right-click the text field and navigate to **Web Behaviors** > **Change Property** on the shortcut menu. Designer displays the Change Property - Web Behavior dialog box.
4. Select **Quantity** from the **Apply Action To** drop-down list, **Background**  from the **Properties** drop-down list, and **TextField** from the **Value** drop-down list, then select **OK**.

   ![Chnage Property by Text Field](https://devnet.logianalytics.com/hc/article_attachments/4420453748503/lc_chgpty.gif)

   Users can type a hexadecimal RGB value in the text field to change the background color of the Quantity field in JDashboard.

Next, we add a label ahead of the text field to help end users identify what it is used for.

1. Navigate to **Insert** > **Label** to add a label ahead of the text field.
2. Double-click the label and edit its text to **Background Color of Quantity**, then resize the label to display the whole text in it completely.

   ![Configuration Panel](https://devnet.logianalytics.com/hc/article_attachments/4420453748759/lc_cnfgpnl.gif)
3. Save the library component.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690448919-Track-3-Creating-Web-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683486487-Track-5-Publishing-Running-and-Administering-Resources)
