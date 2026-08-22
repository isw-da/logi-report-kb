---
title: "Binding Links to Objects"
id: 1500009650322
section: "Web Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009650322-Binding-Links-to-Objects
updated_at: 2021-07-24T20:53:35Z
---

# Binding Links to Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-)

# Binding Links to Objects

You can bind links to labels, images, DBFields, formula fields, parameter fields, special fields, and the category (X) axis labels, legend labels, or data markers of charts. The link can either be a simple link or a conditional link. With conditional link, different targets can be loaded based on different conditions. However, conditional link is not supported on independent objects placed into a component that is not bound to a dataset, for example in a tabular cell.

**To bind a simple link to an object:**

1. Right-select the object and select **Link** on the shortcut menu to display the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009672201-Insert-Link) dialog.
2. From the Link Type drop-down list, select the target to which the object will be linked: [Report](#Report), [URL](#URL), [E-mail](#Mail) or [Content](#Content).
3. Specify the options for the link target.
4. When done, select **OK** to create the link.

**To bind a conditional link to an object:**

1. Right-select the object and select **Link** from the shortcut menu to display the Insert Link dialog.
2. Check the **Conditional Link** checkbox.
3. Select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to open the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009647222-Edit-Conditions) dialog to define a condition using either [simple expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters#Simple) or [complex expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters#Complex) according to your requirements.

   The newly added condition will then be displayed and highlighted in the conditions box in the Insert Link dialog.
4. From the Link Type drop-down list, select the target to which the object will be linked under this condition: [Report](#Report), [URL](#URL), [E-mail](#Mail) or [Content](#Content), then specify the options for the link target.
5. Repeat the above steps to add more conditions and define the link target for each condition.

   To edit a condition, select the condition in the Condition box, then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385303/btn_wbrpt_edit.gif). In the Edit Conditions dialog, edit the expressions as required.

   To remove a condition and the corresponding format, select the condition in the Condition box and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920361623/btn_delete.gif).

   To adjust the priority of a condition, select the condition in the Condition box and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404926639255/btn_mvup.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404920381207/btn_mvdown.gif).
6. When done, select **OK** to finish defining the conditional link.

For an illustrated example, see [Example of binding a conditional link](#Example).

Once a link is added to an object, you can then open the link, further edit the link settings or remove it.

* To open the link, switch Web Report Studio to View Mode, then right-click the trigger object and select **Show Linked Target** from the shortcut menu. If the web report is created in Web Report Studio, you can also directly select the trigger object to open the link, while for a web report created in Logi JReport Designer, whether you can do this depends on the report's Select Priority property setting at report design time. If the priority of the [go-down](https://devnet.logianalytics.com/hc/en-us/articles/1500009650302-Going-Through-the-Report-Data) action is specified the highest and the trigger object is in a hierarchy, you can use a select on the object to open the link only after you have gone down to the lowest level of the hierarchy.
* To edit a link, right-click the object and select **Edit Link** from the shortcut menu. In the [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009671701-Edit-Link) dialog, edit the link according to your requirement.
* To remove a link from an object, right-click the object and select **Remove Link** on the shortcut menu. In the warning message dialog, select **Yes** to confirm the removal.

Below is a list of the sections covered in this topic:

* [Linking a Report to Another Report](#Report)
* [Linking to a URL](#URL)
* [Linking to an E-Mail](#Mail)
* [Linking to a Blob Data Type Field](#Content)
* [Example of Binding a Conditional Link](#Example)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Linking a Report to Another Report

You can make a report linked to another report, then when you select the trigger object in the primary report, you will be able to jump to the linked report to obtain information about the trigger object.

1. In the Insert Link dialog, select **Report** as the link type.

   ![Link to Report](https://devnet.logianalytics.com/hc/article_attachments/4404926642967/insrtlnk_rpt.gif)
2. Select the **Browse** button beside the Report text field to specify the target web report you want as the linked report.
3. Specifies the window or frame in which to load the linked report from the Target drop-down list.
4. Select the **More** button to display more options for setting the link.
5. In the Filter tab, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) above the Components box to specify which components in the linked report will be interlinked with the primary report.
6. Specify the conditions based on which the link relationship between the primary report and the selected components in the linked report is set up.
   1. Select a component in the Components box.
   2. Select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) above the Field Conditions box and a condition line is added.
   3. Select a field from the drop-down list in the Fields(Primary) column.
   4. Choose an operator from the drop-down list in the OP column. The operator can be "=", "<>", "<", ">", "<=", ">=", or "IN".
   5. Specify the field of the linked report from the drop-down list in the Fields(LinkedReport) column. All fields in the linked report of the same value type as the selected primary report field will be available.
   6. If necessary, you can specify more conditions by selecting the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) and then specifying the primary report field, the operator, and the corresponding field in the linked report. Note that the relationship between these conditions is AND, which means that Logi JReport will fetch linked report data which meets all of the conditions.
   7. Repeat the above steps to set link conditions between the primary report and other components in the linked report.
7. Specify whether to apply the on-screen filters (namely, the filters created via the [Filter panel](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters#Panel) and [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009650282-Applying-Filters#Control)) in the primary report to the selected components in the linked report.
   1. Select the component to which you want to apply the filters from the Components box.
   2. Check **Pass on-screen filters to the linked components**.
   3. If the trigger component in the primary report and the selected component in the linked report use different business views, you need to select **Mapping Table** to define the mapping relationship based on which the on-screen filters in the primary report are passed to the linked report in the [Mapping Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009672281-Mapping-Table) dialog.

      ![Mapping Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404920385559/mptbl.gif)
   4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) above to add a mapping line.
   5. Select the field that is bound with an on-screen filter in the primary report from the drop-down list in the Fields (Primary) column.
   6. All available fields in the linked report of the same value type as the selected on-screen filter field are listed in the drop-down list in the Fields (Linked) column. Select a field whose values are the same as those of the on-screen filter field.

      A mapping relationship is now set up. Then when the link is triggered, the corresponding on-screen filter in the primary report will be applied on the selected linked report field.
   7. Add more mapping lines and define the mapping relationship between the on-screen filter fields in the primary report with appropriate fields in the linked report.
   8. Select **OK** to go back to the Insert Link dialog.
   9. Repeat the above steps to apply the on-screen filters in the primary report to other components in the linked report.
8. From the Default Linked Component drop-down list, select the component that is displayed by default in the linked report when the link is triggered in exported result.

   For example, a linked report contains a chart and a table and the table is specified as the default linked component. When you export the primary report to PDF with linked report and trigger the link in the PDF result file, the page that contains the table will be displayed by default. You can scroll to view the chart.
9. If the linked report uses parameters, go to the Parameters tab, the Target Report Parameters box lists the parameters of the linked report. You can assign fields of the primary report to the parameters. Then, when running the linked report from the link, the field values of the primary report will be assigned to the parameters automatically.
10. If you would like the values of the filter objects like filter controls in the primary report to be passed to filter objects in the linked report, go to the **Advanced** tab to set up the relationship between the filter objects as follows:
    1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) to add a line.
    2. In the Primary Report Property/Object column, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385815/btn_chsr.gif) to select a filter object in the primary report in the [Select Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009672561-Select-Value) dialog and select **OK**.
    3. In the Linked Report Property/Object column, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385815/btn_chsr.gif) to select a filter object in the linked report in the Select Value dialog and select **OK**. You need to make sure that values of the filter object in the primary report can be applied to the filter object in the linked report in the same line.
    4. Follow the above steps to set up the relationship between more filter objects.
11. Select **OK** to apply the settings.

You can then trigger the link to open the linked report which will be displayed according to the specified link conditions. The link is also available when the primary report is opened in HTML, PDF or Excel format with the option Run Linked Report being selected.

If the linked report is opened in the same frame as the primary report in Web Report Studio, you can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920386327/btn_back.gif) on the toolbar to go back to the primary report. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920386711/btn_goto.gif) next to ![](https://devnet.logianalytics.com/hc/article_attachments/4404920386327/btn_back.gif) and you will get a drop-down list which lists the original report and the linked targets you have just visited within the link chain. The item checked on the drop-down list is the currently opened page. Select an unchecked item and you will be directed to that target.

**Notes:**

* When linking reports, you need to avoid link loops. For example, if you have linked report A to report B, then you cannot link report B back to report A again.
* The conditions specified in the Filter tab are used for filtering when the link is triggered at server runtime, that is, only the data that meet the conditions in the linked report will be displayed. However, when the link is triggered in HTML, PDF or Excel result, the conditions are used for setting up search criteria between the two linked reports, which means after you select the trigger object  in the primary report, the pages containing the data that meet the conditions in the linked report will be displayed.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Linking to a URL

1. In the Insert Link dialog, select **URL** as the link type.

   ![Link to URL](https://devnet.logianalytics.com/hc/article_attachments/4404920387095/insrtlnk_url.gif)
2. Enter the URL in the Hyperlink text box directly. If needed, select the **Add Dynamic Field** button to insert a field into the URL to compose a dynamic URL.

   For example, suppose the link is defined on the Country DBfield and you compose the URL as follows: type in **http://www.google.com/search?q=** into the Hyperlink text box, then select the **Add Dynamic Field** button to insert the field Country at the end of the URL. You can then select any country value to open a specific URL that directs to a specific country.
3. Specify the frame from the Target drop-down list.

   The Target property works when the link is triggered in Web Report Studio. When the link is triggered in JDashboard, except for Same Frame, all the other targets are treated as New Window.
4. Select **OK** to set up the link.

You can then trigger the link to open the URL. The link is also available when the report is opened in HTML, PDF, or Excel format.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Linking to an E-Mail

1. In the Insert Link dialog, select **E-mail** as the link type.

   ![Link to E-mail](https://devnet.logianalytics.com/hc/article_attachments/4404920387351/insrtlnk_mal.gif)
2. Enter the [e-mail address](#MailSyntax) in the Hyperlink text box directly. If needed, select the **Add Dynamic Field** button to insert a field into the e-mail address to compose a dynamic e-mail address.
3. Select **OK** to set up the link.

You can then trigger the link to open the e-mail with the information specified in the Hyperlink box. You can further customize the e-mail and send it. The link is also available when the report is opened in HTML, PDF, or Excel format.

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

Here are some examples:

* `user@example.com`
* `user1@example.com;user2@example.com`
* `${Customer Name}@jinfonet.com`, here ${Customer Name} is a field name. Note that, fields can work in the hyperlink only when they are inserted via the Add Dynamic Field option.
* `salesmanager@${Country}.jinfonet.com`, here ${Country} is a field name.
* `user@example.com?CC=user1@example.com&BCC=user2@example.com&subject=TestLinkToEmail&Body=Version%20x.x%0D%0A%0D%0ATest%20Link%20To%20E-mail`

  Here is the e-mail result:

  ![E-mail Result](https://devnet.logianalytics.com/hc/article_attachments/4404926643735/wbrpt_edt_link_mail.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Linking to a Blob Data Type Field

You can make an object linked with a Blob data type field. The Blob data type field will then be bound to the object and displayed as a hyperlink. You can download the Blob content by selecting this hyperlink.

In Logi JReport, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, Longvarbinary, and so on.

**To make an object linked to a Blob data type field:**

1. In the Insert Link dialog, select **Content** as the link type.

   ![Link to Content](https://devnet.logianalytics.com/hc/article_attachments/4404920387607/insrtlnk_cntnt.gif)
2. From the Query drop-down list, select the business view which contains the required Blob data type field. Only query based business views that come from the same data source connection as the business view the current report uses are available in the drop-down list.
3. From the Content Type drop-down list, specify the content type for the Blob type data. You can also select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) to bind it with a string type business view element or a record level pass one formula in the selected business view, or with a dynamic formula in the current report.
4. In the File Name text field, specify a file name for the linked Blob type data. You can also select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920382743/btn_wbrpt_fmla.gif) to specify a string type business view element or a record level pass one formula in the selected business view to control the file name.
5. From the Content drop-down list, choose a Blob data type field in the selected business view.
6. Select the **More** button to display more link options.
7. In the Filter tab, specify the filter conditions between the business view used by the current report and the business view that contains the linked Blob content as follows:
   1. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) above the Field Conditions box and a condition line is added.
   2. Select the desired field of the business view used by the current report from the Fields(Primary) drop-down list.
   3. Choose an operator from the drop-down list in the OP column.
   4. Specify the field/formula of the business view that contains the linked Blob content from the drop-down list in the Fields (Linked) column. All fields that are of the same data type as the selected field in the Fields(Primary) column are available in the drop-down list.
   5. If necessary, you can specify more conditions by selecting the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif) and then specifying the fields and operators accordingly. Note that the relationship between these link conditions is AND, which means that Logi JReport will fetch the linked Blob type data which meets all of the conditions.
8. If the business view that contains the linked Blob content uses parameters, the Parameters tab will be enabled. In this tab, you can assign fields of the business view used by the current report to the parameters. Then, when accessing the Blob type data from the link, the field values will be assigned to the parameters automatically.
9. Select **OK** to apply the settings.

You can then trigger the link to download the Blob content according to the specified conditions. The link is also available when the report is opened in HTML, PDF, or Excel format.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Example of Binding a Conditional Link

This section provides an example to show the usage of conditional link and dynamic field.

1. On the Logi JReport Console > Resources page, open the Public Reports > SampleReports folder.
2. Put the mouse pointer over the report row of Link.wls and select the **Edit** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926643991/btn_srv_edit.gif) on the floating toolbar to open the report in Web Report Studio.
3. On the table of the report, right-click on a Product Name value and select **Link** from the shortcut menu.
4. In the Insert Link dialog, check the **Conditional Link** checkbox.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920385047/btn_add1.gif)to define a condition in the Edit Conditions dialog as follows.

   ![Link Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404920387863/wbrpt_edt_link1.gif)
6. We will make the field linked to a URL target based on the condition. From the Link Type drop-down list, select **URL**. In the Confirm dialog, select **OK**.
7. In the Hyperlink text box, type in **http://www.google.com/search?q=** and then select the **Add Dynamic Field** button to insert the field Product Name at the end of the URL.

   ![Conditional Link](https://devnet.logianalytics.com/hc/article_attachments/4404920388119/wbrpt_edt_link2.gif)
8. For the product names other than Blue Mountain and Breakfast Blend, we will make them linked to an e-mail target. Check the **Others** checkbox. A condition named Others will be created.
9. From the Link Type drop-down list, select **E-mail**. In the Confirm dialog, select **OK**.
10. In the Hyperlink text box, type in **@example.com** and then select the **Add Dynamic Field** button to insert the field Product Name right ahead of @.

    ![Other Links](https://devnet.logianalytics.com/hc/article_attachments/4404926644759/wbrpt_edt_link3.gif)
11. Select **OK** in the Insert Link dialog to finish defining the links.

Next we can select the product names in the table to view the link result.

1. Switch Web Report Studio to View Mode.
2. Select **Blue Mountain**. A Google search result page with the key text Blue Mountain is then displayed.

   ![Search Result for Blue Mountain](https://devnet.logianalytics.com/hc/article_attachments/4404926645015/wbrpt_edt_link5.gif)
3. Select **Breakfast Blend** and a Google search result page with the key text Breakfast Blend is displayed.
4. Navigate to the second page of the table. Select **Sumatra** and  an e-mail is displayed as follows:

   ![E-mail to Sumatra](https://devnet.logianalytics.com/hc/article_attachments/4404920388375/wbrpt_edt_link4.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009675261-Manipulating-Data-Components)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650242-Using-Dynamic-Resources-and-Local-Parameters-)
