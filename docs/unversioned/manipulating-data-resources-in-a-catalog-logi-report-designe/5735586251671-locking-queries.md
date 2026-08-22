---
title: "Locking Queries"
id: 5735586251671
section: "Manipulating Data Resources in a Catalog - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735586251671-Locking-Queries
updated_at: 2022-11-02T08:17:46Z
---

# Locking Queries

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534106007-Working-with-Union-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735547165591-Applying-the-Filter-of-a-Query-to-Multiple-Queries)

# Locking Queries

Normally in Designer, queries are free to be shared among reports, which could increase the potential risk of being changed unexpectedly. When a query is shared by more than one report, it can be changed by any of those reports, which means you must be very careful to avoid causing impacts to other reports when you modify the shared query for one report. Therefore, Designer provides you with the flexibility to lock a query to prevent it from being changed unintentionally when someone using the same catalog creates a new report. Once a query is locked, it cannot be used by another report, so when you modify the query you know it does not affect any other reports. This topic describe how you can use the Lock Query feature to ensure each report can have a unique query.

This topic contains the following sections:

* [Creating a User for a Query](#Create)
* [Locking or Sharing a Query](#Lock)

## Creating a User for a Query

Before you can lock or share a query, you need to claim the query by creating a user for it. A query can be claimed by only one user.

**To creating a user to a query**

1. In the Catalog Manager, right-click the query you want to claim and select **Create User** from the shortcut menu. Designer displays the [Create Query's Username and Password dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522220695-Create-Query-s-Username-and-Password-Dialog-Box).

   ![Create Query's Username and Password dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898475085079/crtqrynmpw.gif)
2. Type in the user name and password.
3. Select **OK** to confirm the information.

After creating a user for a query, you can also modify the user information or remove the user.

**To modify the user information**

1. Right-click the query and select **Modify User** from the shortcut menu. Designer displays the Modify User Information dialog box.
2. Provide the old user name and password and select **OK**.
3. In the [Create Query's Username and Password dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735522220695-Create-Query-s-Username-and-Password-Dialog-Box), type in the new user name and password and select **OK**.

**To remove a user**

1. Right-click the query and select **Delete User** on the shortcut menu.
2. In the Remove User dialog box, provide the user and password information and select **OK**. The query is then free to be shared.

## Locking or Sharing a Query

Using the Share property of a query, you can lock or unlock it. By default, the Share property of a query is "true", which means that all queries in a catalog can be shared among multiple reports until you lock them.

**To lock or unlock a query**

1. In the Catalog Manager, select the query that you want to lock or unlock.
2. Select **Show Properties** on Catalog Manager toolbar to show the Properties sheet.
3. Locate the **Share** property and set its value to **true** or **false**. If it is "true", the query can be shared among reports and can be modified; otherwise, the query is locked and can be neither used in new reports nor modified by another user using the same catalog.

You can also lock or unlock a query using the following method:

1. In the Catalog Manager, right-click the query that has already been claimed by a user and select **Set Share Property** from the shortcut menu.
2. In the Set Query's Share Property dialog box, provide the user information and select or clear **Share**.

   ![Set Query's Share Property dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898458028055/qury_lock_share.gif)
3. Select **OK** to confirm the change.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* If a query has not yet been claimed by any user, when you set its Share property in the Properties sheet, Designer prompts you to claim the query by creating a user to it first.
* If a query is locked, it is password protected. Unless you provide valid user information, you are neither able to create a report directly using that query nor make changes to the query, including setting its Share property.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735534106007-Working-with-Union-Queries)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735547165591-Applying-the-Filter-of-a-Query-to-Multiple-Queries)
