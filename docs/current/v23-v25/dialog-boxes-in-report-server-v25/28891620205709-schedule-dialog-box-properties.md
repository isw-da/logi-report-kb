---
title: "Schedule Dialog Box Properties"
id: 28891620205709
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891620205709-Schedule-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:27Z
source_host: docs-report.zendesk.com
---
# 
Schedule Dialog Box Properties

This topic describes how you can use the Schedule dialog box to schedule a task to run a report or multiple reports at  specific times and publish the reports to different destinations in various formats.

This topic contains the following sections:

- General Tab Properties

- Parameter Tab Properties

- Publish Tab Properties

- Conditions Tab Properties

- Notification Tab Properties

- Duration Tab Properties

You see these elements on all the tabs:

Back

Select to go back to the left tab. 

Next

Select to go to the right tab. 

Finish

Select to submit the task with the settings you specified here. 

Cancel

Select to close the dialog box without scheduling a report task.

Help

Select to view information about the dialog box.

## 
General Tab Properties

Select the General tab to specify the general information of the schedule task. It varies when you schedule to run a single report or multiple reports.

### 
For Single Report

Schedule Name

Specify the name for the schedule task.

Select Report Tabs 

The section is available for page reports only. Specify the report tabs you schedule to run. Server will export the selected report tabs following the list order. If the page report has only one report tab, it is selected by default. 

- 
Export to One File
 Select if you want to export the selected report tabs to one file.

- 
Move Up button
    Select to move the specified report tab higher in the list.

- 
Move Down button
       Select to move the specified report tab lower in the list.

Bursting Configuration

Available when you are scheduling a bursting report. 

- 
Select Schema
    Select one or more bursting schemas defined for the report to generate bursting results based on. 

Non-bursting Result

Available when you are scheduling a bursting report. Select to generate non-bursting result based on whole data without data splitting.

Select Dynamic Connection

The section is available when there are multiple dynamic connections for the current signed-in user. You can specify a dynamic connection.

- 
Data Source
 Data source name in the catalog.

- 
Connection Name
    Dynamic connection name.

- 
Connection
    Select a dynamic connection from the drop-down list. 

- 
Connection Properties
Information of the selected dynamic connection, which is read only.

Report Information

Specify the report information. 

- 
Report
 Information about the report.

- 
Catalog
 Catalog information. Unavailable to shared reports.
    - 
Select Another Catalog
        Specify another catalog for the report in the Select Another Catalog dialog box. 

- 
Report Version
Specify the report version used for the schedule task. The default version is always the latest version. This property is unavailable to shared reports.

- 
Catalog Version
  Specify the catalog version used for the schedule task. The default version is always the latest version. This property is unavailable to shared reports.

- 
Priority
This property is available to administrators.    Specify the priority level of the scheduled task. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority. By default, Server ignores this property unless you modify server.properties in <install_root>\bin to set queue.policy not equal to 0.

Advanced

Configure some advanced settings.

- 
Enable Style Group
If a style group has been specified via the Override Style Group option in the server profile, this Enable Style Group option here gets selected by default, and the specified default style group is selected in the Style Group drop-down list, which will apply to running all the selected report tabs or web report for all export formats. You can also choose another style group from the Style Group drop-down list to run the page report tabs or web report.
    When you select the <No Style> item in the Override Style Group drop-down list, this option is unselected by default, and the style group properties of the selected report tabs or web report for the corresponding export formats that are predefined in Report Designer will apply to the schedule task. These predefined style group properties take effect when publishing to version, disk, email, or FTP.

- 
Enable Converting Encoding
Select to enable the conversion of encoding. From the Before Converting and After Converting drop-down lists, select encoding as required.

- 
Enable NLS
Specify whether to enable NLS for the report. If the option is selected, Server will display the Using Language drop-down list for you to choose a language. If there is no NLS resource defined for the report, you can only run the report using the default language.

- 
Encoding
Specify the encoding of the report from the drop-down list.

- 
Connect to [Data Source Name]
Specify the DB user and password for connecting to the data source.
    
- 
Use the DB user and password defined in catalog
        Select if you want to use the DB user and password defined in the catalog.

- 
Use the DB User
        Select this property, and you can then specify another DB user and password instead of the one defined in the catalog.

- 
Add TaskListener to be Invoked
  Select to call a Java application before/after the task runs to obtain information about the task.

- 
Specify a preferred server to run the task
  Directly specify a server in a cluster to perform the schedule task instead of using load balancing. This property is available only when there are more than one active server in a cluster, and when the Identify Server Preference option in the server profile is selected.

- 
Enable Auto Recover Task
   Select if you want Server to automatically recover the task.    
- 
Maximum Retry Times
        Specify the maximum number of times for retrying running the task to recover it.

- 
 Retry Interval
        Specify the interval between retries.

- 
 Recreate All Results
        Select if you want to recreate all results. By default, Server only recreates failed results.

- 
Use User Defined Default On-screen Filter Values
Select to apply the default on-screen filter values specified to the report for the user. Unavailable when Enable Setting Default On-screen Filter Values For the corresponding report type is cleared in the server profile. 

- 
Use Bookmark
This property is available to web reports. Select a bookmark to run the bookmark of the web report. 

### 
For Multiple Reports

Schedule Name

Specify the name for the schedule task.

Report Information

Specify the report information. 

- 
Catalog
 Catalog used by the selected reports.

- 
Priority
This property is available to administrators.    Specify the priority level of the scheduled task. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority. By default, Server ignores this property unless you modify server.properties in <install_root>\bin to set queue.policy not equal to 0.

## 
Parameter Tab Properties

Use the Parameter tab to specify the parameter values if any to run the reports.

Enter Parameters

Server lists all the parameters used by the reports. Edit the values according to your requirement.

If the report uses no parameter, Server displays "No Parameter Needed" here.

Use Saved Values

If it is available, you can select the previously saved parameter values to apply to the report and save parameter values for reuse later.

Save as default

Select to save current parameter values as the default parameter values for the report. Server displays this option when you did not clear Enable Setting Default Parameter Values For the corresponding report type in the server profile. 

This option is a user-report level setting. It is an action and takes effect after you submit the scheduled task. Its initial status is always cleared.

## 
Publish Tab Properties

Use the Publish tab to specify the type of the task. You can use two main tasks to publish your reports: Default Task and User Task. By default, Server uses Default Task to publish the reports. To use the User Task, select User Task in the Default Task page.

Default Task

If you select Default Task to publish your reports with, when specifying the task type, you can choose from the following sub tasks:

- 
To Version
Select to publish the report to the versioning system.

- 
To Disk
Select to publish the report to the file system. This type is not supported to organization users or when you schedule to run multiple reports.

- 
To E-mail
Select to publish the report to email.

- 
To Printer
Select to publish the report to a printer. This type is not supported for bursting result or when you schedule to run multiple reports.

- 
To Fax
Select to publish the report to fax. This type is not supported for bursting result or when you schedule to run multiple reports.

- 
To FTP
Select to publish the report to an FTP site. This type is not supported when you schedule to run multiple reports.

 If you are scheduling a bursting report, the Publish tab changes according to the bursting setting that you made in the General tab of the Schedule dialog box. For more information, see Scheduling Bursting Reports.

User Task

If you select User Task to publish your reports, you can implement a customized task with schedule properties. This property is unavailable to organization users or to bursting reports.

- 
User Task Class Name
Specify the class name for the user task.

- 
Display Name
Specify the display name for the user task.

- 
User Task Properties
Specify user task properties to define tasks.

- 
Import User Task Properties from File
   Import a user task from a properties file.

- 
Upload Properties
  Upload the properties to Server. Server will list the properties in the User Task Properties area.

### 
To Version

Use the To Version tab to specify settings for publishing the report to the versioning system. 

Publish to Versioning System

Select to publish the report to the versioning system. You can publish it to the following formats:

- 
Logi Report Result
Select to publish the page report to a Logi Report result file (RST file). 

- 
Page Report Result
Select to publish the page report to a page report result file (RSD file). 

- 
Web Report Result
Select to publish the web report to a static web report result file (WST file). 

- 
HTML
Select to publish the report to the versioning system in HTML format. 

- 
PDF
Select to publish the report to the versioning system in PDF format.

- 
Excel
Select to publish the report to the versioning system in Excel format. 

- 
Text
Select to publish the report to the versioning system in Text format. 

- 
RTF
Select to publish the report to the versioning system in RTF format. 

- 
XML
Select to publish the report to the versioning system in XML format. 

- 
PostScript
Select to publish the report to the versioning system in PostScript format. 

Archive Location

Specify the location for the saved report version. This property is unavailable for bursting result.

- 
Built-in Version Folder
Specify to save the report version to the built-in version folder. This property is not available to organization users when the report is in the Public Reports folder, and to shared reports either.

- 
My Reports Folder
Specify to save the report version to the My Reports folder.

- 
Public Reports Folder
Specify to save the report version to the Public Reports folder. Not available to organization users.

- 
Organization Reports Folder
Specify to save the report version to the Organization Reports folder. Available to organization users only.

Apply Archive Policy

Apply an archive policy to the report version. Some of the following properties are unavailable for bursting result.

- 
Archive as New Version
Select to enable multiple versions for the report.
    - 
Maximum Number of Versions
Specify the maximum number of versions that  the report can have. The default value 0 means unlimited version number.

- 
Replace Old Version 
Select to replace the old version with the new version.

Result Auto-delete

Specify the deleted date of the result. If the time you specify exceeds one hundred years, Server will keep the result forever.

- 
Result Expires in N Days
Specify a period after which you want to automatically delete the result.

- 
Result Expires After
Specify a certain day when you want to automatically delete the report.

Set Permissions

The property is unavailable when the schedule task is based on multiple reports.

When the schedule task is based on a single report, the property is available only when the Archive Location is specified to be a public folder and when you have the Grant permission on the report. Select the link to open the Set Permissions dialog box to set user permissions   to the specified report tabs in the page report or web report.

### 
To Disk

Use the To Disk tab to specify settings for publishing the report to the file system. It is not available to organization users or when you schedule to run multiple reports.

Publish to Disk

Select to publish the report to the file system. You can publish the report to the following formats:

- 
Logi Report Result
Select to publish the page report to a Logi Report result file (RST file). You can export RST files to HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Server. This property is not available for bursting results, or when the schedule task contains both page reports and web reports. 
- 
Use Custom File Extension
Select if you want the output file to have no file extension or want to use a different file extension from the default one    (.rst).
        This property is not available on the advanced run  and schedule to version dialog boxes since you have no chance to specify a file name.
    

- 
Zip Result
Specify to compress the output to reduce the disk size and I/O; however, it uses more CPU resources.

- 
Run Linked Report
Select if you want to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, leave this property cleared.

- 
Precision Level
Specify the precision level with which you want to publish the report.  Changing the default value may cause abnormalities in report layout.

- 
Page Report Result
Select to publish the page report to a page report result file (RSD file) that you can view in a Page Report Studio. You cannot publish some reports in the Page Report Result format, such as self-contained (CLX) reports, multi-level nested master and subreports, reports containing data objects, and reports developed from a dynamic query or hierarchical data source (HDS).
 This property is not available for bursting results, or when the schedule task contains both page reports and web reports.  An RSD file is a middle result for page report that can preserve data and the working status of a page report and that you can share with others. Based on the RSD file, you can rebuild a page report to analyze data and to export to other formats. An RSD file is a standalone working file so it contains all the useful information, such as the catalog, report template, NLS, data, parameters, and security. The security information of an RSD file is the user of the generator that creates it. When different users open the same RSD, they will get the same result based on the same security configuration. You cannot refresh a report viewed from an RSD file to refetch data from the database. When the system rebuilds a report according to the RSD file, it will only load data from the RSD file. When opening a report RSD, you cannot go back to the actions which the RSD generator took before generating the RSD file but can take actions based on the current RSD resources. 

- 
Use Custom File Extension
Select if you want the output file to have no file extension or want to use a different file extension from the default one    (.rsd).
        This property is not available on the advanced run  and schedule to version dialog boxes since you have no chance to specify a file name.
    

- 
Zip Result
Specify to compress the output. The compressed file's suffix will still be .rsd, its size will be smaller which reduces IO and disk usage; however, it uses more CPU resources. 

- 
Precision Level
Specify the precision level with which you want to publish the report.  Changing the default value may cause abnormalities in the report layout.

- 
Web Report Result
Select to publish the web report to a static web report result file (WST file). You can export WST files to HTML, PDF, Text, Excel, XML, RTF, and Postscript formats via Server. This property is not available for bursting results, or when the schedule task contains both page reports and web reports. 
- 
Use Custom File Extension
Select if you want the output file to have no file extension or want to use a different file extension from the default one    (.wst).
        This property is not available on the advanced run  and schedule to version dialog boxes since you have no chance to specify a file name.
    

- 
Zip Result 
Specify to compress the output to reduce the disk size and I/O; however, it uses more CPU resources.

- 
Run Linked Report
Select if you want to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, leave this property cleared.

- 
Precision Level
Specify the precision level with which to publish the web report result.  Changing the default value may cause abnormalities in report layout.

- 
HTML
Select to publish the report to the file system in HTML format.

- 
PDF
Select to publish the report to the file system in PDF format.

- 
Excel
Select to publish the report to the file system in Excel format. 

- 
Text
Select to publish the report to the file system in Text format.  
    

- 
RTF
Select to publish the report to the file system in RTF format. 

- 
XML
Select to publish the report to the file system in XML format. 

- 
PostScript
Select to publish the report to the file system in PostScript format. 

For each format, you can decide whether to publish the output to the server resource tree or to the server disk path. Then you need to type in the blank location text box root of the resource tree or disk path as shown in the examples: 

- Example for server resource tree: /report1.rst

- Example for server disk path: C:\temp\report1.rst

When publishing a page report, if you choose the Logi Report Result and Page Report Result formats, you need only provide one file path because all selected report tabs will output into one file. For other formats, if you leave the Export to One File property in the General tab cleared, you need to specify a file path for each selected report tab.

### 
To E-mail

Use the To E-mail tab to specify settings for publishing the report to email. Some properties in the tab are unavailable for bursting result.

Mail To

Server lists the email addresses you have sent email to.

New

Select to create a new email.

- 
To
Specify the addresses you want to send the email to.

- 
Cc
Specify the addresses you want to send additional copies of the email to.

- 
Bcc
Specify the addresses you want to secretly send additional copies of the email to. The recipients in the Bcc list are known to the sender and themselves only.

- 
Ellipsis button
Select to open the Select Role, Group and User dialog box to select users, groups, and roles in the Report Server security system to use their email addresses to send the email.
            

- 
Subject
Specify the subject of the email.

- 
Comments
Specify the contents of the email or comments to the contents.

- 
Use Default SMTP Account
Select to use the default SMTP account configured in the Administration > Configuration > E-mail Server page on the Server Console as the email publish account.
    The property is selected by default. Clear it and you will be able to specify a different account using the following properties: 

- 
E-mail Address
Specify the email address of the new SMTP account. 

- 
User Name
Specify the username of the new account.

- 
Password
Specify the password of the new account. 

- 
Compress Attachment as Java Archive
Select to compress the email attachment as Java Archive.

- 
E-mail Result in HTML E-mail Format 
Select to send the report in the HTML format in the email body.
The report will overwrite the comments that you type for the email.    - 
Run Linked Report
Select if you want to generate the linked reports (excluding the detail reports) in the output when the report is linked with other reports. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data. If you are only interested in the primary report, leave this property cleared.

- 
E-mail Result in Plain Text E-mail Format
Select to send the report in plain text format in the email body, with no other information such as color and images.E-mail Result in HTML E-mail Format and E-mail Result in Plain Text Format cannot work concurrently.

When you select one of the following formats, that is you want to send the report as an attachment file, you can specify a file name for the file by setting the File Name property. 

- 
Attachment in Logi Report Result Format
Select to send the report in a Logi Report result file as the email attachment. Unavailable when the schedule task contains both page reports and web reports.

- 
Attachment in Web Report Result Format
Select to send the web report in a WST file as the email attachment. Unavailable when the schedule task contains both page reports and web reports.

- 
Attachment in HTML Format
Select to send the report in an HTML file as the email attachment.

- 
Attachment in PDF Format
Select to send the report in a PDF file as the email attachment.
     If an administrator enabled Split PDF in the Administration > Configuration > Export > E-mail tab on the Server Console, Server disables the TOC and Sign properties here.

- 
Attachment in Excel Format
Select to send the report in an Excel file as the email attachment.

- 
Attachment in Text Format
Select to send the report in a Text file as the email attachment.
    

- 
Attachment in RTF Format
 Select to send the report in an RTF file as the email attachment.

- 
Attachment in XML Format
Select to send the report in an XML file as the email attachment.

- 
Attachment in PostScript Format
Select to send the report in a PostScript file as the email attachment.

- 
OK
Select to retain the settings and add the email address into the Mail To list.

- 
Cancel
Select to cancel the settings.

Edit

Select to edit the specified email in the Mail To list. 

Delete 

Select to delete the specified email from the Mail To list.

### 
To Printer

Use the To Printer tab to specify settings for publishing the report to a printer. It is not available for bursting result or when you schedule to run multiple reports.

Publish to Printer 

Select to publish the report to a printer.

Select Print Method 

Specify the JDK print method to print the report.

Printer

Specify the name with the path of the printer. You can type it in the box or select it from the drop-down list.

When JDK1.4 is selected in the Select Print Method drop-down list, the following properties will be available.

Paper Size

Specify the paper size.

Print Range

Specify the pages to be printed.

Copies

Specify the number of copies you want to print. The number of copies will be applied to all specified pages.

Print to File

Select to print the document to a file instead of a printer. You can only open and print this kind of files by serial port printer on Windows via DOS command. 

- 
File Name
Specify the name of the file to which you print. If you don't provide the path in the file name, Server will save the file to the Server working directory. 

Job Attributes

Select to specify the properties of the print task.

- 
Priority
Specify the print priority for this task.

- 
Job Name
Specify the name of the print task.

- 
User Name
Specify the name of the user. 

Orientation

Select to specify the orientation for the printed output.

- 
Landscape
Select to print the report in a Landscape orientation.

- 
Portrait
Select to print the report in a Standard letter orientation.

- 
Reverse Landscape
Select to print the report in a Reverse Landscape orientation.

- 
Reverse Portrait
Select to print the report in a Reverse Portrait orientation.

Color Appearance

Specify to print the report in Monochrome or in Color.

Print Quality

Specify the print quality. It can be Draft, Normal, or High.

Print Sides

Specify the print sides for the report.

- 
One Side
Select to impose each consecutive print-stream page upon the same side of consecutive media sheets.

- 
Duplex 
Select to impose each consecutive pair of print-stream pages upon the front and back sides of consecutive media sheets, such that the orientation of each pair of print-stream pages on the medium is correct for the reader as if for binding on the long edge.

- 
Tumble
Select to impose each consecutive pair of print-stream pages upon front and back sides of consecutive media sheets, such that the orientation of each pair of print-stream pages on the medium is correct for the reader as if for binding on the short edge.

Sheet collate

Specify the printing order for printing multi-page report.

- 
Collated
If selected, when you print two copies of a three-page report, the page order is 1, 2, 3; 1, 2, 3.

- 
Uncollated
If selected, when you print two copies of a three-page report, the page order is 1, 1; 2, 2; 3, 3.

Margins

Specify the paper margins for the report (MM or Inch).

Media Tray 

First select a printer, and then from the drop-down list, specify the media tray.

### 
To Fax

Use the To Fax tab to specify settings for publishing the report to fax. It is not available for bursting result or when you schedule to run multiple reports.

 Before you can fax the report, you must configure your modem first, otherwise Server displays a warning message.

Publish to Fax 

Select to publish the report to fax.

Quality 

Specify the quality of the fax: Best, Normal, or Fast.

Include Cover Sheet

Specify whether to send a cover sheet with the fax.

Server displays the following items on the fax cover sheet.

To

Specify the name of the recipient.

From

Specify the name of the sender.

Company

Specify the sender's company.

Date

Specify the date when you want to send the fax. You can select the Calendar icon  to select a date from the calendar.

Fax Number

Specify the fax number of the recipient.

Phone Number

Specify the phone number of the sender.

Re

Specify the subject of the fax.

Comments

Specify the comments of the fax.

Urgent

Select if the fax is urgent.

For Review

Select if the recipient only needs to review the fax.

Please Comment 

Select if the recipients need to comment on the contents of the fax.

Please Reply 

Select if the fax needs a reply.

### 
To FTP

Use the To FTP tab to specify settings for sending the report to an FTP site. It is not available when you schedule to run multiple reports. Some properties in the tab are unavailable for bursting result. 

FTP To

Server list the FTP sites you can send the report to.

New

Select to create a new FTP site.

- 
Protocol Type
Specify the protocol type used for publishing the report to FTP.
    
- 
FTP (Standard File Transfer Protocol)
Files are transferred in a non-secure (plain text) style.

- 
SFTP using SSH2
SFTP (SSH File Transfer Protocol, also known as Secure FTP) is a way of securely transferring files over remote systems and is supported by most UNIX servers running SSH2. Ask your server administrator about its availability.

- 
SCP (Secure Copy)
This is a means of securely transferring computer files between a local and a remote host or between two remote hosts, using the Secure Shell (SSH) protocol. If you select this type, you will not be able to create folders to the FTP server.

- 
FTPS with TLS/SSL (Explicit)
Explicit connection type of FTP security with TLS/SSL.

- 
FTPS with TLS/SSL (Implicit)
Implicit connection type of FTP security with TLS/SSL.

- 
FTP Site Name
A user defined name of the FTP site. It is optional.

- 
Host Address
The domain name or IP address of the FTP site. It cannot be null.

- 
Port
The port of the FTP server. It is optional, and by default 21 is used for Standard FTP and Explicit FTPS, 22 SCP and SFTP, and 990 for Implicit FTPS.

- 
Logon Type
The way to authenticate to the FTP server. Available when SFTP using SSH2 is selected as the protocol type.
- 
Normal
Select to use a password to authenticate.

- 
Key File
Select to use a Secure Shell Protocol (SSH) key file to authenticate.

- 
Key File and User/Password
Select to use the combination of a Secure Shell Protocol (SSH) key file and the username/password to authenticate.

- 
User Name
The username is valid to the authentication of the FTP server that can access the FTP site. If not specified, Server will use "anonymous" as the username by default.

- 
Password
The password is valid to the authentication of the FTP server that enables the username to access the FTP site. Unavailable when you set Logon Type to Key File.

- 
Key File
The SSH key file used for authentication. Available when you set Logon Type to Key File or Key File and User/Password.

- 
Passphrase
The passphrase to decrypt the SSH key file. Available when you set Logon Type to Key File or Key File and User/Password.

- 
Account
The account of the FTP user if there exists.

- 
Folder Location
The location where you put the report files on the FTP server. If not specified, Server will use the root path "/" of the FTP server by default.

- 
Handler Class
You can use a customized FTP-client handler class instead of the one provided in Report. You should specify a fully-qualified class name that is package name plus class name, for example, test.DemoJakartaFTPHandler.

- 
Formats
Specify in which formats you want to send the report file to the FTP site. You can specify one or more formats. For each format, you need to specify a name for the report file.
    
- 
Logi Report Result
Select to send the report in a Logi Report result file to the specified FTP site.

- 
Web Report Result
Select to send the report in a WST file to the specified FTP site.

- 
HTML
Select to send the report in an HTML file to the specified FTP site.

- 
PDF
Select to send the report in a PDF file to the specified FTP site.

- 
Excel
Select to send the report in an Excel file to the specified FTP site.

- 
Text
Select to send the report in a Text file to the specified FTP site.
          

- 
RTF
Select to send the report in an RTF file to the specified FTP site.

- 
XML
Select to send the report in an XML file to the specified FTP site.

- 
PostScript
Select to send the report in a PostScript file to the specified FTP site.

- 
Check Connection
Select to check whether Server can connect to the specified FTP location with the specified user account.

- 
OK
Select to retain the settings and add the FTP site into the FTP To list.

- 
Cancel
Select to cancel the creation of the new FTP site.

Edit

Select to edit the specified FTP site in the FTP To list.

Delete

Select to remove the specified FTP site from the FTP To list.

## 
Conditions Tab Properties

Use the Conditions tab to specify the conditions for the publishing task. It contains the following sections: 

- Time Tab Properties

- Trigger Tab Properties

### 
Time Tab Properties

Use the Time tab to set settings for specifying the time for when you want to perform the task.

Time Zone

Select the time zone.

Time Type

Specify when you want to perform the task.

- 
Run this task immediately
Select if you want to perform the task as soon as you submit it.

- 
Run this task at
Select if you want to perform the task at a specific time.
      
- 
Date 
Select the Calendar icon  to select a date from the calendar.

- 
Time
Specify the time of the day.

- 
Run this task periodically
Select if you want to perform the task on a repeated basis.    
- 
Duration
Specify the period during which you want to perform the task on a repeated basis.

- 
Run after
Select and then specify the start date and time of the period.

- 
Run until
Select and then specify the end date and time of the period.

- 
Date
Specify the dates when you want to perform the task.         
- 
Daily
Select if you want to perform the task per a specific number of days or every weekday (from Monday to Friday).

- 
Weekly
Select if you want to perform the task on the specific days of the week per a specific number of weeks.

- 
Monthly
Select if you want to perform the task on a specific day of the month or week, per a specific number of months.

- 
Show/Hide Exception
Select to show or hide the exception date box, which lists the dates when you do not want to perform the task.
 
- 
Add
Select to add an exception date via the Select Condition dialog box.

- 
Remove
               Select to remove the selected exception dates.

- 
Time
Specify the time of the day when you want to perform the task.
     

- 
At
Select if you want to perform the task at a specific time of the day.

- 
Hourly
Select if you want to perform the task at a specific minute per a specific number of hours.

- 
Minutely
Select if you want to perform the task per a specific number of minutes.

- 
Run missed task upon server restart
       Select if you want to run missed tasks when you restart the server.

### 
Trigger Tab Properties

Use the Trigger tab to set settings for specifying a trigger for the task. 

Select a trigger to bind

Select a trigger from the list for the task. 

New Trigger

Select to open the New Trigger dialog box to create a new trigger. This property is not available to organization users.

Logic with time condition

Specify the logic between the time condition and trigger condition.

- 
Trigger Only
    Select if you want to perform the task only when an administrator fires the trigger. 

- 
Trigger and Time Condition 
 Select if you want to perform the task when both time is up and an administrator fires the trigger.
       When you select this logic: 

- No matter which condition is ready, Server performs the task only when its counterpart is ready.

- If you specify to perform the task at a specific time, you must select Run missed task upon server restart, otherwise Server regards the task as expired and deletes it when the time condition is ready before the trigger condition.

- 
Time Condition after Trigger 
    Select if you want to perform the task when time is up after an administrator fires the trigger. If the time condition is ready before the trigger condition, Server regards the task as expired and deletes it.

- 
Time Condition or Trigger
    Select if you want to perform the task when either time is up or an administrator fires the trigger.

## 
Notification Tab Properties

Use the Notification tab to notify someone by email when the task finishes running, regardless of whether it is successful or not.

Successful Task/Failed Task 

Select if you want to send an email when the task is successful/unsuccessful. 

Mail To

Server lists the email addresses you have sent email to.

New

Select to create a new email.

- 
To
Specify the address you want to send the email to.

- 
Cc
Specify the address you want to copy the email to.

- 
Bcc
Specify the address you want to secretly copy the email to.

- 
Subject
Specify the subject of the email.

- 
Comments
Specify the contents of the email or comments to the contents.

- 
Use Default SMTP Account
Specify whether to use the default SMTP account configured in the Administration > Configuration > E-mail Server page on the Server Console as the email publish account.    The property is selected by default. Clear it and you will be able to specify a different account using the following properties: 

- 
E-mail Address
        Specify the email address of the new SMTP account. 

- 
User Name
        Specify the username of the new account.

- 
Password
        Specify the password of the new account. 

- 
OK
Select to retain the settings and add the email address into the Mail To list.

- 
Cancel
Select to cancel the settings. 

Edit

Select to edit the selected email in the Mail To list.

Delete 

Select to remove the selected email from the Mail To list.

## 
Duration Tab Properties

The Duration tab is available only when you have enabled the task-level timeout mechanism. In this tab, you can specify a time duration for the task, and ask Server to cancel the task or to notify you or someone else of the task status via email if the task has not yet finished running when the task duration is up.

The following are the available properties:

Timeout

Specify the time duration for the task.

Notify by e-mail after the specified time

Select to send an email about the task information when the specified time is up.

- 
Mail To
Specify the email address of the recipient.

Cancel the task after the specified time

Select to cancel the running task when the specified time is up.
