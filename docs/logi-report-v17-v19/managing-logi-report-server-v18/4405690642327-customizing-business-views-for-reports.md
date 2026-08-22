---
title: "Customizing Business Views for Reports"
id: 4405690642327
section: "Managing Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690642327-Customizing-Business-Views-for-Reports
updated_at: 2022-01-27T07:59:37Z
---

# Customizing Business Views for Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683934999-Automatically-Recompiling-Dynamic-Resources-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683929879-Managing-Dynamic-Display-Names-of-Business-View-Elements)

# Customizing Business Views for Reports

This topic describes how you can customize business views for reports as an administrator.

For a report you created in Logi Report Designer while its **Constrained Data** property is false, or for a report you created on Server, you can customize the business views for the report. In this way, the combination of the customized business views and the business views used by the report are available to the report.

This topic contains the following sections:

* [Selecting Business Views for a Report Using the Properties Dialog Box](#Dialog)
* [Importing Business Views for Reports Using the Administration Menu](#Menu)

## Selecting Business Views for a Report Using the Properties Dialog Box

1. [Access the Properties dialog box of the report](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties#SingleResource) that has a catalog available in the server resource tree and that is not in the **My Shared** folder.
2. Select the **Available Business Views** tab.

   ![Properties dialog - Available Business Views tab](https://devnet.logianalytics.com/hc/article_attachments/4420461592855/prptyrpt_bv.gif)
3. Select the business views for the report to use.
4. Select **All** if you want to select all the listed business views.
5. To export the selected business views to a plain text file, select **Export**. The default file name is Report\_File\_Name.bvlst.
6. Select **OK** to apply the selected business views to the report.

## Importing Business Views for Reports Using the Administration Menu

1. On the system toolbar of the Server Console, navigate to **Administration** > **Other** > **Business Views for Reports**. Server displays the page:

   ![Importing Business Views for Reports](https://devnet.logianalytics.com/hc/article_attachments/4420461596311/mng_rsc_bv.gif)
2. Select **Browse** to select a plain text file in which you specify business views using a JSON array like ["Data Source 1.BV1","Data Source 1.BV2"]. For example, you can select a file that you exported the selected business views to when [selecting business views for a report using the Properties dialog box](#Dialog).
3. Select **OK** to import the business views from the file.

   ![Selecting Reports](https://devnet.logianalytics.com/hc/article_attachments/4420461596567/mng_rsc_bv_slctrpt.gif)
4. Select the reports you want to use the imported business views.
5. Select **All** if you want to select all the listed reports.
6. Select **OK** to apply the imported business views to the selected reports.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)When you work with a report in the Web Report Studio and Page Report Studio,

* Whether you can see a business view available to the report depends on whether you have the permission. For more information, see [Defining Business View Security in a Catalog](https://devnet.logianalytics.com/hc/en-us/articles/4405683933975-Changing-Resource-Properties#BVSecurity).
* If you created the report in Logi Report Designer and enabled its **Constrained Data** property, only the business views that the report uses are available to the report. In this case, if the report uses no business views, you cannot add any new data components in the report.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683934999-Automatically-Recompiling-Dynamic-Resources-in-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683929879-Managing-Dynamic-Display-Names-of-Business-View-Elements)
