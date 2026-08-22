---
title: "Example: Applying Business View Security"
id: 28897749366413
section: "Defining Report Security - Report Designer v24"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28897749366413-Example-Applying-Business-View-Security
updated_at: 2024-09-30T09:12:11Z
source_host: docs-report.zendesk.com
---
Previous Topic  Next Topic

# 
Example: Applying Business View Security

This topic provides an example to illustrate how you can set security for a business view in a catalog in Designer and run a report that uses the business view with different users to apply the security on Server.

This example uses the business view WorldWideSalesBV in the SampleReports.cat catalog file. It is assumed that the Server administrator has already created two users on Server: User1 and User2, with the passwords "abc" and "xyz" respectively. We create a security policy on SampleReports.cat to limit the two users' access to different group members of WorldWideSalesBV. Before starting the example, make sure you already launch Server.

The example contains the following tasks:

- Task 1: Set security on business view groups

- Task 2: Create a crosstab and publish it to Server

- Task 3: View the crosstab

Task 1: Set security on business view groups

In this task, we import the two Server users to Designer and limit their access to different members of the Region group in WorldWideSalesBV.

- Make sure SampleReports.cat is the currently open catalog file. If not, navigate to File > Open Catalog to open it from <install_root>\Demo\Reports\SampleReports.

- In the Catalog Manager, navigate to the Data Source 1 > Security > Business View Security node, right-click and select Edit Business View Security from the shortcut menu.

- In the Edit Business View Security dialog box, select Add and select Import from  Report Server.

- In the Connect to Report Server dialog box, specify the connection information and select Connect.

- Designer imports the principals created on Server and lists them in the Users/Groups/Roles panel.
    

Next, we assign field members' availability to User1 and User2. We give User1 access to the North America region only, and grant User2 access to regions other than North America.

- Select User1, then in the Resources box, select Region in WorldWideSalesBV.

- In the Security Options box, clear Use Default.

- In the Data Security box, allow the Access permission.

- Select Edit above the Allowed Set box.

- In the Edit Values dialog box, select North America from the Available Values box and select Add to add it to the Selected Values box, then select OK to close the dialog box.    

- In the Edit Business View Security dialog box, clear Allow Unspecified Members, then in the Resource Security box, allow the Visible permission.
    

- Select User2 and the same field Region in WorldWideSalesBV, then clear Use Default in the Security Options box.

- In the Data Security box, allow the Access permission, then select Edit above the Denied Set box.

- In the Edit Values dialog box, select North America from the Available Values box and select Add. Select OK to close the dialog box.

- In the Resource Security box of the Edit Business View Security dialog box, allow the Visible permission for User2.
    

- Select OK in the Edit Business View Security dialog box to save the changes.

- Close the Catalog Manger. 

Task 2: Create a crosstab and publish it to Server

In this task, we create a crosstab using WorldWideSalesBV in the SampleReports catalog  and then publish it to Server.

- Navigate to File > New > Web Report. Designer creates a blank web report.

- Navigate to Insert > Crosstab. Designer displays the Create Crosstab dialog box.

- In the Data screen, select WorldWideSalesBV under Data Source 1, then select Next.

- In the Display screen, select Region as the column field, Category as the row field, and Total Sales as the summary field. Select Finish to create the crosstab.
    

- Select the View tab to preview the crosstab. It shows full data.
    

- Select the Design tab to go back to design mode.

- Save the crosstab as mlscrstab.wls.

Next, we publish the crosstab to Server.

- Navigate to File > Publish > Publish Report to Server. 

- In the Connect to Report Server dialog box, specify the required connection information and select Connect. 

- In the Publish to Report Server dialog box, clear All, then select SampleReports.cat and mlscrstab.wls only.

- Select Browse next to the Publish Resource To text box, then in the Select Folder dialog box, select Public Reports in the Folder box and select OK.

- In the Publish to Report Server dialog box, select More Options, select mlscrstab.wls in the resource box, then in the right panel, switch to the Permissions tab.

We need to grant the two users the necessary permissions on the web report, so that after we publish the report to Server, they are able to run them. 

- Select Enable Setting Permissions, select the User subtab, select User1 in the user box and select Visible and Execute; select User2 and do the same.
    

- Select OK to publish the resources to Server.

Task 3: View the crosstab

Now, we can sign in to Server as User1 and User2 respectively to view the crosstab.

- Sign in to the Server Console using the user name "User1" and password "abc".

- Open the Public Reports folder and run the web report mlscrstab.wls.

- Sign out and then sign in again as "User2" with the password "xyz".

- Run the report.

Previous Topic  Next Topic
