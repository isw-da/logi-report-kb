---
title: "Example of Using Business View Security"
id: 4405661338135
section: "Defining Report Security - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661338135-Example-of-Using-Business-View-Security
updated_at: 2022-01-27T20:34:20Z
---

# Example of Using Business View Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664363415-Configuring-Business-View-Security-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661752215-Printing-and-Exporting-Reports)

# Example of Using Business View Security

This topic provides an example to illustrate how you can set security for a business view in a catalog in Designer and run a report that uses the business view with different users to apply the security on Server.

This example uses the business view WorldWideSalesBV in the SampleReports.cat catalog file. It is assumed that the Server administrator has already created two users on Server: User1 and User2, with the passwords "abc" and "xyz" respectively. We create a security policy on SampleReports.cat to limit the two users' access to different group members of WorldWideSalesBV. Before starting the example, make sure you already launch Server.

The example contains the following tasks:

* [Task 1: Set security on business view groups](#Task1)
* [Task 2: Create a crosstab and publish it to Server](#Task2)
* [Task 3: View the crosstab](#Task3)

**Task 1: Set security on business view groups**

In this task, we import the two Server users to Designer and limit their access to different members of the Region group in WorldWideSalesBV.

1. Make sure **SampleReports.cat** is the currently open catalog file. If not, navigate to **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, navigate to the **Data Source 1** > **Security** > **Business View Security** node, right-click and select **Edit Business View Security** from the shortcut menu.
3. In the Edit Business View Security dialog box, select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420394650391/btn_add.gif) and select **Import from Logi Report Server**.
4. In the Connect to Logi Report Server dialog box, specify the required connection information and select **Connect**.

   Designer imports the principals created on Server and lists them in the **Users/Groups/Roles** panel.

   ![Import Users](https://devnet.logianalytics.com/hc/article_attachments/4420402614423/scrty_bv_eg_addusr.gif)

Next, we assign field members' availability to User1 and User2. We give User1 access to the North America region only, and grant User2 access to regions other than North America.

1. Select **User1**, then in the **Resources** box, select **Region** in **WorldWideSalesBV**.
2. In the **Security Options** box, clear **Use Default**.
3. In the **Data Security** box, allow the **Access** permission.
4. Select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420394656407/btn_edit.gif) above the **Allowed Set** box.
5. In the Edit Values dialog box, select **North America** from the **Available Values** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif) to add it to the **Selected Values** box, then select **OK** to close the dialog box.

   ![Add Value for User1](https://devnet.logianalytics.com/hc/article_attachments/4420394939415/scrty_bv_eg_vlu.gif)
6. In the Edit Business View Security dialog box, clear **Allow Unspecified Members**, then in the **Resource Security** box, allow the Visible permission.

   ![Permission of Users](https://devnet.logianalytics.com/hc/article_attachments/4420394939799/scrty_bv_eg_user1.gif)
7. Select **User2** and the same field **Region** in **WorldWideSalesBV**, then clear **Use Default** in the **Security Options** box.
8. In the **Data Security** box, allow the **Access** permission, then select **Edit**![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4420394656407/btn_edit.gif) above the **Denied Set** box.
9. In the Edit Values dialog box, select **North America** from the **Available Values** box and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/4420410583703/btn_addarrow.gif). Select **OK** to close the dialog box.
10. In the **Resource Security** box of the Edit Business View Security dialog box, allow the Visible permission for User2.

    ![Permission of User2](https://devnet.logianalytics.com/hc/article_attachments/4420402614935/scrty_bv_eg_user2.gif)
11. Select **OK** in the Edit Business View Security dialog box to save the changes.
12. Close the Catalog Manger.

**Task 2: Create a crosstab and publish it to Server**

In this task, we create a crosstab using WorldWideSalesBV in the SampleReports catalog and then publish it to Server.

1. Navigate to **File** > **New** > **Web Report**. Designer creates a blank web report.
2. Navigate to **Insert** > **Crosstab**. Designer displays the Create Crosstab dialog box.
3. In the **Data** screen, select **WorldWideSalesBV** under Data Source 1, then select **Next**.
4. In the **Display** screen, select **Region** as the column field, **Category** as the row field, and **Total Sales** as the summary field. Select **Finish** to create the crosstab.

   ![Create Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4420402615319/scrty_bv_eg_crtcrstb.gif)
5. Select the **View** tab to preview the crosstab. It shows full data.

   ![Preview Crosstab](https://devnet.logianalytics.com/hc/article_attachments/4420402615575/scrty_bv_eg_viewcrstb.gif)
6. Select the **Design** tab to go back to design mode.
7. Save the crosstab as **mlscrstab.wls**.

Next, we publish the crosstab to Server.

1. Navigate to **File** > **Publish** > **Publish Report to Server**.
2. In the Connect to Logi Report Server dialog box, specify the required connection information and select **Connect**.
3. In the Publish to Logi Report Server dialog box, clear **All**, then select **SampleReports.cat** and **mlscrstab.wls** only.
4. Select **Browse** next to the **Publish Resource To** text box, then in the Select Folder dialog box, select **Public Reports** in the **Folder** box and select **OK**.
5. In the Publish to Logi Report Server dialog box, select **More Options**, select **mlscrstab.wls** in the resource box, then in the right panel, switch to the **Permissions** tab.

We need to grant the two users the necessary permissions on the web report, so that after we publish the report to Server, they are able to run them.

1. Select **Enable Setting Permissions**, select the **User** subtab, select **User1** in the user box and select **Visible** and **Execute**; select **User2** and do the same.

   ![Publish Resource to Server](https://devnet.logianalytics.com/hc/article_attachments/4420410941335/scrty_bv_eg_pblsh.gif)
2. Select **OK** to publish the resources to Server.

**Task 3: View the crosstab**

Now, we can sign in to Server as User1 and User2 respectively to view the crosstab.

1. Sign in to the Server Console using the user name "User1" and password "abc".
2. Open the **Public Reports** folder and run the web report **mlscrstab.wls**.

   ![User1 Crosstab Result](https://devnet.logianalytics.com/hc/article_attachments/4420402615959/scrty_bv_eg_rst1.gif)
3. Sign out and then sign in again as "User2" with the password "xyz".
4. Run the report.

   ![User2 Crosstab Result](https://devnet.logianalytics.com/hc/article_attachments/4420394941079/scrty_bv_eg_rst2.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664363415-Configuring-Business-View-Security-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661752215-Printing-and-Exporting-Reports)
