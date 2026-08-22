---
title: "Examples of Scheduling Reports"
id: 1500009778441
section: "Scheduling Tasks to Run Reports"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009778441-Examples-of-Scheduling-Reports
updated_at: 2021-07-24T00:47:40Z
---

# Examples of Scheduling Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778461-Scheduling-to-Run-Multiple-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778401-Scheduling-Bursting-Reports)

# Examples of Scheduling Reports

This topic provides examples of creating schedule tasks to publish reports to different destinations: the Versioning System, disk, email, printer, fax, and an FTP site.

This topic contains the following sections:

* [Example 1: Scheduling to Publish a Report to the Versioning System](#Version)
* [Example 2: Scheduling to Publish a Report to Disk](#Disk)
* [Example 3: Scheduling to Publish a Report to E-mail](#Mail)
* [Example 4: Scheduling to Publish a Report to Printer](#Printer)
* [Example 5: Scheduling to Publish a Report to Fax](#Fax)
* [Example 6: Scheduling to Publish a Report to an FTP Site](#FTP)

## Example 1: Scheduling to Publish a Report to the Versioning System

In this example, you will create a schedule task to publish a page report to the versioning system in the Logi Report Result and PostScript file formats immediately. You will put the generated result to the built-in version table of the report and keep the result for 60 days.

1. Located the report in the server resource tree, then put the mouse pointer over the report row and select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880187927/btn_schdl.gif) on the floating toolbar to open the Schedule dialog box.
2. In the **General** tab, specify the [general report settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report#General).
3. In the **Parameter** tab, specify the parameter values as required if the report has parameters.
4. In the **Publish** tab,
   1. Select the **To Version** tab, then select **Publish to Versioning System**.
   2. Select the Logi Report **Result** and **PostScript** formats and set the format settings.
   3. Keep the default Archive Location to be **Built-in Version Folder** to save the report result version in the built-in version folder of the report.
   4. Select **Result Auto-delete** and define the result to expire in **60** days.

      ![Publish to Version](https://devnet.logianalytics.com/hc/article_attachments/4404880231319/wkrpt_sch_dlg_eg_vrsn.gif)
5. In the **Conditions** tab, select the **Time** tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task immediately**.
6. Go to the **Notification** tab and then set the settings if you want to notify someone of when the task is finished by sending an e-mail.
7. Select **Finish** to submit the task.
8. Select **My Tasks** on the system toolbar. You can see a record of the task in the Running table when the task is being performed. Logi Report Server will put it into the Completed table once it is completed.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)The Logi Report Result and Page Report Result formats for page reports are based on the report level. Therefore, when you schedule to run a page report to the versioning system, Server outputs the page report with all selected report tabs to a single file no matter whether you selected **Export to One File** in the General tab.

**Tip:** There is another way to publish the result of a report to version.

1. Set the property server.version.from.temp to true in the server.properties file in  `<install_root>\bin`, or select the option Enable "Publish to Versioning System" for Background Tasks View in the Administration > Configuration > Advanced page in the Server Console.
2. [Run a report in the Advanced mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports#Advanced), select a format other than Page Report or Web Report in the Format tab. Specify other settings as required. Then select **Finish**.
3. In the view page, you will see a link Publish to Versioning System at the upper-left corner. Select the link to publish the report to version in the current format.

## Example 2: Scheduling to Publish a Report to Disk

In this example, you will create a schedule task to publish a page report to the file system in the Page Report Result and XML file formats repeatedly at the start of each month at 7:00 AM. You will save the page report result file in the Public Reports folder in the server resource tree, and save the XML result file in the local directory `D:\PublishedResult` on the server machine.

1. Located the report in the server resource tree, then put the mouse pointer over the report row and select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880187927/btn_schdl.gif) on the floating toolbar to open the Schedule dialog box.
2. In the **General** tab, specify the [general report settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report#General). Suppose the page report contains two report tabs. By default, both report tabs are selected to run by the schedule task.
3. In the **Parameter** tab, specify the parameter values as required if the report has parameters.
4. In the **Publish** tab,
   1. Select the **To Disk** tab, then select **Publish to Disk**.
   2. Select **Page Report Result**, keep the default result location as Publish to Server Resource Tree, in the location text box specify the server resource tree path and file name of the result as **/PublishedResult.rsd**.
   3. Select **XML**, select **Publish to Server Disk Path**, specify the disk path and file name of the result, then set the other format settings as required. In this example, the page report contains two report tabs but Export to One File is not selected in the General tab, so we need to provide the disk path and file name for each of the report tab. Type **D:\PublishedResult\Result1.xml** for report1 and **D:\PublishedResult\Result2.xml** for report 2.

      ![Publish to Disk](https://devnet.logianalytics.com/hc/article_attachments/4404885372055/wkrpt_sch_dlg_eg_disk1.gif)
5. In the **Conditions** tab,
   1. In the **Time** tab, define the time zone from the Time Zone drop-down list, then from the Time Type drop-down list, choose **Run this task periodically**.
   2. In the **Duration** box, you can specify a period for when the task will be performed.
   3. Select **Monthly** from the Date drop-down list and keep the default to run on the first day of every 1 month.
   4. Edit the Time settings to **7:00 AM**.

   ![Schedule dialog - Time](https://devnet.logianalytics.com/hc/article_attachments/4404880231831/wkrpt_sch_dlg_eg_disk2.gif)
6. Go to the **Notification** tab and set the settings if you want to notify someone of when the task is finished by sending an e-mail.
7. Select **Finish** to submit the task.
8. Select **My Tasks** on the system toolbar. You can see that the task has been recorded in the Scheduled table. Since you have not specified a duration to run the task until a certain time, Logi Report Server will not stop performing it until you delete or disable it from the Scheduled table.

The following shows more about the **To Disk** publish type. You should be aware of them when you schedule to publish a report to disk.

* [Organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) cannot use the To Disk publish type. You are not able to use this publish type when you schedule to run multiple reports either.
* The Logi Report Result and Page Report Result formats for page reports are based on the report level. Therefore Logi Report Server will output the page report with all selected report tabs to a single file when you schedule to run a page report no matter whether you select Export to One File in the General tab or not.
* For each of the selected format, you need to provide the correct server resource tree path/disk path and file name with correct format type as the suffix for the corresponding result file. In addition, for a page report, except for the Logi Report Result and Page Report Result formats, you need to specify the path and file name for the result file of each specified report tab in the report if you do not select the Export to One File option in the General tab. You can apply [dynamic names](https://devnet.logianalytics.com/hc/en-us/articles/1500009749622-Applying-Dynamic-Names-for-Published-Result-Files) in the file name of the result.
  + To save the result in the My Reports folder in the server resource tree, the path is "/USERFOLDERPATH/*username*/" (change *username* to the real user name with which you log onto Logi Report Server).

    Example: /USERFOLDERPATH/admin/report1.pdf
  + To save the result in the Public Reports folder in the server resource tree, the path is "/".

    Example: /report2.html.
* When you specify to publish the report result to the server resource tree, Logi Report Server will put the result to the real path if the specified folder has a [real path](https://devnet.logianalytics.com/hc/en-us/articles/1500009777261-Getting-and-Using-Resources-From-a-Real-Path). Otherwise Logi Report Server will put the result to the default disk location where server resources are saved, that is `<install_root>\jreports` which is the mapped disk path of the root node "/" on the server resource tree.
* If you specify to publish the report result to a non-existent folder on disk, Logi Report Server will automatically create it.

## Example 3: Scheduling to Publish a Report to E-mail

The server administrator must have configured an [e-mail server](https://devnet.logianalytics.com/hc/en-us/articles/1500009743742-Configuring-the-E-mail-Server) before you can e-mail the report result.

In this example, you will create a schedule task to send the result of a report by e-mail.

1. Located the report in the server resource tree, then put the mouse pointer over the report row and select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880187927/btn_schdl.gif) on the floating toolbar to open the Schedule dialog box.
2. In the **General** tab, specify the [general report settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report#General).
3. In the **Parameter** tab, specify the parameter values as required if the report has parameters.
4. In the **Publish** tab, select the **To E-mail** tab.

   ![Schedule to E-mail](https://devnet.logianalytics.com/hc/article_attachments/4404880232087/sch_pub_mal.gif)

   From the **Mail To** list, select to whom the report result will be sent. You can select the **Edit** button to edit the specified e-mail.
   If you want to create another e-mail, select the **New** button, then fill in [every field](https://devnet.logianalytics.com/hc/en-us/articles/1500009774581-Schedule-Dialog-Box-Properties#NewMail), select the formats in which you want to send the report result and set the settings accordingly. When you choose to send the result as an attachment, you need to specify a file name for the attachment. You can apply [dynamic names](https://devnet.logianalytics.com/hc/en-us/articles/1500009749622-Applying-Dynamic-Names-for-Published-Result-Files) for the result file.

   When you create or edit an e-mail, you can select ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880232343/btn_chsr5.gif) next to the To, Cc, and Bcc text boxes to access the [Select Role, Group and User](https://devnet.logianalytics.com/hc/en-us/articles/1500009746482-Select-Role-Group-and-User-Dialog-Box-Properties) dialog box to select the users, groups, and roles in the Logi Report Server security system to use their mail addresses to send the e-mail. Admin users can [customize the scheduling recipients](https://devnet.logianalytics.com/hc/en-us/articles/1500009749862-Managing-User-Accounts#Recipient) that are available to you.
5. Specify the time for when to perform the task in the **Conditions** tab.
6. Go to the **Notification** tab and set the settings if you want to notify someone of when the task is finished by sending an e-mail.
7. Specify the settings in the **Duration** tab if you want to specify a timeout for the task.
8. Select **Finish** to have the task performed.
9. Select **My Tasks** on the system toolbar. You can see a record of the task in the Running table when the task is being performed. Logi Report Server will put it into the Completed table once it is completed.

## Example 4: Scheduling to Publish a Report to Printer

In this example, you will create a schedule task to send the result of a report to a printer.

1. Located the report in the server resource tree, then put the mouse pointer over the report row and select the  **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880187927/btn_schdl.gif) on the floating toolbar to open the Schedule dialog box.
2. In the **General** tab, specify the [general report settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report#General).
3. In the **Parameter** tab, specify the parameter values as required if the report has parameters.
4. In the **Publish** tab,
   1. Select the **To Printer** tab and then select **Publish to Printer**.

      ![Publish to Printer](https://devnet.logianalytics.com/hc/article_attachments/4404880232855/sch_pub_prnt.gif)
   2. Select a print method from the **Select Print Method** drop-down list.
   3. Type a name with the path of the printer in the **Printer** text box or select it from the drop-down list
      that follows.
   4. Specify other [options](https://devnet.logianalytics.com/hc/en-us/articles/1500009774581-Schedule-Dialog-Box-Properties#Printer) if you select to use the JDK1.4 print method, such as the paper size, print range, and print quality.
5. Specify the time for when to perform the task in the **Conditions** tab.
6. Go to the **Notification** tab and set the settings if you want to notify someone of when the task is finished by sending an e-mail.
7. Specify the settings in the **Duration** tab if you want to specify a timeout for the task.
8. Select **Finish** to have the task performed.
9. Select **My Tasks** on the system toolbar. You can see a record of the task in the Running table when the task is being performed. Logi Report Server puts it into the Completed table once it is completed.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* When there is no printer connected with Server, and you schedule to publish a report to a printer, the server may crash or throw an exception.
* Server cannot obtain information on which options are supported and which are not from your printer and reflect it in the To Printer tab. You should configure the setting according to your printer carefully.

## Example 5: Scheduling to Publish a Report to Fax

The server administrator must have configured the [fax settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009743702-Configuring-Export-Settings#Fax) before you can fax the report result.

In this example, you will create a schedule task to publish the result of a report to fax.

1. Located the report in the server resource tree, then put the mouse pointer over the report row and select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880187927/btn_schdl.gif) on the floating toolbar to open the Schedule dialog box.
2. In the **General** tab, specify the [general report settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report#General).
3. In the **Parameter** tab, specify the parameter values as required if the report has parameters.
4. In the **Publish** tab, select the **To Fax** tab, select the **Publish to Fax** option and then fill in [every field](https://devnet.logianalytics.com/hc/en-us/articles/1500009774581-Schedule-Dialog-Box-Properties#Fax) and set the settings according to your requirements.

   ![Publish to Fax](https://devnet.logianalytics.com/hc/article_attachments/4404880233111/sch_pub_fax.gif)
5. Specify the time for when to perform the task in the **Conditions** tab.
6. Go to the **Notification** tab and set the settings if you want to notify someone of when the task is finished by sending an e-mail.
7. Specify the settings in the **Duration** tab if you want to specify a timeout for the task.
8. Select **Finish** to have the task performed.
9. Select **My Tasks** on the system toolbar. You can see a record of the task in the Running table when the task is being performed. Logi Report Server will put it into the Completed table once it is completed.

## Example 6: Scheduling to Publish a Report to an FTP Site

In this example, you will create a schedule task to publish the result of a report to an FTP site.

1. Located the report in the server resource tree, then put the mouse pointer over the report row and select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4404880187927/btn_schdl.gif) on the floating toolbar to open the Schedule dialog box.
2. In the **General** tab, specify the [general report settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009778481-Scheduling-to-Run-a-Report#General).
3. In the **Parameter** tab, specify the parameter values as required if the report has parameters.
4. In the **Publish** tab,
   1. Select the **To FTP** tab.

      ![Publish to FTP](https://devnet.logianalytics.com/hc/article_attachments/4404885373079/sch_pub_ftp.gif)
   2. Select the **New** button to set up a new FTP site or select the **Edit** button to edit a specified FTP site in the **FTP To** list.
   3. Fill in [every field](https://devnet.logianalytics.com/hc/en-us/articles/1500009774581-Schedule-Dialog-Box-Properties#FTP), select the formats in which you want to send the report result and then set the settings according to your requirements.
5. Specify the time for when to perform the task in the **Conditions** tab.
6. Go to the **Notification** tab and set the settings if you want to notify someone of when the task is finished by sending an e-mail.
7. Specify the settings in the **Duration** tab if you want to specify a timeout for the task.
8. Select **Finish** to have the task performed.
9. Select **My Tasks** on the system toolbar. You can see a record of the task in the Running table when the task is being performed. Logi Report Server will put it into the Completed table once it is completed.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009778461-Scheduling-to-Run-Multiple-Reports)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009778401-Scheduling-Bursting-Reports)
