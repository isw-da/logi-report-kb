---
title: "Bookmarking a Web Report"
id: 7985371637143
section: "Web Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/7985371637143-Bookmarking-a-Web-Report
updated_at: 2022-10-31T17:15:24Z
---

# Bookmarking a Web Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985339998487-Managing-Datasets-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741464615703-Saving-a-Web-Report)

# Bookmarking a Web Report

This topic describes how you can bookmark a web report with different parameter and filter scenarios and manage the bookmarks for a web report in Web Report Studio.

This topic contains the following sections:

* [Bookmarking a Web Report](#Bookmark)
* [Managing Bookmarks for a Web Report](#Manage)

## Bookmarking a Web Report

You can create bookmarks for a web report with different parameter and filter scenarios. Filters include these types: [on-screen filters](https://devnet.logianalytics.com/hc/en-us/articles/5741470839191-Applying-Filters-in-Web-Report#OnScreen), [dataset filters](https://devnet.logianalytics.com/hc/en-us/articles/5741470839191-Applying-Filters-in-Web-Report#BV), browser filters that you create via the [Filter dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741470839191-Applying-Filters-in-Web-Report#Dialog), and go-to filters that you create when performing the [go-to-by-value action](https://devnet.logianalytics.com/hc/en-us/articles/5741476511127-Going-Through-Web-Report-Data#Go-to-by-value).

To bookmark the active web report with its current parameter and filter status in Web Report Studio:

1. Select the **Save Bookmark** button ![Save Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9905574599191/btn_wbrpt_svbkmk.gif) on the toolbar. Server displays the [Bookmark dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985355762711-Bookmark-Dialog-Box-Properties).

   ![Bookmark dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905612658583/bkmk.gif)
2. You can view the parameters and filters that are applying to the report.
3. Type a name for the bookmark in the **Name** field. The name should not be used by other bookmarks.
4. Provide a description for the bookmark in the **Description** field.
5. Select **OK** to create the bookmark.

When you have created bookmarks for a web report, you can then [set the default bookmark](#DefaultBookmark) so that Server applies it when [running the web report in Web Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/5741439314455-Running-Reports#Bookmark) from the Server Console next time.

## Managing Bookmarks for a Web Report

You can view and manage bookmarks for the active web report in Web Report Studio.

1. Select the **Bookmark Setting** button ![Save Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/9905574662167/btn_wbrpt_bkmkst.gif) on the toolbar. Server displays the [Bookmark Setting dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985324116503-Bookmark-Setting-Dialog-Box-Properties).

   ![Bookmark Setting dialog box](https://devnet.logianalytics.com/hc/article_attachments/9905574774167/bkmkst.gif)
2. Server lists all the bookmarks that you have created for the web report. To view or update a bookmark, select **Details**, and then view the bookmark information or update the name and description of the bookmark in the [Bookmark dialog box](https://devnet.logianalytics.com/hc/en-us/articles/7985355762711-Bookmark-Dialog-Box-Properties).
3. You can set a bookmark as the default bookmark for the report. Select the bookmark, and then select **Set as Default**. By default, Server displays the default bookmark when you run the web report in Web Report Studio.

   Later if you want to cancel the default bookmark, select it and then select **Clear Default**.
4. To open a bookmark and replace the current report, select the bookmark, and then select **Apply**.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9905612785687/noteicon.jpg) You cannot undo or redo the action after you apply a bookmark.
5. To remove a bookmark, select it, and then select **Delete**.
6. Select **OK** to apply any changes you made here.

You can also update and remove bookmarks and set the default bookmark for a web report on the Server Console. See [Running Web Reports Using Default Bookmark](https://devnet.logianalytics.com/hc/en-us/articles/5741439314455-Running-Reports#Bookmark).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/7985339998487-Managing-Datasets-in-Web-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741464615703-Saving-a-Web-Report)
