---
title: "Cached Report Bursting"
id: 1500009674901
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674901-Cached-Report-Bursting
updated_at: 2021-07-24T20:53:41Z
---

# Cached Report Bursting

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649982-Report-Security-System)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650002-Record-Level-Security-and-Column-Level-Security)

# Cached Report Bursting

Security in a report is a kind of privileged control. Logi JReport supports cached report bursting which creates a security mechanism for controlling access to the report. By defining which groups of data are available to which users, groups, or roles, report results are created for each user, role and group. When a user accesses the report result, Logi JReport checks the user, group and role of the user and merges the groups of data in the report the user is authorized to see and displays it to the user. Cached report bursting is implemented with these security properties on the group panel: Cascade, Grant, Groups, and Roles. The feature enables different users to view different data groups according to their access privileges. It also applies to nested groups.

This section focuses on how to view and schedule a report that has cached report bursting with Logi JReport Server. For detailed descriptions about setting up cached report bursting in reports, see "Cached Report Bursting" in the *Logi JReport Designer User's Guide*.

Below is a list of the sections covered in this topic:

* [Viewing a Report With Cached Report Bursting](#View)
* [Scheduling a Report With Cached Report Bursting](#Schedule)
* [Example: E-Mailing Billing Reports](#Example)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Viewing a Report With Cached Report Bursting

Since the control of report access is not possible without a user ID, the significance of this function is only apparent after reports have been published to Logi JReport Server and users access it using their Logi JReport User ID (security identifier).

When a client views a report with cached report bursting in Logi JReport Server, the corresponding groups will be displayed according to the security identifier. You can also advanced run reports with cached report bursting in different formats, including Page Report, HTML, PDF, TEXT, Excel, PS, XML and Rich Text Format (this feature does not support the RST and Applet formats).

To view a report with cached report bursting in Logi JReport Server, the report must first be published to the server from Logi JReport Designer. For example, if in Logi JReport Designer, the security for a report that is grouped by the Customer\_Region field has been set as follows:

* The user ID admin has the privilege to view the CA and MN groups of the report.
* The user ID jennifer has the privilege to view the BC group of the report.

Then,

1. Access the Logi JReport Console page via a web browser with the user ID admin.
2. Browse to the report that you are going to view.
3. Select the report name, and you will then be able to view the CA and MN groups of the report.
4. If you log onto Logi JReport Server with the user ID jennifer, you will then only be able to view the BC group.

**Note:** When designing the report in Logi JReport Designer, if the Cascade property is set to be false, the specified group will only display its group header and footer.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Scheduling a Report With Cached Report Bursting

You can schedule a report with cached report bursting as a normal report. However, there are some differences between the formats in which the report is to be published.

### Scheduling to HTML/Page Report Result to version

When you schedule a task to publish a report with cached report bursting to the HTML and/or Page Report Result formats to the versioning system, the scheduled result depends on the mode which is controlled by the property server.enable.cachedreportbursting in server.properties in `<install_root>\bin`:

* When `server.enable.cachedreportbursting=true` which is the default, Logi JReport will create a report result with the report data for all possible users. This allows the report to run with a single query to the DBMS to create the report for all users in one pass. It is similar to [report bursting](https://devnet.logianalytics.com/hc/en-us/articles/1500009674701-Scheduling-a-Task-Containing-a-Bursting-Report), however, report bursting does not support the Page Report Result format and it makes a separate physical report result for each user and the administrator needs to manually restrict access to the result. When a user views the report result using cached report bursting, Logi JReport Server will use the security identifier of the user to restrict access to the data in the report to the specific groups the security identifier is allowed to view. The end result is the same as the bursting report in that the user sees only his data, the advantage to the administrator is there is only one version result to manage. Users can perform interactive actions on the scheduled page report result as on other page report result, and the formulas, summaries and other similar data will be recalculated based on the privileged data.

  **Note:** If the report is cached report bursting and RLS/CLS mixed, then when other users other than the user who did the scheduling view the scheduled HTML result, a blank page is displayed.
* When `server.enable.cachedreportbursting=false`, the scheduled result only contains the data that the user who did the scheduling is allowed to see. This is primarily for compatibility with pre-8.2 versions of Logi JReport. In this case, "to page report result" is not supported.

### Scheduling to E-Mail

When you schedule a report with cached report bursting to publish it to e-mail, there is a slight difference. Logi JReport Server supports a multiple mail feature which enables sending the data result directly to each user who is authorized to view the report.

Assuming that the catalog and the report have been published to Logi JReport Server, and two users admin and jennifer both have the permission to view the report. The following procedure shows how to schedule a task on a report with cached report bursting to be published to e-mail.

1. Access the Logi JReport Console page with user ID admin or jennifer.
2. Browse to the row that the report is in, put the mouse pointer over the report row and select the **Schedule** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920422295/btn_srv_schdl.gif) on the floating toolbar.
3. In the General tab, select the report tab with cached report bursting.
4. In the Publish tab, switch to the **To E-mail** sub tab and then check **This report has Cached Report Bursting. E-mail the report to each specified user**.
5. Type the subject and select the result format, then select **Finish**.

Logi JReport Server will get the e-mail addresses from the user accounts, and then send the report result to admin and jennifer, with the contents in accord with their access right to the report.

**Note:** Before publishing to e-mail, make sure you have input the e-mail addresses of the users when configuring Logi JReport Server. To do this:

1. Access the Logi JReport Administration page, select **Security** on the system toolbar, and then select **User** from the drop-down menu.
2. In the User panel, choose the user name that you want to edit in the User ID column, and then select it. You can then type in the e-mail address of the user.

### Scheduling to Other Formats

When scheduling a report with cached report bursting to other formats, the scheduled result only contains the report data that the user who does the schedule is allowed to see. All users will see the same data as the scheduling person.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Example: E-Mailing Billing Reports

Sometimes, sending pertinent report data to corresponding mail recipients is required. Logi JReport Server allows you to send a scheduled report result to the e-mail addresses accordingly, based on the cached report bursting settings of the report and the user information stored in Logi JReport Server (for example, e-mail address information). Therefore, each recipient will only be able to view certain parts of the report data. However, using e-mail information of server users is not reliable, since a user ID that is appropriate for the report doesn't always exist in Logi JReport Server. In cases like this, the mails will not be sent successfully. The best way to resolve this is to use an external e-mail information source by implementing the UserMailList and UserMailListFactory API that Logi JReport provides.

Logi JReport provides two interfaces for you to retrieve user and e-mail information from a customized source:

* **jet.server.api.UserMailListFactory**  
   Used to get the UserMailList instance implemented by the user.
* **jet.server.api.UserMailList**  
   Used to get e-mail information from a customized source.

You can implement multiple classes of interface UserMailList. Each of them may refer to a particular report. By using the getInstance() method in the jet.server.api.UserMailListFactory interface, you can get one implementation of the UserMailList. For more information on these two interfaces, see Logi JReport Server API Documentation.

The following is a simple example:

1. Here, there is a Customers table with customer names and their e-mail addresses, as illustrated below. You can design a report using this table and others. Then apply cached report bursting for this report, so that later in the server side, you can schedule the report and send pertinent data to different recipients saved in this Customers table.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926662423/scrty_rsc_rpt_crb.gif)
2. In Logi JReport Designer, design a report and set cached report bursting for it. In this case, group the report data by Customer Name, and then grant a formula FPageLevel to it. The content of the formula FPageLevel is as follows:

   `@"Customer Name";`

   This means that only the records of the specified group will be shown at runtime when you enter with different IDs -- Customer Name, in this example.
3. Then in the server side, implement the two interfaces to import the e-mail lists saved in the Customers table. Specifically, implement the jet.server.api.UserMailListFactory interface. The getInstance() method should be implemented in this interface to get an instance of jet.server.api.UserMailList. Take the following implementation as a reference, where the implementing class name of the UserMailList interface is formatted as "UserMailList\_" + report + "\_Impl", such as "UserMailList\_InvoiceReport\_cls\_Impl".

   |  |
   | --- |
   | ``` import jet.server.api.*; import jet.cs.util.*; public class DemoUserMailListFactoryImpl implements UserMailListFactory {     public UserMailList getInstance(ServerInfo serverInfo) {         if (serverInfo == null) {             return null;         }         String rpt = null;         try {             rpt = serverInfo.getTaskProperties().getProperty(APIConst.TAG_REPORT);         } catch (RptServerException e) {             e.printStackTrace();             return null;         }         rpt = rpt.substring(rpt.lastIndexOf("/") + 1);         rpt = rpt.replace('.', '_');         rpt = rpt.replace(' ', '_');         String clsName = "UserMailList_" + rpt + "_Impl";         try {             UserMailList mailList = (UserMailList)Class.forName(clsName).newInstance();             return mailList;         } catch (InstantiationException e1) {             e1.printStackTrace();          } catch (IllegalAccessException e1) {             e1.printStackTrace();         } catch (ClassNotFoundException e1) {             e1.printStackTrace();         }         return null;     } } ``` |
4. Then implement the jet.server.api.UserMailList interface, which gets the user and e-mail information from the customized data source. The following implementation gets the e-mail list from the Customers table, which contains Customer Name and Customer E-mail columns.

   |  |
   | --- |
   | ``` import jet.server.api.*; import java.util.*; import java.sql.*; public class UserMailList_InvoiceReport_cls_Impl implements UserMailList {     public static Hashtable userEmails = new Hashtable();     private String curRealmName = "defaultRealm";     public UserMailList_InvoiceReport_cls_Impl() {         loadData();     }     private void loadData () {         try {              String jdbcDriver = "sun.jdbc.odbc.JdbcOdbcDriver";             DriverManager.registerDriver((Driver) Class.forName(jdbcDriver)                     .newInstance());              Connection conn = DriverManager                     .getConnection("jdbc:odbc:jinfonet4");             Statement stmt = conn.createStatement();             ResultSet rs = stmt.executeQuery("select * from Customers");             String userName = null;             String userEmail = null;             while(rs.next()) {                 userName = rs.getString("Customer Name");                 userEmail = rs.getString("Customer Email");                 if (userEmail != null) {                     userEmails.put(userName, userEmail);                 }             }         } catch(Exception e) {             e.printStackTrace();         }     }     public java.util.Enumeration getAllMailAddresses(String realmName) {         if (realmName.equals(curRealmName)) {             return userEmails.elements();         } else {             return null;         }      }      public java.util.Enumeration getGroupMailAddresses (String realmName, String groupName) {         if (realmName.equals(curRealmName) && userEmails.containsKey(groupName)) {             Vector groupEmails = new Vector();             groupEmails.addElement(userEmails.get(groupName));              return groupEmails.elements() ;         } else {             return null;         }     }      public java.util.Enumeration getRoleMailAddresses (String realmName, String roleName) {         if (realmName.equals(curRealmName) && userEmails.containsKey(roleName)) {             Vector roleEmails = new Vector();             roleEmails.addElement(userEmails.get(roleName));              return roleEmails.elements() ;         } else {             return null;         }     }     public java.lang.String getMailAddress(String realmName, String userName) {          if (realmName.equals(curRealmName) && userEmails.containsKey(userName)) {              return (String)userEmails.get(userName);         } else {             return null;         }     } } ``` |
5. Register the above classes to Logi JReport Server before the server is started.  
   1. Add the parameter -Dcom.jinfonet.mailListFactory=UserMailListFactoryImplName to the command line/batch file that starts Logi JReport Server, where UserMailListFactoryImplName indicates the implementation of the jet.server.api.UserMailListFactory interface.

      In this case, the parameter should be -Dcom.jinfonet.mailListFactory=DemoUserMailListFactoryImpl.
   2. Add the path of the implementation classes to the class path of the command line/batch file.
6. Start Logi JReport Server and then publish the report and catalog.
7. Schedule the report, publish to e-mail, check the option **This report has Cached Report Bursting. E-mail the report to each specified user**. Provide the necessary information and then submit the schedule.

The report will be processed and sent to the corresponding recipients with pertinent report data.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649982-Report-Security-System)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650002-Record-Level-Security-and-Column-Level-Security)
