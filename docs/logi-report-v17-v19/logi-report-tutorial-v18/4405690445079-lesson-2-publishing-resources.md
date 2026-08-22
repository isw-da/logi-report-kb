---
title: "Lesson 2: Publishing Resources"
id: 4405690445079
section: "Logi Report Tutorial v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690445079-Lesson-2-Publishing-Resources
updated_at: 2022-01-27T07:58:17Z
---

# Lesson 2: Publishing Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683487511-Lesson-1-Starting-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683488663-Lesson-3-Running-Reports)

# Lesson 2: Publishing Resources

Logi Report Server is only able to run reports and use library components that have been published to it. As you saw in the previous lesson, some reports have automatically been published to Logi Report Server in the Public Reports folder. In this lesson, we publish the reports and library components in the JinfonetGourmetJava.cat catalog which were created in the previous tracks. If you haven't completed those tracks or do not want to use your own, you can use the version of the JinfonetGourmetJava catalog offered by Logi Report Server, which is located at `<install_root>\help\samples\JinfonetGourmetJava`.

A report or library component must initially be published along with its catalog. Updates to the resource can be published independently, as long as the catalog associated with the resource remains published and has not changed. This enables you to quickly and easily install a change to a resource in the runtime environment.

This lesson contains the following tasks:

* [Task 1: Publish Reports](#Task1)
* [Task 2: Publish Library Components](#Task2)

## Task 1: Publish Reports

1. In the Resources page of the server console, open the **Public Reports** folder.
2. Select **Publish** > **From Server Machine** on the task bar of the Resources page.

   ![Publish to Local Server](https://devnet.logianalytics.com/hc/article_attachments/4420447434135/admin_lsn2_pblsh.gif)

   The Publish from Server Machine dialog box is displayed:

   ![Publish to Local Server Page](https://devnet.logianalytics.com/hc/article_attachments/4420453755543/admin_lsn2_dlg.gif)
3. Keep the default selected resource type Folder with Contents in the Resource Type drop-down list.

   The Resource Type list enables you to specify the resource, the catalog, report, or folder with these objects, to be published to Logi Report Server.
4. Select the **Browse** button next to the From Folder field, and then browse to select the `<install_root>\help\samples\JinfonetGourmetJava` directory.
5. In the Resource Node Name field type **JinfonetGourmetJava**.
6. In the Resource Description field type **Jinfonet Gourmet Java catalog and reports**.
7. Select **OK** to publish the resources.

   After the resources have been successfully published, the JinfonetGourmetJava folder is displayed in the resource tree.
8. Select the folder name **JinfonetGourmetJava** and the reports in the folder are listed:

   ![JinfonetGourmetJava Reports](https://devnet.logianalytics.com/hc/article_attachments/4420461815191/admin_lsn2_tab.gif)

## Task 2: Publish Library Components

1. In the Resources page of the server console, open the **My Components** folder.
2. Select **Publish** > **From Server Machine** on the task bar of the Resources page. The Publish Resources page is displayed.
3. Keep the default selected resource type Folder with Contents in the Resource Type drop-down list.
4. Select the **Browse** button next to the From Folder field, and then browse to select the `<install_root>\help\samples\JinfonetGourmetJava` directory.
5. In the Resource Node Name field type **JinfonetGourmetJava**.
6. In the Resource Description field type **Jinfonet Gourmet Java catalog and library components**.
7. Select **OK** to publish the resources.

   After the resources have been successfully published, the JinfonetGourmetJava folder is displayed in the resource tree.
8. Select the folder name **JinfonetGourmetJava** and the library components in the folder will be listed.

   ![JinfonetGourmetJava Library Components](https://devnet.logianalytics.com/hc/article_attachments/4420453755799/admin_lsn2_publc.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453376919/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683487511-Lesson-1-Starting-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420461444759/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683488663-Lesson-3-Running-Reports)
