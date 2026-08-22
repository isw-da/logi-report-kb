---
title: "Adding Links in a Report"
id: 1500009724822
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009724822-Adding-Links-in-a-Report
updated_at: 2021-07-25T07:18:34Z
---

# Adding Links in a Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-)

# Adding Links in a Report

You can link a web report with other reports, locations specified by URLs, e-mail addresses, or Blob data type fields, to gain access to the linked targets by selecting the corresponding trigger objects in the report. This topic describes the methods to add links in a report.

Web Report Studio supports the following objects as the trigger objects of links: labels, images, DBFields, formula fields, parameter fields, special fields, and the category (X) axis labels, legend labels and data markers of charts.You can create either simple links or conditional links in a report. Using conditional links, you can make different targets loaded based on different conditions.

Select the following links to view the topics:

* [Adding a Link](#Add)

+ [Linking to Another Report](#Report)
+ [Linking to a URL](#URL)
+ [Linking to an E-Mail](#Mail)
+ [Linking to a Blob Data Type Field](#Content)

* [Opening a Link](#Open)
* [Editing a Link](#Edit)
* [Removing a Link](#Remove)
* [Example of Adding a Conditional Link](#Example)

## Adding a Link

**To add a simple link in a report:**

1. Right-click the object used as the trigger object of the link and select **Link** on the shortcut menu to display the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009749021-Insert-Link) dialog box.
2. From the Link Type drop-down list, select the target to which the object will be linked: [Report](#Report), [URL](#URL), [E-mail](#Mail) or [Content](#Content).
3. Specify the options for the link target.
4. Select **OK** to create the link.

**To add a conditional link to an object:**

1. Right-click the object used as the trigger object of the link and select **Link** from the shortcut menu to display the Insert Link dialog box.
2. Select the **Conditional Link** check box.
3. Select the button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to open the [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009721522-Edit-Conditions) dialog box to define a condition using either [simple expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters#Simple) or [complex expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters#Complex) according to your requirements.

   The newly added condition will then be displayed and highlighted in the conditions box in the Insert Link dialog box.
4. From the Link Type drop-down list, select the target to which the object will be linked under this condition: [Report](#Report), [URL](#URL), [E-mail](#Mail) or [Content](#Content), then specify the options for the link target.
5. Repeat the above steps to add more conditions and define the link target for each condition.

   To edit a condition, select the condition in the Condition box, then select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404936735255/btn_wbrpt_edit.gif). In the Edit Conditions dialog box, edit the expressions as required.

   To remove a condition and the corresponding format, select the condition in the Condition box and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404936717719/btn_delete.gif).

   To adjust the priority of a condition, select the condition in the Condition box and then select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404942457495/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404936729239/btn_mvdown.gif).
6. Select **OK** to finish defining the conditional link.

For an illustrated example, see [Example of binding a conditional link](#Example).

### Linking to Another Report

You can make a report linked to another report, then when you select the trigger object in the primary report, you will be able to jump to the linked report to obtain information about the trigger object.

1. In the Insert Link dialog box, select **Report** as the link type.

   ![Link to Report](https://devnet.logianalytics.com/hc/article_attachments/4404936735511/insrtlnk_rpt.gif)
2. Select the **Browse** button beside the Report text box to specify the target web report you want as the linked report in the [Select a Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009749381-Select-a-Report) dialog box.
3. Specifies the window or frame in which to load the linked report from the Target drop-down list.
4. You can select the **More** button to display more options for setting the link.
5. In the Filter tab, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) above the Components box to specify which data component in the linked report will be interlinked with the primary report. You can add only one data component at a time, so if there are multiple data components in the linked report and you want some or all of them to be interlinked with the primary report, you will need to select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) several times to add them one by one.
6. Specify the filter conditions based on which the link relationship between the primary report and the selected data components in the linked report (linked data components) are set up. However depending on where the trigger object is placed in the primary report, you are not able to define filter conditions under some circumstances. For example, if the trigger object is a label in the report body, you will find the Add button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) above the Field Conditions box is not activated.

   ![Insert Link - Filter Tab](https://devnet.logianalytics.com/hc/article_attachments/4404936735767/wbrpt_edt_link_fltr.gif)

   1. Select a linked data component in the Components box.
   2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) above the Field Conditions box and a condition line is added.
   3. Select the primary field from the field drop-down list in the Fields (Primary) column. The provided field list contains all view elements in the business view used by the data component that contains the trigger object, as well as the dynamic formulas in the primary report.

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")When the trigger object is one of the following, you will find the item Current Field available in the Fields (Primary) drop-down list. Select it if you want to use the data field that is related to the trigger object in the filter condition.

      * A column/row field in a crosstab.
      * A DBField, formual field, summary field, or the special field Group Name in a banded object or table.
      * The chart legend labels which are bound with the category/series field of a chart, or the category axis labels of a chart.
   4. Choose an operator from the drop-down list in the OP column. The operator can be "=", "<>", "<", ">", "<=", ">=", or "IN".
   5. Select the linked field from the field drop-down list in the Fields (Linked) column, where the view elements in the business view used by the linked data component which are of the same data type as the selected primary field are listed.

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")When Current Field is selected in the Fields (Primary) drop-down list, if the business view of the linked data component contains the data field which is of the same data type and the same name as the data field that is related to the trigger object in the primary report, the item Corresponding Field will be available in the Fields (Linked) drop-down list. Select it to use this corresponding field in the linked data component in the filter condition.

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")When you define a filter condition as Current Field = Corresponding Field, you will be able to set up dynamic links with filters automatically generated from the [drilling](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data) path. For example, if the data field related to the trigger object in the primary report is the group object Country, which is contained in a hierarchy and its one-level-lower group is City, after you drill from Country down to City in the primary report and trigger the link on any city, you will get data of the specified city in the linked data component.
   6. You can specify more conditions by selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) and then specifying the primary field, the operator, and the corresponding linked field. The relationship between these conditions is AND, which means that Web Report Studio will fetch data for the linked data component which meets all of the conditions.
   7. Repeat the above steps to set link conditions between the primary report and other linked data components.
7. Specify whether to apply the [on-screen filters](https://devnet.logianalytics.com/hc/en-us/articles/1500009751481-Applying-Filters#OnScreen) in the primary report to the selected data components of the linked report (linked data components).

   ![Insert Link - Filter Tab](https://devnet.logianalytics.com/hc/article_attachments/4404936735767/wbrpt_edt_link_fltr.gif)

   1. Select a linked data component from the Components box.
   2. Select **Pass on-screen filters to the linked components**.
   3. When the data component containing the trigger object in the primary report and the linked data component use different business views, the Mapping Table button is activated. In this case, you need to select the button to define the mapping relationship based on which the on-screen filters in the primary report are passed to the linked data component using the [Mapping Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009749141-Mapping-Table) dialog box.

      ![Mapping Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936736023/mptbl.gif)
   4. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add a mapping line.
   5. Select the field that is bound with an on-screen filter in the primary report from the drop-down list in the Fields (Primary) column.
   6. All available fields in the business view used by the linked data component which are of the same data type as the selected on-screen filter field are listed in the drop-down list in the Fields (Linked) column. Select a field whose values are the same as those of the on-screen filter field.

      A mapping relationship is now set up. Then when the link is triggered, the corresponding on-screen filter in the primary report will be applied to the selected linked field in the linked data component.
   7. Add more mapping lines and define the mapping relationship between the on-screen filter fields in the primary report with appropriate fields in the linked data component.
   8. Select **OK** to go back to the Insert Link dialog box.
   9. Repeat the above steps to apply the on-screen filters in the primary report to other linked data components.
8. From the Default Linked Component drop-down list, select the component that is displayed by default in the linked report when the link is triggered in exported result.

   For example, a linked report contains a chart and a table and the table is specified as the default linked component. When you export the primary report to PDF with linked report and trigger the link in the PDF result file, the page that contains the table will be displayed by default. You can scroll to view the chart.
9. If the linked report contains one or more parameters, the Parameters tab is activated. In this tab, you can assign fields of the primary report to parameters of the linked report to use the field values for the parameters automatically when running the linked report from the link. If the selected field is a parameter field, you can choose Current Value to use its most recently specified value or Initial Value to use its original value for the parameter in the linked report.

   ![Insert Link - Parameters Tab](https://devnet.logianalytics.com/hc/article_attachments/4404942461207/wbrpt_edt_link_prm.gif)
10. If you would like the values of the filter objects like filter controls in the primary report to be passed to filter objects in the linked report, go to the **Advanced** tab to set up the relationship between the filter objects as follows.

    ![Insert Link - Advanced Tab](https://devnet.logianalytics.com/hc/article_attachments/4404936736279/wbrpt_edt_link_advcd.gif)

    1. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) to add a line.
    2. In the Primary Report Property/Object column, select ![Select Value](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) to select a filter object in the primary report in the [Select Value](https://devnet.logianalytics.com/hc/en-us/articles/1500009722282-Select-Value) dialog box and select **OK**.
    3. In the Linked Report Property/Object column, select ![Select Value](https://devnet.logianalytics.com/hc/article_attachments/4404936725911/btn_chsr.gif) to select a filter object in the linked report in the Select Value dialog box and select **OK**. You need to make sure that values of the filter object in the primary report can be applied to the filter object in the linked report in the same line.
    4. Follow the above steps to set up the relationship between more filter objects.
11. Select **OK** to apply the settings.

Then when you are in the View Mode of Web Report Studio, you can trigger the link to open the linked report. The link is also available when you run the primary report in the HTML, PDF, or Excel format with the **Run Linked Report** option selected.

If the linked report is opened in the same frame as the primary report in Web Report Studio, you can select ![Back button](https://devnet.logianalytics.com/hc/article_attachments/4404936736535/btn_back.gif) on the toolbar to go back to the primary report. Select ![Go To button](https://devnet.logianalytics.com/hc/article_attachments/4404936736791/btn_goto.gif) next to ![Back button](https://devnet.logianalytics.com/hc/article_attachments/4404936736535/btn_back.gif) and you will get a drop-down list which lists the original report and the linked targets you have just visited within the link chain. The item selected on the drop-down list is the currently opened page. Select an unselected item and you will be directed to that target.

**Notes:**

* When linking reports, you need to avoid link loops. For example, if you have linked report A to report B, then you cannot link report B back to report A again.
* The conditions specified in the Filter tab are used for filtering when the link is triggered in Web Report Studio, that is, only the data that meet the conditions in the linked report will be displayed. However, when the link is triggered in HTML, PDF, or Excel result, the conditions are used for setting up search criteria between the two linked reports, which means after you select the trigger object in the primary report, the pages containing the data that meet the conditions in the linked report will be displayed.
* ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")When you specify the filter condition between the primary report and linked report as Current Field = Corresponding Field, if there isn't a matched corresponding field in the linked report, the condition will be ignored, which means after you trigger the link, you will get a linked report which is not filtered. In the meantime, an error message will be added into log to record the issue.

### Linking to a URL

1. In the Insert Link dialog box, select **URL** as the link type.

   ![Link to URL](https://devnet.logianalytics.com/hc/article_attachments/4404936737047/insrtlnk_url.gif)
2. Type the URL in the Hyperlink text box directly. You can select the **Add Dynamic Field** button to insert a field into the URL via the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009749341-Select-Field#Link) dialog box to compose a dynamic URL.

   For example, suppose the link is defined on the Country DBField and you compose the URL as follows: type **http://www.google.com/search?q=** into the Hyperlink text box, then select the **Add Dynamic Field** button to insert the field Country at the end of the URL. You can then select any country value to open a specific URL that directs to a specific country.
3. Specify the frame from the Target drop-down list.

   The Target property works when the link is triggered in Web Report Studio. When the link is triggered in JDashboard, except for Same Frame, all the other targets are treated as New Window.
4. Select **OK** to set up the link.

Then when you are in the View Mode of Web Report Studio, you can trigger the link to open the URL. The link is also available when you run the report in the HTML, PDF, or Excel format.

### Linking to an E-Mail

1. In the Insert Link dialog box, select **E-mail** as the link type.

   ![Link to E-mail](https://devnet.logianalytics.com/hc/article_attachments/4404936737303/insrtlnk_mal.gif)
2. Type the [e-mail address](#MailSyntax) in the Hyperlink text box directly. You can select the **Add Dynamic Field** button to insert a field into the e-mail address via the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009749341-Select-Field#Link) dialog box to compose a dynamic e-mail address.
3. Select **OK** to set up the link.

Then when you are in the View Mode of Web Report Studio, you can trigger the link to open the e-mail. You can further customize the e-mail and send it. The link is also available when you run the report in the HTML, PDF, or Excel format.

**E-mail address syntax**

When composing the e-mail address, you need to follow the syntax: `sAddress[sHeaders]`. See the details about the syntax below.

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

  ![E-mail Result](https://devnet.logianalytics.com/hc/article_attachments/4404942461463/wbrpt_edt_link_mail.gif)

### Linking to a Blob Data Type Field

When you link a report with Blob data type fields, Web Report Studio will bind the Blob data type fields to the trigger objects of the links and display them as hyperlinks. You can then download the Blob content by selecting the hyperlinks in the report.

In Web Report Studio, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, Longvarbinary, and so on.

**To make a report linked to a Blob data type field:**

1. In the Insert Link dialog box, select **Content** as the link type.

   ![Link to Content](https://devnet.logianalytics.com/hc/article_attachments/4404942461719/insrtlnk_cntnt.gif)

   Depending on the location of the trigger object, you are not able to link the report with Blob data type fields under some special circumstances. For example, if the trigger object is a label in the report body, after you choose the Content link type, you will find all the other settings in the dialog box are disabled.
2. From the Query drop-down list, select the business view which contains the required Blob data type field. The available business views are those that come from the same data source connection as the business view the current report uses.
3. From the Content Type drop-down list, specify the content type for the Blob type data. You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936732951/btn_wbrpt_fmla.gif) to bind the content type with a string type business view element in the selected business view, or with a dynamic formula in the current report.
4. In the File Name text box, specify a file name for the linked Blob type data. You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404936732951/btn_wbrpt_fmla.gif) to specify a string type view element in the selected business view, or a dynamic formula in the current report, to control the file name.
5. From the Content drop-down list, choose a Blob data type field in the selected business view.
6. Select the **More** button to display more link options.
7. In the Filter tab, specify the filter conditions between the business view used by the current report and the business view that contains the linked Blob content as follows:
   1. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) above the Field Conditions box and a condition line is added.
   2. Select the desired view element in the business view used by the current report or a dynamic formula in the current report as the primary field from the Fields (Primary) drop-down list. Select **Current Field** if you want to use the field that is related to the trigger object of the link in the filter condition.
   3. Choose an operator from the drop-down list in the OP column.
   4. Select the linked field from the drop-down list in the Fields (Linked) column. All the view elements in the business view containing the linked Blob content which are of the same data type as the selected field in the Fields (Primary) column are available in the drop-down list.

      When Current Field is selected in the Fields (Primary) drop-down list, if the business view containing the linked Blob content has the view element which is of the same data type and the same name as the field that is related to the trigger object, the item Corresponding Field will be available in the Fields (Linked) drop-down list. Select it to use this corresponding field in the business view of the Blob content in the filter condition.
   5. You can specify more conditions by selecting ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif) and then specifying the fields and operators accordingly. The relationship between these link conditions is AND, which means that Web Report Studio will fetch the linked Blob type data which meets all of the conditions.
8. If the business view that contains the linked Blob content uses parameters, the Parameters tab will be enabled. In this tab, you can assign fields of the business view used by the current report to the parameters. Then, when accessing the Blob type data from the link, the field values will be assigned to the parameters automatically.
9. Select **OK** to apply the settings.

Then when you are in the View Mode of Web Report Studio, you can trigger the link to download the Blob content according to the specified conditions. The link is also available when you run the report in the HTML, PDF, or Excel format.

## Opening a Link

To open a link, switch Web Report Studio to **View Mode**, then right-click the trigger object and select **Show Linked Target** from the shortcut menu.

If the web report is created in Web Report Studio, you can also directly select the trigger object to open the link, while for a web report created in Logi Report Designer, whether you can do this depends on if the report designer gave the Link action the highest Click Priority at report design time. If the priority of the [go-down](https://devnet.logianalytics.com/hc/en-us/articles/1500009724802-Going-Through-the-Report-Data) action is specified the highest and the trigger object is in a hierarchy, you can use a select on the object to open the link only after you have gone down to the lowest level of the hierarchy.

## Editing a Link

To edit a link, right-click its trigger object and select **Edit Link** from the shortcut menu. In the [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009721542-Edit-Link) dialog box, [edit the link](#Add) according to your requirement.

## Removing a Link

To remove a link, right-click its trigger object and select **Remove Link** on the shortcut menu. In the warning message dialog box, select **Yes** to confirm the removal.

## Example of Adding a Conditional Link

The following provides an example to show the usage of conditional link and dynamic field.

1. In Web Report Studio [create a summary table](https://devnet.logianalytics.com/hc/en-us/articles/1500009724682-Creating-Web-Reports-Using-Wizard)  which is based on WorldWideSalesBV in Data Source 1, shows Product Name, Total Sales and Total Cost, and use Basic as the report style.
2. Right-click on any Product Name value and select **Link** from the shortcut menu.

   ![Link Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404942461975/wbrpt_edt_link6.gif)
3. In the Insert Link dialog box, select the **Conditional Link** check box.
4. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404936734999/btn_add1.gif)to define a condition in the Edit Conditions dialog box as follows.

   ![Link Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404936737687/wbrpt_edt_link1.gif)

We will make the field linked to a URL target based on the condition.

1. From the Link Type drop-down list in the Insert Link dialog box, select **URL**. In the Confirm dialog box, select **OK**.
2. In the Hyperlink text box, type **http://www.google.com/search?q=** and then select the **Add Dynamic Field** button to insert the field **Product Name** at the end of the URL.

   ![Conditional Link](https://devnet.logianalytics.com/hc/article_attachments/4404942462231/wbrpt_edt_link2.gif)

For the product names other than Blue Mountain and Breakfast Blend, we will make them linked to an e-mail target.

1. Select the **Others** check box. A condition named Others is created.
2. From the Link Type drop-down list, select **E-mail**. In the Confirm dialog box, select **OK**.
3. In the Hyperlink text box, type **@example.com** and then select the **Add Dynamic Field** button to insert the field Product Name right ahead of @.

   ![Other Links](https://devnet.logianalytics.com/hc/article_attachments/4404936737943/wbrpt_edt_link3.gif)
4. Select **OK** in the Insert Link dialog box to finish defining the links.

Next we can select the product names in the table to view the link result.

1. Switch Web Report Studio to View Mode.
2. Select **Blue Mountain**. A Google search result page with the keyword Blue Mountain is then displayed.

   ![Search Result for Blue Mountain](https://devnet.logianalytics.com/hc/article_attachments/4404942462743/wbrpt_edt_link5.gif)
3. Select **Breakfast Blend**. Report Server displays a Google search result page with the keyword **Breakfast Blend**.
4. Select **Sumatra**. Report Server displays an e-mail as follows:

   ![E-mail to Sumatra](https://devnet.logianalytics.com/hc/article_attachments/4404936738327/wbrpt_edt_link4.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009724842-Manipulating-Data-Components)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009751461-Using-Dynamic-Resources-and-Local-Parameters-)
