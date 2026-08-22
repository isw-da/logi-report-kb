---
title: "Adding Links in Reports"
id: 1500009613322
section: "Creating Datasets and Designing Reports - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009613322-Adding-Links-in-Reports
updated_at: 2022-10-24T11:32:25Z
---

# Adding Links in Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636161-Filtering-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613282-Changing-the-Display-Type-of-Objects-in-Reports)

# Adding Links in Reports

You can add links in a report to make the report linked with other reports, locations specified by URLs, e-mail addresses, or Blob data type fields. In this way, the users of the report can gain access to the linked targets by selecting the corresponding trigger objects in the report. This topic describes the methods to add links in a report.

Logi Report Designer supports the following objects as the trigger objects of links: [labels](https://devnet.logianalytics.com/hc/en-us/articles/1500009606282-Labels), data fields ([DBFields](https://devnet.logianalytics.com/hc/en-us/articles/1500009629081-DBFields), [summary fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009629241-Summary-Fields-), [formula fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009629101-Formula-Fields), [parameter fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009606382-Parameter-Fields)), [special fields](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields), [images](https://devnet.logianalytics.com/hc/en-us/articles/1500009606262-Images), areas in [shape maps](https://devnet.logianalytics.com/hc/en-us/articles/1500009629181-Shape-Maps), and the category/series axis, legend and data markers in [charts](https://devnet.logianalytics.com/hc/en-us/articles/1500009605562-Charts). You can create either simple links or conditional links in a report. Using conditional links, you can make different targets loaded based on different conditions.

This topic includes the following sections:

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
2. In the [Insert Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009632221-Insert-Link-Dialog) dialog, select the target to which the trigger object will be linked: [Report](#Report), [Master/Detail Report](#Detail), [URL](#URL), [E-mail](#Mail), or [Content](#Content) from the Link Type drop-down list.
3. Specify the options for the link target.
4. Select **OK** to create the link.

**To add a conditional link in a report:**

1. Right-click the object used as the trigger object of the link and select **Link** on the shortcut menu.
2. In the Insert Link dialog, select the **Conditional Link** checkbox.

   ![Insert Link dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904187543/rpt_link_cndtnl.gif)
3. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) . The [Edit Conditions](https://devnet.logianalytics.com/hc/en-us/articles/1500009607862-Edit-Conditions-Dialog) dialog appears.

   ![Edit Conditions dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904187799/edtcndtn.gif)
4. Select the **Add Condition** button to add a condition line.
5. From the field drop-down list, select the field on which the condition will be based.
6. Choose the operator with which to compose the condition expression from the operator drop-down list.
7. From the value drop-down list, specify the value of how to build the condition. You can also type in the value manually.

   ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")You can specify an empty string as the value for a field of String type, by simply leaving the text box blank (value length=0). If you would like to filter space string (one or more spaces) as well as empty string, create a formula with the statement `Trim(@Field)` which transforms the spaces into empty string, then use the formula to replace the field itself on which the condition is based.
8. Select **Add Condition** to add more condition lines and define the logic between the condition lines.

   To make some condition lines grouped, select them and select the **Group** button, then the selected condition lines will be added in one group and work as one line of filter expression. Conditions and groups together can be further grouped. To take any condition or group in a group out, select it and select **Ungroup.**

   To adjust the priority of the condition lines, select it and select the **Up** or **Down** button.

   To delete a condition line, select it and select the **Delete** button.
9. Select **OK** to save the condition.

   The newly added condition is then displayed and highlighted in the conditions box in the Insert Link dialog.
10. From the Link Type drop-down, select the target to which the trigger object will be linked under this condition: [Report](#Report), [Master/Detail Report](#Detail), [URL](#URL), [E-mail](#Mail), or [Content](#Content), then specify the options for the link target.
11. Repeat the above steps to add more conditions and define the target for each condition.

    To edit a condition, select the condition, select ![Edit button](https://devnet.logianalytics.com/hc/article_attachments/4404911588375/btn_edit.gif), then edit it in the Edit Conditions dialog.

    To adjust the priority of the conditions, select a condition and select the ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404904182551/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404904182807/btn_mvdwn.gif) button.

    To remove a condition, select the condition and then select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404904182167/btn_rmv.gif).
12. Select the **Others** checkbox and define a target to which the trigger object will be linked when none of the conditions you have specified are met.
13. Select **OK** to create the conditional link. See [Example of binding a conditional link](#Example) for more information.

**Notes:**

* Conditional links are not supported on objects the parents of which are not bound with datasets.
* By default, the link action has the highest select priority at runtime. You can change the priority by setting the report's [Click Priority](https://devnet.logianalytics.com/hc/en-us/articles/1500009635621-Page-Report-Tab-Properties#Priority) property.

### Linking to Another Report

In most cases, your reports are affiliated with one another, with each report emphasizing one or more aspects of a bigger picture. Relationships can be set up for users to browse from one report to another through the relationship "channels" created. You can achieve an inter-report relationship network by setting up the link conditions between two reports in the same catalog. Then when you view the primary report at runtime, you can gain access to the linked report by selecting the trigger object.

**To make a report linked to another report:**

1. In the Insert Link dialog, select **Report** as the link type.

   ![Insert Link dialog - Report](https://devnet.logianalytics.com/hc/article_attachments/4404911621271/instlnk_rpt.gif)
2. If the primary report is a page report, select the **Browse** button to specify the page report in the same catalog that contains the report tab you want as the linked report. Then select the report tab name from the Report Tab drop-down list.

   If the primary report is a web report or a library component, select the **Browse** button to specify the web report in the same catalog that you want as the linked report.
3. From the Target drop-down list, select where you want the linked report to be loaded.

   The Target property works when the link is triggered in Page Report Studio or Web Report Studio. When the link is triggered in JDashboard, except for Same Frame, all the other targets are treated as New Window.
4. Select the **More** button to display more options for setting the link.
5. In the Filter tab, select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)**, then in the Choose Component dialog, add the data components in the linked report you want to be interlinked with the primary report. If the required data components use different datasets, you need to add them respectively, however you can add them all at the same time as long as the data components are based on the same dataset.

   ![Chosse Component dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911621655/rpt_link_chscmpnt.gif)
6. Specify the filter conditions based on which the link relationship between the primary report and the selected data components in the linked report (linked data components) are set up. However depending on where the trigger object is placed in the primary report, you are not able to define filter conditions under some circumstances. For example, if the trigger object is a label in the report body, you will find the Add button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the Field Conditions box is not activated.

   ![Edit Filter Condition Tab](https://devnet.logianalytics.com/hc/article_attachments/4404904188055/rpt_link_fltr.gif)

   1. Select a linked data component from the Components box.
   2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the Field Conditions box and a condition line is added.
   3. Select the primary field from the field drop-down list in the Fields (Primary) column. The provided field list contains all the data fields in the current catalog that are valid to the data resource used by the data component that contains the trigger object.

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When the trigger object is one of the following, you will find the item Current Field available in the Fields (Primary) drop-down list. Select it if you want to use the data field that is related to the trigger object in the filter condition.

      * A column/row field in a crosstab.
      * A DBField, formual field, summary field, or the special field Group Name in a banded object or table.
      * The chart legend which is bound with the category/series field of a chart, or the category/series axis of a chart.
   4. Choose an operator from the drop-down list in the OP column.
   5. Select the linked field from the field drop-down list in the Fields (Linked) column, where all data fields in the current catalog that are valid to the data resource used by the linked data component which are of the same data type as the selected primary field are listed.

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When you select Current Field in the Fields (Primary) drop-down list, Logi Report Designer will add the item Corresponding Field in the Fields (Linked) drop-down list if the dataset of the linked data component contains the data field which is of the same data type and the same name as the data field that is related to the trigger object in the primary report. Select **Corresponding Field** to use this corresponding field in the linked data component in the filter condition.

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When you define a filter condition as Current Field = Corresponding Field, the users of the report will be able to set up dynamic links with filters automatically generated from the drilling path at runtime. For example, if the data field related to the trigger object in the primary report is the group object Country, which is contained in a hierarchy and its one-level-lower group is City, after the report users drill from Country down to City in the primary report and trigger the link on any city, they will get data of the specified city in the linked data component only.
   6. You can specify more conditions by selecting **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)** and then specifying the primary field, the operator, and the linked field. The relationship between these conditions is AND, which means that Logi Report will fetch data for the linked data component which meets all of the conditions.
   7. Repeat the above steps to set link conditions between the primary report and other linked data components.
7. Specify whether to apply the on-screen filters (filters created via [filter controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009629421-Using-Advanced-Web-Controls#Filter)) in the primary report to the selected data components of the linked report (linked data components).

   ![Edit Filter Condition Tab](https://devnet.logianalytics.com/hc/article_attachments/4404904188055/rpt_link_fltr.gif)

   1. Select a linked data component from the Components box.
   2. Select **Pass on-screen filters to the linked components**.
   3. When the data component containing the trigger object in the primary report and the linked data component use different data resources, the Mapping Table button is activated. In this case, you need to select the button to define the mapping relationship based on which the on-screen filters in the primary report are passed to the linked data component using the [Mapping Table](https://devnet.logianalytics.com/hc/en-us/articles/1500009609102-Mapping-Table-Dialog)dialog.

      ![Mapping Table dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911621911/mptbl.gif)
   4. Select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)** to add a mapping line.
   5. Select the field that is bound with a filter control in the primary report from the drop-down list in the Fields (Primary) column.
   6. All available fields in the data resource used by the linked data component which are of the same data type as the selected filter control field are listed in the drop-down list in the Fields (Linked) column. Select a field whose values are the same as those of the filter control field.

      A mapping relationship is now set up. Then when the link is triggered, Logi Report will apply the corresponding on-screen filter in the primary report to the selected linked field in the linked data component.
   7. Add more mapping lines and define the mapping relationship between the filter control fields in the primary report with appropriate fields in the linked data component.
   8. Select **OK** to go back to the Insert Link dialog.
   9. Repeat the above steps to apply the on-screen filters in the primary report to other linked data components.
8. From the Default Linked Component drop-down list, select the data component that is displayed by default in the linked report when the link is triggered in exported result.

   For example, a linked report contains a chart and a table and the table is specified as the default linked component. When you export the primary report to PDF with linked report and trigger the link in the PDF result file, the page that contains the table will be displayed by default. You can scroll to view the chart.
9. If the linked report contains one or more parameters, the Parameters tab is activated. In this tab, you can assign fields of the primary report to parameters of the linked report to use the field values for the parameters automatically when running the linked report from the link. If the selected field is a parameter field, you can choose Current Value to use its most recently specified value or Initial Value to use its original value for the parameter in the linked report.

   ![Insert Link dialog - Report - Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404904188311/rpt_link_rptprm.gif)
10. If you would like the values of the filter objects like filter controls in the primary report to be passed to filter objects in the linked report, go to the **Advanced** tab to set up the relationship between the filter objects as follows (not available to library component):

    ![Insert Link dialog - Report - Advanced](https://devnet.logianalytics.com/hc/article_attachments/4404911622423/rpt_link_rptadvcd.gif)

    1. Select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)** to add a mapping line.
    2. Select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) in the Primary Report Property/Object column, then in the Select Value dialog select a filter object in the primary report and select **OK**.

       ![Select Value dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911622679/rpt_link_slctvlu.gif)

       All the objects in the primary report are listed in the Select Value dialog but only filter controls can be selected from the object tree.
    3. In the Linked Report Property/Object column, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404904183063/btn_chsr1.gif) to select a filter object in the linked report. You need to make sure that values of the filter object in the primary report can be applied to the filter object in the linked report in the same line.
    4. Follow the above steps to set up the relationship between more filter objects in the primary report and linked report.
11. Select **Pass style group information down to the linked report** to transfer style information from the primary report to the linked report, so that the style of the primary report will apply to the linked report.
12. Select **OK** to apply the settings.

Then, when you run the primary report at server runtime and select the trigger object, you will find that the linked report is displayed according to the specified link conditions. You can also trigger the link when viewing the report in HTML, PDF, or Excel format if you select the Run Linked Report option while specifying the settings of the corresponding format.

**Notes:**

* A page report can only be linked with another page report, and a web report with another web report. For a library component, it can only be linked with a web report.
* When linking reports, you need to avoid link loops. For example, if you have linked report A to report B, then you cannot link report B back to report A again.
* The conditions specified in the Filter tab are used for filtering when the link is triggered at server runtime, that is, only the data that meets the conditions in the linked report will be displayed. However, when the link is triggered in HTML, PDF, or Excel result, the conditions are used for setting up search criteria between the two linked reports, which means after you select the trigger object in the primary report, the pages containing the data that meet the conditions in the linked report will be displayed.
* ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When you specify the filter condition between the primary report and linked report as Current Field = Corresponding Field, at server runtime Logi Report will ignore the condition if there isn't a matched corresponding field in the linked report, which means after you trigger the link, you will get a linked report which is not filtered. In the meantime, Logi Report will add an error message into log to record the issue.

### Linking to a Detail Report

Reports in the same catalog can be joined together in order to create a master/detail report group. Usually, the master report holds comprehensive data, while the detail reports hold related detailed information. A detail report can also be the master report of another report. In this way, you can set up more pairs of master/detail reports, where many reports are joined together, eventually leading to the formation of a report chain. Then, when you view the master report at runtime, you can gain access to the detail report by selecting a trigger, which is an object defined in the master report to load a detail report. However, in a master/detail report group, crosstab reports cannot be used as the master.

The main advantage of using a master/detail relationship is the user can browse though the details by selecting next detail and previous detail without going back to the master report. When the user does go back to the master report they will see the master report based on the last detail report that was viewed.

The Master/Detail Report link type is supported in page reports that are created using query resources only.

**To make a report linked to a detail report:**

1. In the Insert Link dialog, select **Master/Detail Report** as the link type.

   ![Insert Link dialog - Mater/Detail Report](https://devnet.logianalytics.com/hc/article_attachments/4404904188567/instlnk_dtl.gif)
2. Select the **Browse** button next to the Report text box to specify the report in the same catalog which contains the report tab you want for the detail report, and then select the report tab name from the Report Tab drop-down list.
3. Select the **Browse** button beside the Component text box. In the Choose Component dialog, specify which data component in the detail report (detail data component) you want to be interlinked with the master report with conditions. You can select more than one detail data component as long as the data components are based on the same dataset.
4. From the Target drop-down list, select where the detail report will be loaded.
5. Specify the join relationship between the master report and detail report in the Anchor section. The join can only have one condition. For example, the join can be: (Detail Report) Product ID = (Master Report) Product ID. The join condition should be as:

   `(Detail Report) expression1 operator (Master Report) expresion2`

   To make the join more meaningful, expression1 should be a DBField or [record level pass one](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels)[formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#PassOne) in the GROUP section of the selected data component in the detail report; and expression2 a DBField or record level pass one formula in the DETAIL section of the data component that contains the trigger object in the master report. This is because generally the master report is used to present comprehensive data, and the detail report to present more detailed information. Therefore based on this prerequisite, Logi Report Designer only lists the qualified fields in the field drop-down lists of the Anchor section.

   **To specify the join condition:**

   1. Select a field from the Column in Detail Report drop-down list. If this list does not offer the required field, you will need to select the detail data component the query used by which contains the specific field. To do this, specify the component by selecting the Browse button besides the Component text box again.
   2. Choose the operator from the Operator drop-down list.
   3. Specify the field of the master report from the Column in Master Report drop-down list. This field should be of the same data type as the selected detail report field.
6. Select the **More** button to display more options for setting the link.
7. In the Conditions tab, specify the filter conditions between the master report and the selected data components in the detail report. However depending on where the trigger object is placed in the master report, you are not able to define filter conditions under some circumstances. For example, if the trigger object is a label in the report body, you will find the Add button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) above the Field Conditions box is not activated.
   1. Select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)** above the Field Conditions box and a condition line is added.
   2. Select the master report field from the Fields (Master Report) drop-down list. The provided field list contains the fields that satisfy the same conditions as for the Anchor section.

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When the trigger object is one of the following, you will find the item Current Field available in the Fields (Master Report) drop-down list. Select it if you want to use the data field that is related to the trigger object in the filter condition.

      * A column/row field in a crosstab.
      * A DBField, formual field, summary field, or the special field Group Name in a banded object or table.
      * The chart legend which is bound with the category/series field of a chart, or the category/series axis of a chart.
   3. Choose an operator from the drop-down list in the OP column.
   4. Specify the detail report field from the drop-down list in the Fields (Detail Report) column. The available fields are those that satisfy the same conditions as for the Anchor section and at the same time are of the same data type as the selected master report field.

      ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When Current Field is selected in the Fields (Master Report) drop-down list, if the dataset of the detail data component contains the data field which is of the same data type and the same name as the data field that is related to the trigger object in the master report, the item Corresponding Field will be available in the Fields (Detail Report) drop-down list. Select it to use this corresponding field in the detail data component in the filter condition.
   5. You can specify more conditions by selecting the button **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)** and then specifying the master report field, the operator, and the corresponding field in the detail report. You can use the More column to specify the relationship between conditions to be AND or OR.
8. If there is at least one parameter applied in the filters of the queries that the detail report uses, the Parameters tab is enabled. In this tab, you can assign field of the master report to parameter of the detail report. Then when running the detail report from the link, the field value of the master report will be assigned to the parameter automatically.

   ![Insert Link dialog - Mater/Detail Report - Parameter](https://devnet.logianalytics.com/hc/article_attachments/4404911622935/rpt_link_dtlprm.gif)
9. If both reports use the same encoding and DB settings, you should select the option **Use the same encoding and DB settings for the detail report as that of the master report**. If this option is not selected, when the detail report is triggered at runtime, you will be prompted to specify the encoding and DB settings for the detail report.
10. Select **OK** to confirm.

After a set of master/detail reports have been defined in Logi Report Designer and published to Logi Report Server, they can be viewed in Page Report Studio. The detail report supports all the page report operations, such as Sort, Filter, Drill, and Search.

**Notes:**

* The join and filter conditions work together. If you want to set a single condition, you can use join (anchor). If you want to set a group of conditions, you can use the filter conditions together with a join condition. The relationship between the join and filter conditions is "join condition AND (filter conditions)".
* ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404911621015/___newv17.jpg "New for version 17.")When you specify the filter condition between the master report and detail report as Current Field = Corresponding Field, at server runtime if there isn't a matched corresponding field in the detail report, the condition will be ignored, which means after you trigger the link, you will get a detail report which is not filtered. In the meantime, an error message will be added into log to record the issue.
* If you specify to load the detail report in a new browser window, the detail report will be opened independently when you select the trigger in Page Report Studio. That is to say, the join and filter conditions you have set between the master report and detail report will not be applied.

### Linking to a URL

1. In the Insert Link dialog, select **URL** as the link type.

   ![Insert Link dialog - URL](https://devnet.logianalytics.com/hc/article_attachments/4404904188823/instlnk_url.gif)
2. Type the URL in the Hyperlink text box directly. You can select the **Add Dynamic Field** button to insert a field into the URL via the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009610322-Select-Field-Dialog) dialog to compose a dynamic URL.

   ![Select Field dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911623191/slctfld.gif)

   For example, you can compose a URL as follows: type in **http://www.google.com/search?q=** into the Hyperlink text box, then select the **Add Dynamic Field** button to insert the field Country at the end of the URL. You can then select the trigger object to open a specific URL that directs to a specific country.
3. Specify the frame from the Target drop-down list.

   The Target property works when the link is triggered in Page Report Studio or Web Report Studio. When the link is triggered in JDashboard, except for Same Frame, all the other targets are treated as New Window.
4. When you link a trigger object in a web report table to a URL, you can select the **IE Navigate2 Flags** button to use the IE Navigate2 method and its flags to control the behavior of IE when loading the URL in Internet Explorer. Choose one or more flags as needed.
5. Select **OK** to set up the link.

Then, when you run the report at server runtime, or view it in HTML, PDF or Excel format, you can select the trigger object to open the URL.

### Linking to an E-mail

1. In the Insert Link dialog, select **E-mail** as the link type.

   ![Insert Link dialog - E-mail](https://devnet.logianalytics.com/hc/article_attachments/4404904189079/instlnk_mail.gif)
2. Type the [e-mail address](#MailSyntax) in the Hyperlink text box directly. You can select the **Add Dynamic Field** button to insert a field into the e-mail address via the [Select Field](https://devnet.logianalytics.com/hc/en-us/articles/1500009610322-Select-Field-Dialog) dialog to compose a dynamic e-mail address.
3. Select **OK** to set up the link.

Then, when you run the report at server runtime, or view it in HTML, PDF or Excel format, you can select the trigger object to open the e-mail with the information specified in the Hyperlink box. You can further customize the e-mail and send it.

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

Hyperlink examples:

* `user@example.com`
* `user1@example.com;user2@example.com`
* `Customer Name@jinfonet.com`, here Customer Name is a field name. Note that, fields can work in the hyperlink only when they are inserted via the Add Dynamic Field option.
* `salesmanager@Country.jinfonet.com`, here Country is a field name.
* `user@example.com?CC=user1@example.com&BCC=user2@example.com&subject=TestLinkToEmail&Body=Version%20x.x%0D%0A%0D%0ATest%20Link%20To%20E-mail`

  Here is the e-mail result:

  ![Label Linked Mail](https://devnet.logianalytics.com/hc/article_attachments/4404911623447/rpt_link_mail.gif)

### Linking to a Blob Data Type Field

When a report is linked with Blob data type fields, the Blob data type fields will be bound to the trigger objects of the links and displayed as hyperlinks, and you can download the Blob content by selecting the hyperlinks in the report.

In Logi Report, Blob could be image, Binary, Blob, Clob, LongBlob, LongClob, Varbinary, Longvarbinary, and so on.

Page reports created using business views cannot be linked to Blob data type fields.

**To make a report linked to a Blob data type field:**

1. In the Insert Link dialog, select **Content** as the link type.

   ![Insert Link dialog - Content](https://devnet.logianalytics.com/hc/article_attachments/4404904189335/instlnk_cntnt.gif)

   Depending on the location of the trigger object, you are not able to link the report with Blob data type fields under some special circumstances. For example, if the trigger object is a label in the report body, after you choose the Content link type, you will be prompted with a warning message and all the other settings in the dialog are disabled.
2. From the Query drop-down list, select the query (for page report) or business view (for web report and library component) which contains the required Blob data type field. The available queries/business views are those that come from the same data source connection as the query/business view the current report uses.
3. From the Content Type drop-down list, specify the content type for the Blob type data. You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif) to bind the content type with a field in the selected query/business view, or [use a formula to control](https://devnet.logianalytics.com/hc/en-us/articles/1500009634221-Using-Formulas-to-Control-Object-Properties) the type.
4. In the File Name text box, specify a file name for the linked Blob type data. You can also select ![Formula button](https://devnet.logianalytics.com/hc/article_attachments/4404904189591/btn_fmla.gif) to specify a field or formula to control the name.
5. From the Content drop-down list, choose a Blob data type field in the selected query/business view.
6. Select the **More** button to display more link options.
7. In the Filter tab, specify the filter conditions between the query/business view used by the current report and the query/business view that contains the linked Blob content as follows:
   1. Select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)** above the Field Conditions box and a condition line is added.
   2. Select the desired data field in the query/business view used by the current report from the Fields (Primary) drop-down list. Select **Current Field** if you want to use the data field that is related to the trigger object of the link in the filter condition.
   3. Choose an operator from the drop-down list in the OP column.
   4. Select the linked field from the drop-down list in the Fields (Linked) column. All the data fields in the query/business view containing the linked Blob content which are of the same data type as the selected field in the Fields (Primary) column are available in the drop-down list.

      When Current Field is selected in the Fields (Primary) drop-down list, if the query/business view containing the linked Blob content has the data field which is of the same data type and the same name as the data field that is related to the trigger object, the item Corresponding Field will be available in the Fields (Linked) drop-down list. Select it to use this corresponding field in the query/business view of the Blob content in the filter condition.
   5. You can specify more conditions by selecting **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif)** and then specifying the fields and operators accordingly. The relationship between these filter conditions is AND, which means that Logi Report will fetch the linked Blob type data which meets all of the conditions.
8. If the query/business view that contains the linked Blob content uses parameters, the Parameters tab will be enabled. In this tab, you can assign fields of the query/business view used by the current report to the parameters. Then, when accessing the Blob type data from the link, the field values will be assigned to the parameters automatically.
9. Select **OK** to apply the settings.

Then, when you run the report at server runtime, or view it in HTML, PDF or Excel format, you can select the trigger object to download the Blob content according to the specified conditions.

## Editing the Links in a Report

You can edit the links added in a report at any time. To do this, right-click the trigger object of the link you want to edit and select **Edit Link** from the shortcut menu. Then in the Edit Link dialog, [redefine the link](#Add).

See also the [Edit Link](https://devnet.logianalytics.com/hc/en-us/articles/1500009607902-Edit-Link-Dialog) dialog for additional information about options in the dialogs.

## Removing Links from a Report

To remove a link from a report, right-click the trigger object of the link and select **Remove Link** from the shortcut menu.

## Example of Adding a Conditional Link

This example shows the usage of conditional link and dynamic field.

1. Make sure SampleReports.cat is the currently open catalog file. If not select **File** > **Open Catalog** to open it from `<install_root>\Demo\Reports\SampleReports`.
2. Select **File** > **New** > **Web Report** to create a web report.
3. [Insert a summary table in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009629281-Inserting-Tables-in-a-Report-#BV) which is based on WorldWideSalesBV in Data Source 1 of the catalog, shows Product Name, Total Sales and Total Cost, and uses the Basic style.
4. Right-click on the **Product Name** field in the second group header panel and then select **Link** from the shortcut menu.

   ![Insert a Link for the Label](https://devnet.logianalytics.com/hc/article_attachments/4404911623703/rpt_link_eg1.gif)
5. In the Insert Link dialog, select the **Conditional Link** checkbox.
6. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904181783/btn_add.gif) to define a condition in the Edit Conditions dialog as follows.

   ![Add Conditions](https://devnet.logianalytics.com/hc/article_attachments/4404904189847/rpt_link_eg2.gif)
7. We will make the field linked to a URL target based on the condition. From the Link Type drop-down list, select **URL**. In the Message dialog, select **Yes**.
8. In the Hyperlink text box, type in **http://www.google.com/search?q=** and then select the **Add Dynamic Field** button to insert the field Product Name at the end of the URL.

   ![Insert Link](https://devnet.logianalytics.com/hc/article_attachments/4404911623959/rpt_link_eg3.gif)
9. For the product names other than Blue Mountain and Breakfast Blend, we will make them linked to an e-mail target. Select the **Others** checkbox. A condition named Others will be created.
10. From the Link Type drop-down list, select **E-mail**. In the Message dialog, select **Yes**.
11. In the Hyperlink text box, type in **@example.com** and then select the **Add Dynamic Field** button to insert the field Product Name right ahead of @.

    ![Insert Link](https://devnet.logianalytics.com/hc/article_attachments/4404911624471/rpt_link_eg4.gif)
12. Select **OK** in the Insert Link dialog.
13. Select **File** > **Save** to save the report and select **View** > **Preview As** > **Web Report Result** to view the report result in Web Report Studio. We can select the product names in the table to trigger the link.
14. Select **Blue Mountain** and a Google search result page with the key text Blue Mountain will be displayed.

    ![Google Search Result](https://devnet.logianalytics.com/hc/article_attachments/4404904190103/rpt_link_eg5.gif)
15. Select **Breakfast Blend** and a Google search result page with the key text Breakfast Blend will be displayed.
16. Select another product name other than Blue Mountain and Breakfast Blend to send an e-mail.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009636161-Filtering-Reports) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009613282-Changing-the-Display-Type-of-Objects-in-Reports)
