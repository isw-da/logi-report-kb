---
title: "Example of Using Business View Security"
id: 1500009571162
section: "Defining Report Security - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009571162-Example-of-Using-Business-View-Security
updated_at: 2021-07-24T05:53:44Z
---

# Example of Using Business View Security

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568002-Printing-and-Exporting-Reports)

# Example of Using Business View Security

This example is based on the business view WorldWideSalesBV in the SampleReports.cat catalog file. It is assumed that the server administrator has already created two users on Logi JReport Server: User1 and User2, with the passwords abc and xyz respectively. We will create a security policy on SampleReports.cat to limit the two users' access to different group members of WorldWideSalesBV. Before starting the example, make sure Logi JReport Server is started.

This topic contains the following tasks:

> * [Task 1: Set Security on Business View Groups](#Task2)
> * [Task 2: Create a Crosstab and Publish it to Logi JReport Server](#Task3)
> * [Task 3: View the Crosstab](#Task3)

## Task 1: Set Security on Business View Groups

In this task, we will import the two server users to Logi JReport Designer and limit their access to different members of the Region group in WorldWideSalesBV.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `C:\Logi JReport\Designer\Demo\Reports\SampleReports`.
2. In the Catalog Manager, go to the **Data Source 1** > **Security** > **Business View Security** node, right-click and select **Edit Business View Security**.
3. In the Edit Business View Security dialog, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) and select **Import from Logi JReport Server**.
4. In the Connect to Logi JReport Server dialog, specify the required connection information, then select **Connect**.

   The principals created on the server will all be imported and listed in the Users/Groups/Roles box.

   ![Import Users](https://devnet.logianalytics.com/hc/article_attachments/4404889276823/scrty_bv_eg_addusr.gif)

Next, we will assign field members availability to User1 and User2. We will make User1 have access on the North America region only and User2 regions other than North America.

1. Select **User1**, in the Resources box select **Region** in WorldWideSalesBV.
2. In the Security Options box, uncheck **Use Default**.
3. In the Data Security box, allow the Access permission.
4. Select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif) above the Allowed Set box.
5. In the Edit Values dialog, select **North America** from the Available Values box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif) to add it to the Selected Values box, then select **OK** to close the dialog.

   ![Add Value for User1](https://devnet.logianalytics.com/hc/article_attachments/4404889277079/scrty_bv_eg_vlu.gif)
6. In the Edit Business View Security dialog, uncheck the option **Allow Unspecified Members**, then in the Resource Security box, allow the Visible permission.

   ![Permission of Users](https://devnet.logianalytics.com/hc/article_attachments/4404893792279/scrty_bv_eg_user1.gif)
7. Select **User2** and the same field **Region** in WorldWideSalesBV, then uncheck **Use Default** in the Security Options box.
8. In the Data Security box, allow the Access permission, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404893791511/btn_edit.gif) above the Denied Set box.
9. In the Edit Values dialog, select **North America** from the Available Values box and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif), then select **OK**.
10. In the Resource Security box, allow the Visible permission for User2.

    ![Permission of User2](https://devnet.logianalytics.com/hc/article_attachments/4404893792535/scrty_bv_eg_user2.gif)
11. Select **OK** in the Edit Business View Security dialog to save the changes.
12. Close the Catalog Manger.

## Task 2: Create a Crosstab and Publish it to Logi JReport Server

In this task, we will create a crosstab using WorldWideSalesBV and then publish it to Logi JReport Server.

1. In Logi JReport Designer, select **File** > **New** > **Web Report**. A blank web report is created.
2. Select **Insert** > **Crosstab**. The Create Crosstab wizard is displayed.
3. In the Data screen, select **WorldWideSalesBV** under Data Source 1, then select **Next**.
4. In the Display screen, select **Region** as the column field, **Category** as the Row field, and **Total Sales** as the summary field. Select **Finish** to create the crosstab.

   ![Create Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404889277335/scrty_bv_eg_crtcrstb.gif)
5. Select the **View** tab to preview the crosstab. It shows full data.

   ![Preview Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4404889277591/scrty_bv_eg_viewcrstb.gif)
6. Go back to the Design tab and select **File** > **Save** to save the crosstab as **mlscrstab.wls**.

Next, we will publish the crosstab to Logi JReport Server.

1. Select **File** > **Publish** > **Publish Report to Server** on Logi JReport Designer menu bar.
2. In the Connect to Logi JReport Server dialog, specify the required connection information, then select **Connect**.
3. In the Publish to Logi JReport Server dialog, unselect the **All** checkbox and then select the **SampleReports.cat** and **mlscrstab.wls** only.
4. Select the **Browse** button next to the Publish Resource To text field, then in the Select Folder dialog, select **Public Reports**  in the Folder box and select **OK**.
5. In the Publish to Logi JReport Server dialog, select the **More Options** button, select **mlscrstab.wls** in the resource box, then on the right panel, switch to the **Permissions** tab.

We will grant the two users the necessary permissions on the web report, so that after the report is published to Logi JReport Server, they are able to run them.

1. Select the **Enable Setting Permissions** checkbox, select the **User** sub tab, select **User1** in the user box and check the **Visible** and **Execute** checkboxes; select **User2** and do the same.

   ![Publish Resource to Server](https://devnet.logianalytics.com/hc/article_attachments/4404893792791/scrty_bv_eg_pblsh.gif)
2. Select the **OK** button to publish the resources to Logi JReport Server.

## Task 3: View the Crosstab

Now, we can log onto Logi JReport Server as User1 and User2 separately to view the crosstab.

1. Log onto the Logi JReport Server user console as User1 with the password abc.
2. Open the Public Reports folder and run the web report mlscrstab.wls. The result will be:

   ![User1 Crosstab Result](https://devnet.logianalytics.com/hc/article_attachments/4404893793047/scrty_bv_eg_rst1.gif)
3. Log out and then log in again as User2 with the password xyz. Run the report and the result will be:

   ![User2 Crosstab Result](https://devnet.logianalytics.com/hc/article_attachments/4404893793303/scrty_bv_eg_rst2.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009593141-Configuring-Business-View-Security)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568002-Printing-and-Exporting-Reports)
