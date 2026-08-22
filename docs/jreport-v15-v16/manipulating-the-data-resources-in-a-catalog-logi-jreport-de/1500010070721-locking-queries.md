---
title: "Locking Queries"
id: 1500010070721
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010070721-Locking-Queries
updated_at: 2021-07-24T10:37:46Z
---

# Locking Queries

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070701-Using-a-Query-to-Filter-Multiple-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034722-Query-Modifiers)

# Locking Queries

Normally in Logi JReport Designer, queries are free to be shared among reports, which could increase the potential risk of being changed unexpectedly. When a query is shared by more than one report, it can be changed by any of those reports, which means you must be very careful to avoid causing impacts to other reports when you modify the shared query for one report. However, Logi JReport provides you with the flexibility to lock a query to prevent it from being changed unintentionally when someone using the same catalog creates a new report. Once a query is locked, it cannot be used by another report even if you do not want to make any changes to the query.

By using this feature, you can ensure each report has a unique query so when you modify the query you know it cannot affect any other reports.

Below is a list of the sections covered in this topic:

* [Creating a User for a Query](#Create)
* [Locking or Sharing a Query](#Lock)

## Creating a User for a Query

Before you can lock or share a query, you need to claim the query by creating a user for it.

**To creating a user to a query:**

1. In the Catalog Manager, right-click the query you want to claim and select **Create User** from the shortcut menu. The [Create Query's Username and Password](https://devnet.logianalytics.com/hc/en-us/articles/1500010030162-Create-Query-s-Username-and-Password-Dialog) dialog appears.

   ![Create Query's Username and Password dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901141399/crtqrynmpw.gif)
2. Type in the user name and password.
3. Select **OK** to confirm the information.

When a user has been created for a query, you can modify the user information or remove the user as required.

* To modify the user information:

1. Right-click the query and select **Modify User** from the shortcut menu. The Modify User Information dialog appears.
2. Provide the old user name and password and select **OK**. The [Create Query's Username and Password](https://devnet.logianalytics.com/hc/en-us/articles/1500010030162-Create-Query-s-Username-and-Password-Dialog) dialog appears.
3. Type in the new user name and password as required and select **OK**.

* To remove a user, right-click the query and select **Delete User** on the shortcut menu. In the Remove User dialog, provide the user and password information and select **OK**. The query is then free to be shared.

**Note:** A query can be claimed by only one user.

## Locking or Sharing a Query

Using the Share property of a query, you can lock or unlock it according to your requirements. By default, the Share property of a query is true, which means that all queries in a catalog can be shared among multiple reports until you lock them.

**To lock or unlock a query:**

1. In the Catalog Manager, select the query that you want to lock or unlock.
2. Select **Show Properties** on Catalog Manager toolbar to show the Properties sheet.
3. Locate the Share property and set its property to true or false. If it is true, the query can be shared among reports and can be modified. Otherwise, the query is locked and can be neither used in new reports nor modified by another user using the same catalog.

You can also lock or unlock a query in the following way:

1. In the Catalog Manager, right-click the query that has already been claimed by a user and select **Set Share Property** from the shortcut menu.
2. In the Set Query's Share Property dialog, provide the user information and check or clear the Share option as required.

   ![Set Query's Share Property dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901141655/qury_lock_share.gif)
3. Select **OK** to confirm the change.

**Notes:**

* If a query has not yet been claimed by any user, when you set its Share property in the Properties sheet, you will be prompted to claim the query by creating a user to it.
* If a query is locked, it is password protected. Unless you provide valid user information, you will neither be able to create a report directly using that query nor make changes to the query, including setting its Share property.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070701-Using-a-Query-to-Filter-Multiple-Queries) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034722-Query-Modifiers)
