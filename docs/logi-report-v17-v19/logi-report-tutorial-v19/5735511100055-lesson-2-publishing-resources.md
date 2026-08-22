---
title: "Lesson 2: Publishing Resources"
id: 5735511100055
section: "Logi Report Tutorial v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735511100055-Lesson-2-Publishing-Resources
updated_at: 2022-11-29T03:39:09Z
---

# Lesson 2: Publishing Resources

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735563057559-Lesson-1-Starting-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735497665815-Lesson-3-Running-Reports)

# Lesson 2: Publishing Resources

Server is only able to run reports and use library components that have been published to it. As you saw in the previous lesson, some reports have automatically been published to Server in the Public Reports folder. In this lesson, we publish the reports and library components in the JinfonetGourmetJava.cat catalog that were created in the previous tracks. If you have not completed those tracks or do not want to use your own, you can use the version of the JinfonetGourmetJava catalog offered by Server, which is located at `<install_root>\help\samples\JinfonetGourmetJava`.

You must publish a report or library component along with its catalog initially. You can publish updates to the resource independently, as long as the catalog associated with the resource remains published and has not changed. This enables you to quickly and easily install a change to a resource in the runtime environment.

This lesson contains the following tasks:

* [Task 1: Publish Reports](#Task1)
* [Task 2: Publish Library Components](#Task2)

## Task 1: Publish Reports

1. In the Resources page of the Server Console, open the **Public Reports** folder.
2. Navigate to **Publish** > **From Server Machine** on the task bar of the Resources page.

   ![Publish to Local Server](https://devnet.logianalytics.com/hc/article_attachments/9898539553559/admin_lsn2_pblsh.gif)

   Server displays the Publish from Server Machine dialog box.

   ![Publish to Local Server Page](https://devnet.logianalytics.com/hc/article_attachments/9898539560727/admin_lsn2_dlg.gif)
3. Keep the default selected resource type **Folder with Contents** in the **Resource Type** drop-down list. From the Resource Type list, you can specify the resource, the catalog, report, or folder with these objects, to publish to Server.
4. Select **Browse** next to the **From Folder** text box, and then browse to select the `<install_root>\help\samples\JinfonetGourmetJava` directory.
5. In the **Resource Node Name** text box, type **JinfonetGourmetJava**.
6. In the **Resource Description** text box, type **Jinfonet Gourmet Java catalog and reports**.
7. Select **OK** to publish the resources.
8. After Server publishes the resources successfully, it displays the **JinfonetGourmetJava** folder in the resource tree.
   Select the folder name and Server lists the reports in the folder.

   ![JinfonetGourmetJava Reports](https://devnet.logianalytics.com/hc/article_attachments/9898523367703/admin_lsn2_tab.gif)

## Task 2: Publish Library Components

1. In the Resources page of the Server Console, open the **My Components** folder.
2. Navigate to **Publish** > **From Server Machine** on the task bar of the Resources page. Server displays the Publish Resources page.
3. Keep the default selected resource type **Folder with Contents** in the **Resource Type** drop-down list.
4. Select **Browse** next to the **From Folder** text box, and then browse to select the `<install_root>\help\samples\JinfonetGourmetJava` directory.
5. In the **Resource Node Name** text box, type **JinfonetGourmetJava**.
6. In the **Resource Description** text box, type **Jinfonet Gourmet Java catalog and library components**.
7. Select **OK** to publish the resources.
8. After Server publishes the resources successfully, it displays the **JinfonetGourmetJava** folder in the resource tree. Select the folder name and Server lists the library components in the folder.

   ![JinfonetGourmetJava Library Components](https://devnet.logianalytics.com/hc/article_attachments/9898539572119/admin_lsn2_publc.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898403124503/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735563057559-Lesson-1-Starting-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898403130775/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735497665815-Lesson-3-Running-Reports)
