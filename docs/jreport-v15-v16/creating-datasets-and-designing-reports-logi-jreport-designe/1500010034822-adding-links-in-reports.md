---
title: "Adding Links in Reports"
id: 1500010034822
section: "Creating Datasets and Designing Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports
updated_at: 2021-07-24T10:37:44Z
---

# Adding Links in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070861-Filtering-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034802-Changing-the-Display-Type-of-Objects-in-Reports)

# Adding Links in Reports

A report can be linked with other reports, locations specified by URLs, e-mail addresses or Blob data type fields, so that the report users can gain access to the linked targets by selecting the corresponding trigger objects in the report.

In a report, the following objects can be used as the trigger objects of links: [labels](https://devnet.logianalytics.com/hc/en-us/articles/1500010029102-Labels), data fields ([DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500010063761-DBFields), [summary fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010029262-Summary-Fields-), [formula fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010063801-Formula-Fields), [parameter fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010029182-Parameter-Fields)), [special fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010029242-Special-Fields), [images](https://devnet.logianalytics.com/hc/en-us/articles/1500010029062-Images), areas in [shape maps](https://devnet.logianalytics.com/hc/en-us/articles/1500010063881-Shape-Maps), and the category/series axis, legend and data markers in [charts](https://devnet.logianalytics.com/hc/en-us/articles/1500010028702-Charts). You can create either simple links or conditional links in a report. With conditional link, different targets can be loaded based on different conditions.

Below is a list of the sections covered in this topic:

* [Adding Links in a Report](#Add) 
  + [Linking to Another Report](#Report)
  + [Linking to a Detail Report](#Detail)
  + [Linking to a URL](#URL)
  + [Linking to an E-mail](#Mail)
  + [Linking to a Blob Data Type Field](#Content)

* [Editing the Links in a Report](#Edit)
* [Removing Links from a Report](#Remove)
* [Example of Adding a Conditional Link](#Example)

## Adding Links in a Report

**To add a simple link in a report:**

1. Right-click the object used as the trigger object of the link and select **Link** on the shortcut menu.
2. In the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500010066921-Insert-Link-Dialog) dialog, select the target to which the trigger object will be linked: [Report](#Report), [Master/Detail Report](#Detail), [URL](#URL), [E-mail](#Mail) or [Content](#Content) from the Link Type drop-down list.
3. Specify the options for the link target.
4. Select **OK** to create the link.

**To add a conditional link in a report:**

1. Right-click the object used as the trigger object of the link and select **Link** on the shortcut menu.
2. In the Insert Link dialog, check the **Conditional Link** checkbox.

   ![Insert Link dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909124503/rpt_link_cndtnl.gif)
3. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) above the conditions box. The [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500010065521-Edit-Conditions-Dialog) dialog appears.

   ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901131543/edtcndtn.gif)
4. Select the **Add Condition** button to add a condition line.
5. From the field drop-down list, select the field on which the condition will be based.
6. Choose the operator with which to compose the condition expression from the operator drop-down list.
7. From the value drop-down list, specify the value of how to build the condition. You can also type in the value manually.
8. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
9. Select **OK** to save the condition.

   The newly added condition is then displayed and highlighted in the conditions box in the Insert Link dialog.
10. From the Link Type drop-down, select the target to which the trigger object will be linked under this condition: [Report](#Report), [Master/Detail Report](#Detail), [URL](#URL), [E-mail](#Mail), or [Content](#Content), then specify the options for the link target.
11. Repeat the above steps to add more conditions and define the target for each condition.

    To edit a condition, select the condition, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404901116439/btn_edit.gif), then edit it in the Edit Conditions dialog.

    To adjust the priority of the conditions, select a condition and select the ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404909121047/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909121303/btn_mvdwn.gif) button.

    To remove a condition, select the condition and then select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404909120791/btn_rmv.gif).
12. Check the **Others** checkbox and define a target to which the trigger object will be linked when none of the conditions you have specified are met.
13. Select **OK** to create the conditional link. See [Example of binding a conditional link](#Example) for more information.

**Notes:**

* Conditional links are not supported on objects the parents of which are not bound with datasets.
* By default, the link action has the highest select priority at runtime. You can change the priority by setting the report's [Select Priority](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Priority) property.

### Linking to Another Report

In most cases, your reports are affiliated with one another, with each report emphasizing one or more aspects of a bigger picture. Relationships can be set up for users to browse from one report to another through the relationship "channels" created. You can achieve an inter-report relationship network by setting up the link conditions between two reports in the same catalog. Then when you view the primary report at runtime, you can gain access to the linked report by selecting the trigger object.

**To make a report linked to another report:**

1. In the Insert Link dialog, select **Report** as the link type.

   ![Insert Link dialog - Report](https://devnet.logianalytics.com/hc/article_attachments/4404901131799/instlnk_rpt.gif)
2. If the primary report is a page report, select the **Browse** button next to the Report text box to specify the page report in the same catalog that contains the report tab you want as the linked report. Then select the report tab name from the Report Tab drop-down list.

   If the primary report is a web report or a library component, select the **Browse** button to specify the web report in the same catalog that you want as the linked report.
3. From the Target drop-down list, select where the linked report will be loaded.

   The Target property works when the link is triggered in Page Report Studio or Web Report Studio. When the link is triggered in JDashboard, except for Same Frame, all the other targets are treated as New Window.
4. Select the **More** button to display more options for setting the link.
5. In the Filter tab, select the button **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** above the Components box. In the Choose Component dialog, add the data components in the linked report you want to be interlinked with the primary report. If the required data components use different datasets, you need to add them respectively, however, as long as the components are based on the same dataset, you can add them all at the same time.

   ![Chosse Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909124759/rpt_link.gif)
6. Specify the filter conditions based on how the link relationship between the primary report and the selected data components in the linked report are set up.
   1. Select a component from the Components box.
   2. Select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** above the Field Conditions box and a condition line is added.
   3. Select the desired field of the primary report from the drop-down list in the Fields (Primary) column.
   4. Choose an operator from the drop-down list in the OP column.
   5. Specify the field/formula of the linked report from the drop-down list in the Fields (Linked) column. All fields in the linked report of the same value type as the selected primary report field are available in the drop-down list.
   6. If necessary, you can specify more conditions by selecting the button **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** and then specifying the primary report field, the operator, and the corresponding field in the linked report. Note that the relationship between these conditions is AND, which means that Logi JReport will fetch linked report data which meets all of the conditions.
   7. Repeat the above steps to set link conditions between the primary report and other components in the linked report.
7. Specify whether to apply the on-screen filters (filters created via [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500010064061-Using-Advanced-Web-Controls#Filter)) in the primary report to the selected data components of the linked report.
   1. Select the data component to which you want to apply the on-screen filters from the Components box.
   2. Check **Pass on-screen filters to the linked components**.
   3. If the trigger data component in the primary report and the selected data component in the linked report use different datasets, you need to select **Mapping Table** to define the mapping relationship based on which the on-screen filters in the primary report are passed to the linked report in the [Mapping Table](https://devnet.logianalytics.com/hc/en-us/articles/1500010067161-Mapping-Table-Dialog) dialog.

      ![Mapping Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909125015/mptbl.gif)
   4. Select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** to add a mapping line.
   5. Select the field that is bound with a filter control in the primary report from the drop-down list in the Fields (Primary) column.
   6. All available fields in the linked report of the same value type as the selected filter control field are listed in the drop-down list in the Fields (Linked) column. Select a field whose values are the same as those of the filter control field.

      A mapping relationship is now set up. Then when the link is triggered, the corresponding on-screen filter in the primary report will be applied on the selected linked report field.
   7. Add more mapping lines and define the mapping relationship between the filter control fields in the primary report with appropriate fields in the linked report.
   8. Select **OK** to go back to the Insert Link dialog.
   9. Repeat the above steps to apply the on-screen filters in the primary report to other data components in the linked report.
8. From the Default Linked Component drop-down list, select the data component that is displayed by default in the linked report when the link is triggered in exported result. For example, a linked report contains a chart and a table and the table is specified as the default linked component. When you export the primary report to PDF with linked report and trigger the link in the PDF result file, the page that contains the table will be displayed by default. You can scroll to view the chart.
9. If the linked report contains one or more parameters, the Parameters tab is activated. In this tab, you can assign fields of the primary report to parameters of the linked report to use the field values for the parameters automatically when running the linked report from the link. If the selected field is a parameter field, you can choose Current Value to use its most recently specified value or Initial Value to use its original value for the parameter in the linked report.

   ![Insert Link dialog - Report - Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404909125271/rpt_link_rptprm.gif)
10. If you would like the values of the filter objects like filter controls in the primary report to be passed to filter objects in the linked report, go to the **Advanced** tab to set up the relationship between the filter objects as follows (not available to library component):

    ![Insert Link dialog - Report - Advanced](https://devnet.logianalytics.com/hc/article_attachments/4404909125527/rpt_link_rptadvcd.gif)

    1. Select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** to add a line.
    2. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the Primary Report Property/Object column, then in the Select Value dialog select a filter object in the primary report and select **OK**.

       ![Select Value dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909125783/rpt_link_slctvlu.gif)

       All the objects in the primary report are listed in the Select Value dialog but only filter controls can be selected from the object tree.
    3. In the Linked Report Property/Object column, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) to select a filter object in the linked report. You need to make sure that values of the filter object in the primary report can be applied to the filter object in the linked report in the same line.
    4. Follow the above steps to set up the relationship between more filter objects in the primary report and linked report.
11. Check **Pass style group information down to the linked report** to transfer style information from the primary report to the linked report, so that the style of the primary report will apply to the linked report.
12. Select **OK** to apply the settings.

Then, when you run the primary report at server runtime and select the trigger object, you will find that the linked report is displayed according to the specified link conditions. You can also trigger the link when viewing the report in HTML, PDF or Excel format if you check the Run Linked Report option when specifying the settings of the corresponding format.

**Notes:**

* A page report can only be linked with another page report, and a web report with another web report. For a library component, it can only be linked with a web report.
* When linking reports, you need to avoid link loops. For example, if you have linked report A to report B, then you cannot link report B back to report A again.
* The conditions specified in the Filter tab are used for filtering when the link is triggered at server runtime, that is, only the data that meet the conditions in the linked report will be displayed. However, when the link is triggered in HTML, PDF or Excel result, the conditions are used for setting up search criteria between the two linked reports, which means after you select the trigger object in the primary report, the pages containing the data that meet the conditions in the linked report will be displayed.

### Linking to a Detail Report

Reports in the same catalog can be joined together in order to create a master/detail report group. Usually, the master report holds comprehensive data, while the detail reports hold related detailed information. A detail report can also be the master report of another report. In this way, you can set up more pairs of master/detail reports, where many reports are joined together, eventually leading to the formation of a report chain. Then, when you view the master report at runtime, you can gain access to the detail report by selecting a trigger, which is an object defined in the master report to load a detail report. However, in a master/detail report group, crosstab reports cannot be used as the master.

The main advantage of using a master/detail relationship is the user can browse though the details by selecting next detail and previous detail without going back to the master report. When the user does go back to the master report they will see the master report based on the last detail report that was viewed.

The Master/Detail Report link type is supported in page reports that are created using query resources only.

**To make a report linked to a detail report:**

1. In the Insert Link dialog, select **Master/Detail Report** as the link type.

   ![Insert Link dialog - Mater/Detail Report](https://devnet.logianalytics.com/hc/article_attachments/4404901132055/instlnk_dtl.gif)
2. Select the **Browse** button next to the Report text box to specify the report in the same catalog which contains the report tab you want for the detail report, and then select the report tab name from the Report Tab drop-down list.
3. Select the **Browse** button beside the Component field. In the Choose Component dialog, specify which data component in the detail report you want to be interlinked with the master report with conditions. You can select more than one data component as long as the components are based on the same dataset.
4. From the Target drop-down list, select where the detail report will be loaded.
5. Specify the join relationship between the master report and detail report in the Anchor section. The join can only have one condition. For example, the join can be: (Detail Report) Product ID = (Master Report) Product ID. The join condition should be as:

   `(Detail RPT) expression1 operator (Master RPT) expresion2`

   To make the join more meaningful, expression1 should be a column or record level formula in the GROUP section of a component in the detail report; and expression2 should be a column or record level formula in the DETAIL section of a component in the master report. This is because generally the master report is used to present comprehensive data, and the detail report to present more detailed information. To specify the join condition,

   1. Select a field/formula from the Column in Detail Report drop-down list. If this list does not offer the required field/formula, then you will need to specify the component with the data source that contains the specific field/formula. To do this, specify the component by selecting the Browse button besides the Component field.
   2. Choose the operator from the Operator drop-down list.
   3. Specify the field/formula of the master report from the Column in Master Report drop-down list. This field/formula should be of the same data type as the selected field/formula of the detail report.
6. Select the **More** button to display more options for setting the link.
7. In the Conditions tab, specify the filter conditions between the master report and the detail report.
   1. Select the add button **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** above the Field Conditions box and a condition line is added.
   2. Select the desired field of the master report from the Fields (MasterReport) drop-down list.
   3. Choose an operator from the drop-down list in the OP column.
   4. Specify the field/formula of the detail report from the drop-down list in the Fields (DetailReport) column. All fields in the detail report of the same value type as the selected primary report field are available in the drop-down list.
   5. If necessary, you can specify more conditions by selecting the button **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** and then specifying the master report field, the operator, and the corresponding field in the detail report. You can use the More column to specify the relationship between conditions to be AND or OR.
8. If there is at least one parameter applied in the filters of the queries that the detail report uses, the Parameters tab is enabled. In this tab, you can assign field of the master report to parameter of the detail report. Then when running the detail report from the link, the field value of the master report will be assigned to the parameter automatically.

   ![Insert Link dialog - Mater/Detail Report - Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404901132311/rpt_link_dtlprm.gif)
9. If both reports use the same encoding and DB settings, you should check the option **Use the same encoding and DB settings for the detail report as that of the master report**. If this option is not checked, when the detail report is triggered at runtime, you will be prompted to specify the encoding and DB settings for the detail report.
10. Select **OK** to confirm.

After a set of master/detail reports have been defined in Logi JReport Designer and published to Logi JReport Server, they can be viewed in Page Report Studio. The detail report supports all the page report operations, such as sort, filter, drill, and search.

**Notes:**

* The join and filter conditions work together. If you want to set a single condition, you can use join (anchor). If you want to set a group of conditions, you can use the filter conditions together with a join condition. The relationship between the join and filter conditions is "Join condition AND (filter conditions)".
* If you specify to load the detail report in a new browser window, the detail report will be opened independently when you select the trigger in Page Report Studio. That is to say, the join and filter conditions you have set between the master report and detail report will not be applied.

### Linking to a URL

1. In the Insert Link dialog, select **URL** as the link type.

   ![Insert Link dialog - URL](https://devnet.logianalytics.com/hc/article_attachments/4404909126039/instlnk_url.gif)
2. Enter the URL in the Hyperlink text box directly. If needed, select the **Add Dynamic Field** button to open the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010067801-Select-Field-Dialog) dialog to insert a field into the URL to compose a dynamic URL.

   ![Select Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909126295/slctfld.gif)

   For example, you can compose a URL as follows: type in **http://www.google.com/search?q=** into the Hyperlink text box, then select the **Add Dynamic Field** button to insert the field Country at the end of the URL. You can then select the trigger object to open a specific URL that directs to a specific country.
3. Specify the frame from the Target drop-down list.

   The Target property works when the link is triggered in Page Report Studio or Web Report Studio. When the link is triggered in JDashboard, except for Same Frame, all the other targets are treated as New Window.
4. When you link a trigger object in a web report table to a URL, you can select the **IE Navigate2 Flags** button to use the IE Navigate2 method and its flags to control the behavior of IE when loading the URL in Internet Explorer. Choose one or more flags as needed.
5. Select **OK** to set up the link.

Then, when you run the report at server runtime, or view it in HTML, PDF or Excel format, you can select the trigger object to open the URL.

### Linking to an E-mail

1. In the Insert Link dialog, select **E-mail** as the link type.

   ![Insert Link dialog - E-mail](https://devnet.logianalytics.com/hc/article_attachments/4404901132567/instlnk_mail.gif)
2. Enter the [e-mail address](#MailSyntax) in the Hyperlink text box directly. If needed, select the **Add Dynamic Field** button to to open the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500010067801-Select-Field-Dialog) dialog to insert a field into the e-mail address to compose a dynamic e-mail address.
3. Select **OK** to set up the link.

Then, when you run the report at server runtime, or view it in HTML, PDF or Excel format, you can select the trigger object to open the e-mail with the information specified in the Hyperlink box. You can further customize the e-mail and send it.

**E-mail address syntax**

When composing the e-mail address, you need to follow the syntax: `sAddress[sHeaders]`. Below are details about the syntax.

* **sAddress**One or more valid e-mail addresses separated by a semicolon. You must use Internet-safe characters, such as %20 for the space character.
* **sHeaders**Optional. One or more name-value pairs. The first pair should be prefixed by a "?" and any additional pairs should be prefixed by a "&". The name can be one of the following strings:
  + **CC**  
     Addresses to be included in the "cc" (carbon copy) section of the message.
  + **BCC**  
     Addresses to be included in the "bcc" (blind carbon copy) section of the message.
  + **subject**  
     Text to appear in the subject line of the message.
  + **body**  
     Text to appear in the body of the message.

Hyperlink examples:

* `user@example.com`
* `user1@example.com;user2@example.com`
* `Customer Name@jinfonet.com`, here Customer Name is a field name. Note that, fields can work in the hyperlink only when they are inserted via the Add Dynamic Field option.
* `salesmanager@Country.jinfonet.com`, here Country is a field name.
* `user@example.com?CC=user1@example.com&BCC=user2@example.com&subject=TestLinkToEmail&Body=Version%20x.x%0D%0A%0D%0ATest%20Link%20To%20E-mail`

  Here is the e-mail result:

  ![Label Linked Mail](https://devnet.logianalytics.com/hc/article_attachments/4404901132823/rpt_link_mail.gif)

### Linking to a Blob Data Type Field

When a report is linked with Blob data type fields, the Blob data type fields will be bound to the trigger objects of the links and displayed as hyperlinks, and you can download the Blob content by selecting the hyperlinks in the report.

In Logi JReport, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, Longvarbinary and so on.

Page reports created using business views cannot be linked to Blob data type fields.

**To make a report linked to a Blob data type field:**

1. In the Insert Link dialog, select **Content** as the link type.

   ![Insert Link dialog - Content](https://devnet.logianalytics.com/hc/article_attachments/4404901133079/instlnk_cntnt.gif)
2. From the Query drop-down list, select the query (for page report) or business view (for web report and library component) which contains the required Blob data type field. Only queries/business views that come from the same data source connection as the query/business view used by the current report are available in the drop-down list.
3. From the Content Type drop-down list, specify the content type for the Blob type data. You can also select the button ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) to bind the content type with a field in the selected query/business view, or [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500010033202-Using-Formulas-to-Control-Object-Properties) the type.
4. In the File Name text box, specify a file name for the linked Blob type data. You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404901133335/btn_fmla.gif) to select a field or formula to control the name.
5. From the Content drop-down list, choose a Blob data type field in the selected query/business view.
6. Select the **More** button to display more link options.
7. In the Filter tab, specify the filter conditions between the query/business view used by the current report and the query/business view that contains the linked Blob content as follows:
   1. Select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** above the Field Conditions box and a condition line is added.
   2. Select the desired field of the query/business view used by the current report from the Fields (Primary) drop-down list.
   3. Choose an operator from the drop-down list in the OP column.
   4. Specify the field/formula of the query/business view that contains the linked Blob content from the drop-down list in the Fields (Linked) column. All fields that are of the same data type as the selected field in the Fields (Primary) column are available in the drop-down list.
   5. If necessary, you can specify more conditions by selecting the button **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif)** and then specifying the fields and operators accordingly. Note that the relationship between these link conditions is AND, which means that Logi JReport will fetch the linked Blob type data which meets all of the conditions.
8. If the query/business view that contains the linked Blob content uses parameters, the Parameters tab will be enabled. In this tab, you can assign fields of the query/business view used by the current report to the parameters. Then, when accessing the Blob type data from the link, the field values will be assigned to the parameters automatically.
9. Select **OK** to apply the settings.

Then, when you run the report at server runtime, or view it in HTML, PDF or Excel format, you can select the trigger object to download the Blob content according to the specified conditions.

## Editing the Links in a Report

You can edit the links added in a report at any time. To do this, right-click the trigger object of the link you want to edit and select **Edit Link** from the shortcut menu. Then in the Edit Link dialog, [redefine the link](#Add).

See also the [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500010030482-Edit-Link-for-Page-Report-Dialog) dialog for additional information about options in the dialogs.

## Removing Links from a Report

To remove a link from a report, right-click the trigger object of the link and select **Remove Link** from the shortcut menu.

## Example of Adding a Conditional Link

This example shows the usage of conditional link and dynamic field.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a summary table in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500010063941-Inserting-Tables-in-a-Report-#BV) which is based on WorldWideSalesBV in Data Source 1 of the catalog, shows Product Name, Total Sales and Total Cost, and uses the Basic style.
4. Right-click on the **Product Name** field in the second group header panel and then select **Link** from the shortcut menu.

   ![Insert a Link for the Label](https://devnet.logianalytics.com/hc/article_attachments/4404901133591/rpt_link1.gif)
5. In the Insert Link dialog, check the **Conditional Link** checkbox.
6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) to define a condition in the Edit Conditions dialog as follows.

   ![Add Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404901133847/rpt_link2.gif)
7. We will make the field linked to a URL target based on the condition. From the Link Type drop-down list, select **URL**. In the Message dialog, select **Yes**.
8. In the Hyperlink text box, type in **http://www.google.com/search?q=** and then select the **Add Dynamic Field** button to insert the field Product Name at the end of the URL.

   ![Insert Link](https://devnet.logianalytics.com/hc/article_attachments/4404901134103/rpt_link3.gif)
9. For the product names other than Blue Mountain and Breakfast Blend, we will make them linked to an e-mail target. Check the **Others** checkbox. A condition named Others will be created.
10. From the Link Type drop-down list, select **E-mail**. In the Message dialog, select **Yes**.
11. In the Hyperlink text box, type in **@example.com** and then select the **Add Dynamic Field** button to insert the field Product Name right ahead of @.

    ![Insert Link](https://devnet.logianalytics.com/hc/article_attachments/4404901134359/rpt_link4.gif)
12. Select **OK** in the Insert Link dialog.
13. Select **File** > **Save** to save the report and select **View** > **Preview As** > **Web Report Result** to view the report result in Web Report Studio. We can select the product names in the table to trigger the link.
14. Select **Blue Mountain** and a Google search result page with the key text Blue Mountain will be displayed.

    ![Google Search Result](https://devnet.logianalytics.com/hc/article_attachments/4404901134615/rpt_link6.gif)
15. Select **Breakfast Blend** and a Google search result page with the key text Breakfast Blend will be displayed.
16. Select another product name other than Blue Mountain and Breakfast Blend to send an e-mail.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010070861-Filtering-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034802-Changing-the-Display-Type-of-Objects-in-Reports)
