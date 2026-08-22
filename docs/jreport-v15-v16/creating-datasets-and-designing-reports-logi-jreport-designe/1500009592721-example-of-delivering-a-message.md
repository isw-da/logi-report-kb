---
title: "Example of Delivering a Message"
id: 1500009592721
section: "Creating Datasets and Designing Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009592721-Example-of-Delivering-a-Message
updated_at: 2021-07-24T05:53:51Z
---

# Example of Delivering a Message

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592741-Receiving-Messages)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592781-Previewing-a-Library-Component)

# Example of Delivering a Message

This example demonstrates how to deliver a filter user defined message between two library components in order to synchronize the data components in them. It contains the following tasks:

> * [Task 1: Create Two Library Components](#Task1)
> * [Task 2: Send out a Filter User Defined Message from the Chart](#Task2)
> * [Task 3: Make the Two Data Components Receive the Same Message](#Task3)
> * [Task 4: Publish the Library Components to Logi JReport Server](#Task4)
> * [Task 5: Deliver the Message in a Dashboard for Data Synchronization](#Task5)

## Task 1: Create Two Library Components

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. Use the business view SaleStat in Data Source 1 to [create two library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009592701-Creating-a-Library-Component) and save them as Component 1.lc and Component 2.lc.

   For Component 1, create a chart which displays in the clustered bar 2-D chart type, shows Assigned Region on X-Axis and Total Actual as Bar Length. For Component 2, create a crosstab using Order ID and Assigned Region respectively as the row and column fields, and Total Actual as the summary field. Apply the style Commercial to both of them.

## Task 2: Send out a Filter User Defined Message from the Chart

In this task, we will send a filter user defined message from the chart in Component 1 when the Select event occurs on any legend entry value.

1. Open Component 1.lc.
2. Right-click the chart legend and select **Send Message** > **Customize**  on the shortcut menu to bring out the Send Message dialog.
3. In the Events box, check **Select** as the trigger event, then select on the event to activate the message options on the right.
4. From the Message drop-down list, select **User Defined**, then input **1001** and **Filter - Assigned Region** as the message ID and name.
5. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a message line.
6. Select the **<Input>** item from the drop-down list in the Key column and input **Assigned Region** in the text box.
7. Select **Current Value** from the drop-down list in the Value column. String is displayed automatically in the Data Type column.

   The message is defined as follows:

   ![Send Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893813655/rpt_lc_msg_eg_send.gif)
8. Select **OK** to finish defining the message to be sent out.
9. Save the library component.

## Task 3: Make the Two Data Components Receive the Same Message

In this task we will make the chart and crosstab in the two library components receive the same filter message to filter on the Assigned Region values when they receive the message sent out from a chart legend entry.

1. Right-click the chart platform and select **Receive Message** from the shortcut menu to display the Receive Message dialog.
2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a message line.
3. Select the **<Input>** item from the drop-down list in the Message ID column, then input **1001** in the text box.
4. Input **Filter - Assigned Region** in the text box of the Message Name column.
5. Select the blank text box in the Actions column, then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) that appears.

   ![Receive Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893813911/rpt_lc_msg_eg_recv1.gif)
6. In the Web Action List dialog, select **\*Filter** and select **OK** to display the Filter dialog.
7. Select **Assigned Region** from the Filter On drop-down list, keep the default operator, then select **<Input>** under the Message Key node in the Value drop-down list and input **Assigned Region** in the text box.

   ![Filter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893814167/rpt_lc_msg_eg_recv2.gif)
8. Select **OK** to go back to the Receive Message dialog. The message Component 1 receives is defined as follows:

   ![Receive Message dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893814551/rpt_lc_msg_eg_recv3.gif)
9. Select **OK**, then save the library component.
10. Open Component 2.lc.
11. Right-click the crosstab and select **Receive Message** from the shortcut menu.
12. In the Receive Message dialog, specify the message the crosstab is going to receive [as shown above](#Chart).
13. Upon finishing defining the received message, save the library component.

## Task 4: Publish the Library Components

Start Logi JReport Server and publish the library components along with the catalog SampleReports.cat to the component library in Logi JReport Server. For details about publishing resources from Logi JReport Designer to Logi JReport Server, see [Publishing Resources Remotely](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Remotely).

## Task 5: Deliver the Message in a Dashboard for Data Synchronization

1. Open the Logi JReport Console > Resources page, select **New** > **Dashboard** on the task bar. A blank dashboard is displayed in JDashboard.
2. Open the Resources panel and browse to the folder where the two library components are published.
3. Drag and drop the two library components to the dashboard.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889292311/rpt_lc_msg_eg_msg1.gif)
4. Select **Asia-Pacific** in the chart legend to send out the message. The chart and the crosstab are both filtered to show data in the Asia-Pacific region only.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889292567/rpt_lc_msg_eg_msg2.gif)
5. Select the **Clear Filters** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404893814807/rpt_lc_msg_eg_clrfltr.gif) on the toolbar to clear the filter in both components.
6. Select **Europe, Middle East, Africa** in the chart legend and the chart and crosstab are filtered based on this region now.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889292823/rpt_lc_msg_eg_msg3.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009592741-Receiving-Messages)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009592781-Previewing-a-Library-Component)
