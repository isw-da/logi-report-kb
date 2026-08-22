---
title: "Cached Report Bursting"
id: 4405690679703
section: "Logi Report Server Security System Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690679703-Cached-Report-Bursting
updated_at: 2022-01-27T07:59:48Z
---

# Cached Report Bursting

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690678807-Report-Security-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684016663-Record-Level-and-Column-Level-Security)

# Cached Report Bursting

Logi Report supports cached report bursting which creates a security mechanism for controlling access to a report. This topic describes how you can view and schedule a report with cached report bursting, on Logi Report Server.

Security in a report is a kind of privileged control. By defining which groups of data are available to which users, groups, or roles, Logi Report creates a report for each user, role, and group. When a user accesses the report, Logi Report checks the group and role of the user and merges the groups of data in the report that the user is authorized to see and displays it to the user. Cached report bursting is implemented with these security properties on the group panel: Cascade, Grant, Groups, and Roles. The feature enables different users to view different data groups according to their access privileges. It also applies to nested groups.

For more information about setting up cached report bursting in reports, see Applying Cached Report Bursting in the *Logi Report Designer Guide*.

This topic contains the following sections:

* [Viewing a Report with Cached Report Bursting](#View)
* [Scheduling a Report with Cached Report Bursting](#Schedule)

+ [Scheduling to HTML/Page Report Result to Version](#HTML)
+ [Scheduling to Email](#Mail)
+ [Scheduling to Other Formats](#Other)

* [Example: Emailing Billing Reports](#Example)

## Viewing a Report with Cached Report Bursting

Since the control of report access is not possible without a user ID, the significance of this function is only apparent after reports have been published to Logi Report Server and users access it using their Logi Report User ID (security identifier).

When a client views a report with cached report bursting in Logi Report Server, the corresponding groups will be displayed according to the security identifier. You can also advanced run reports with cached report bursting in different formats, including Page Report, HTML, PDF, TEXT, Excel, PS, XML and Rich Text Format (this feature does not support the RST format).

To view a report with cached report bursting in Logi Report Server, the report must first be published to the server from Logi Report Designer. For example, if in Logi Report Designer, the security for a report that is grouped by the Customer\_Region field has been set as follows:

* The user ID admin has the privilege to view the CA and MN groups of the report.
* The user ID Jennifer has the privilege to view the BC group of the report.

Then,

1. [Access the Server Console](https://devnet.logianalytics.com/hc/en-us/articles/4405690636055-Accessing-Logi-Report-Server-via-a-Web-Browser) with the user ID admin.
2. Browse to the report that you are going to view.
3. Select the report name, and you will then be able to view the CA and MN groups of the report.
4. If you sign in to Logi Report Server with the user ID Jennifer, you will then only be able to view the BC group.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)When you designed the report in Logi Report Designer and set the Cascade property to false, the specified group only displays its group header and footer.

## Scheduling a Report with Cached Report Bursting

You can schedule a report with cached report bursting as a normal report. However, there are some differences between the formats in which the report is to be published.

### Scheduling to HTML/Page Report Result to Version

When you schedule a task to publish a report with cached report bursting to the HTML and/or Page Report Result formats to the versioning system, the scheduled report depends on the mode which is controlled by the server.enable.cachedreportbursting property in server.properties in `<install_root>\bin`:

* When server.enable.cachedreportbursting=true which is the default, Server will create a report with the report data for all possible users. This enables the report to run with a single query to the DBMS to create reports for all users in one pass. It is similar to [report bursting](https://devnet.logianalytics.com/hc/en-us/articles/4405690677015-Scheduling-Bursting-Reports), however, report bursting does not support the Page Report Result format and it makes a separate physical report for each user and the administrator needs to manually restrict access to the report. When a user views the report using cached report bursting, Server will use the security identifier of the user to restrict access to the data in the report to the specific groups the security identifier is allowed to view. The report is the same as the bursting report in that the user sees only his data, the advantage to the administrator is that there is only one report version to manage. Users can perform interactive actions on scheduled page reports as on other page reports, and Server will recalculate the formulas, summaries, and other similar data based on the privileged data.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)If the report is cached report bursting and RLS/CLS mixed, then when other users other than the user who did the scheduling view the scheduled HTML result, Server displays a blank page.
* When server.enable.cachedreportbursting=false, the scheduled report only contains the data that the user who did the scheduling is allowed to see. This is primarily for compatibility with pre-8.2 versions of Logi Report. In this case, Server does not support "to page report result".

### Scheduling to Email

When you schedule a report with cached report bursting to publish it to email, there is a slight difference. Server supports a multiple mail feature which enables sending the data directly to each user who is authorized to view the report.

Assuming that you have published the catalog and the report to Server, and two users admin and Jennifer both have the permission to view the report. The following procedure shows how to schedule a task to publish a report with cached report bursting to email.

1. Access the Server Console with the user ID admin or Jennifer.
2. Browse to the row that the report is in, put the mouse pointer over the report row and select the **Schedule** button ![Schedule button](https://devnet.logianalytics.com/hc/article_attachments/4420447088151/btn_schdl.gif) on the floating toolbar.
3. In the **General** tab, select the report tab with cached report bursting.
4. In the **Publish** tab, select **To E-mail** and then select **This report has Cached Report Bursting. E-mail the report to each specified user**.
5. Type the subject and select the report format, then select **Finish**.

Server will get the email addresses from the user accounts, and then send the report to admin and Jennifer, with the contents in accord with their access rights to the report.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4420453448599/criticalicon.gif) Before publishing to email, make sure you have specified the email addresses of the users when configuring Logi Report Server. To do this:

1. On the system toolbar of the Server Console, navigate to **Administration** > **Security** > **User**. Server displays the User page.
2. Select the username that you want to edit in the User ID column. Server displays a dialog box.
3. Type the email address of the user in the E-mail text box.

### Scheduling to Other Formats

When scheduling a report with cached report bursting to other formats, the scheduled report only contains the report data that the user who does the schedule is allowed to see. All users will see the same data as the scheduling person.

## Example: Emailing Billing Reports

Sometimes, you may need to send pertinent report data to corresponding email recipients. Server enables you to send a scheduled report to the email addresses accordingly, based on the cached report bursting settings of the report and the user information stored in Logi Report Server (for example, email address information). Therefore, each recipient will only be able to view certain parts of the report data. However, using email information of server users is not reliable, since a user ID that is appropriate for the report does not always exist in Logi Report Server. In cases like this, the mails will not be sent successfully. The best way to resolve this is to use an external email information source by implementing the UserMailList and UserMailListFactory API that Logi Report provides.

Logi Report provides two interfaces for you to retrieve user and email information from a customized source:

* **jet.server.api.UserMailListFactory**  
   Used to get the UserMailList instance implemented by the user.
* **jet.server.api.UserMailList**  
   Used to get email information from a customized source.

You can implement multiple classes of interface UserMailList. Each of them may refer to a particular report. Using the *getInstance()* method in the jet.server.api.UserMailListFactory interface, you can get one implementation of the UserMailList. For more information on these two interfaces, see Logi Report Server API Documentation.

The following is a simple example:

1. Here, there is a Customers table with customer names and their email addresses. You can design a report using this table and others. Then apply cached report bursting for this report, so that later in the server side, you can schedule the report and send pertinent data to different recipients saved in this Customers table.

   ![Customers table](https://devnet.logianalytics.com/hc/article_attachments/4420461537047/scrty_rsc_rpt_crb.gif)
2. In Logi Report Designer, design a report and set cached report bursting for it. In this case, group the report data by Customer Name, and then grant a formula FPageLevel to it. The contents of the formula FPageLevel are:

   `@"Customer Name";`

   This means that only the records of the specified group will be shown at runtime when you enter with different IDs -- Customer Name, in this example.
3. Then in the server side, implement the two interfaces to import the email lists saved in the Customers table. Specifically, implement the jet.server.api.UserMailListFactory interface. The *getInstance()* method should be implemented in this interface to get an instance of jet.server.api.UserMailList. Take the following implementation as a reference, where the implementing class name of the UserMailList interface is formatted as "UserMailList\_" + report + "\_Impl", such as "UserMailList\_Payroll Report\_cls\_Impl".

   ```
   import jet.server.api.*;  
   import jet.cs.util.*;  
     
   public class DemoUserMailListFactoryImpl implements UserMailListFactory {  
       public UserMailList getInstance(ServerInfo serverInfo) {  
           if (serverInfo == null) {  
               return null;  
           }  
           String rpt = null;  
           try {  
               rpt = serverInfo.getTaskProperties().getProperty(APIConst.TAG_REPORT);  
           } catch (RptServerException e) {  
               e.printStackTrace();  
               return null;  
           }  
           rpt = rpt.substring(rpt.lastIndexOf("/") + 1);  
           rpt = rpt.replace('.', '_');  
           rpt = rpt.replace(' ', '_');  
           String clsName = "UserMailList_" + rpt + "_Impl";  
           try {  
               UserMailList mailList = (UserMailList)Class.forName(clsName).newInstance();  
               return mailList;  
           } catch (InstantiationException e1) {  
               e1.printStackTrace();   
           } catch (IllegalAccessException e1) {  
               e1.printStackTrace();  
           } catch (ClassNotFoundException e1) {  
               e1.printStackTrace();  
           }  
           return null;  
       }  
   }
   ```
4. Then implement the jet.server.api.UserMailList interface, which gets the user and email information from the customized data source. The following implementation gets the email list from the Customers table, which contains Customer Name and Customer E-mail columns.

   ```
   import jet.server.api.*;  
   import java.util.*;  
   import java.sql.*;  
     
   public class UserMailList_Payroll Report_cls_Impl implements UserMailList {  
       public static Hashtable userEmails = new Hashtable();  
       private String curRealmName = "defaultRealm";  
     
       public UserMailList_Payroll Report_cls_Impl() {  
           loadData();  
       }  
     
       private void loadData () {  
           try {   
               String jdbcDriver = "sun.jdbc.odbc.JdbcOdbcDriver";  
               DriverManager.registerDriver((Driver) Class.forName(jdbcDriver)  
                   .newInstance());   
               Connection conn = DriverManager  
                   .getConnection("jdbc:odbc:jinfonet4");  
               Statement stmt = conn.createStatement();  
               ResultSet rs = stmt.executeQuery("select * from Customers");  
               String userName = null;  
               String userEmail = null;  
               while(rs.next()) {  
                   userName = rs.getString("Customer Name");  
                   userEmail = rs.getString("Customer Email");  
                   if (userEmail != null) {  
                       userEmails.put(userName, userEmail);  
                   }  
               }  
           } catch(Exception e) {  
                e.printStackTrace();  
           }  
       }  
     
       public java.util.Enumeration getAllMailAddresses(String realmName) {  
           if (realmName.equals(curRealmName)) {  
               return userEmails.elements();  
           } else {  
               return null;  
           }   
       }   
     
       public java.util.Enumeration getGroupMailAddresses (String realmName, String groupName) {  
           if (realmName.equals(curRealmName) && userEmails.containsKey(groupName)) {  
               Vector groupEmails = new Vector();  
               groupEmails.addElement(userEmails.get(groupName));   
               return groupEmails.elements() ;  
           } else {  
               return null;  
           }  
       }   
     
       public java.util.Enumeration getRoleMailAddresses (String realmName, String roleName) {  
        
           if (realmName.equals(curRealmName) && userEmails.containsKey(roleName)) {  
         
               Vector roleEmails = new Vector();  
         
               roleEmails.addElement(userEmails.get(roleName));   
      
               return roleEmails.elements() ;  
          
           } else {  
           
               return null;  
       
           }  
       }  
     
       public java.lang.String getMailAddress(String realmName, String userName) {   
           if (realmName.equals(curRealmName) && userEmails.containsKey(userName)) {   
               return (String)userEmails.get(userName);  
           } else {  
               return null;  
           }  
       }  
   }
   ```
5. Register the preceding classes to Logi Report Server before the server is started.  
   1. Add the parameter `-Dcom.jinfonet.mailListFactory=UserMailListFactoryImplName` to the command line/batch file that starts Logi Report Server, where UserMailListFactoryImplName indicates the implementation of the jet.server.api.UserMailListFactory interface.

      In this case, the parameter should be `-Dcom.jinfonet.mailListFactory=DemoUserMailListFactoryImpl`.
   2. Add the path of the implementation classes to the class path of the command line/batch file.
6. Start Logi Report Server and then publish the report and catalog.
7. Schedule the report, publish to email, select the option **This report has Cached Report Bursting. E-mail the report to each specified user**. Provide the necessary information and then submit the schedule.

The report will be processed and sent to the corresponding recipients with pertinent report data.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690678807-Report-Security-System)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405684016663-Record-Level-and-Column-Level-Security)
