---
title: "Specifying Parameter Values for a Dashboard"
id: 1500009718942
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009718942-Specifying-Parameter-Values-for-a-Dashboard
updated_at: 2021-07-25T07:20:13Z
---

# Specifying Parameter Values for a Dashboard

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745061-Filtering-the-Data-Components-in-a-Dashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745041-Exporting-and-Printing-Library-Components)

# Specifying Parameter Values for a Dashboard

The topic introduces how to specify parameter values to a dashboard/library compoment, how to save and customize parameter values, plus how to share parameters between library components.

Select the following links to view the topics:

* [Specifying Parameter Values to a Dashboard](#Dashboard)

+ [Specifying Multiple Values for a Parameter](#MultiValue)
+ [Saving Default Parameter Values](#Default)
+ [Saving Parameter Values for Reuse](#Reuse)

* [Specifying Parameter Values to a Library Component](#LC)
* [Sharing Parameters Between Library Components](#Share)

## Specifying Parameter Values to a Dashboard

When you run a dashboard that contains parameters, the default values of the parameters are applied automatically to the dashboard by default, which can be the default values specified in the parameters' definition or the [default values you save for the dashboard](#Default) when [Use User Defined Default Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009718962-Customizing-JDashboard-Profile#UserDefined) in the JDashboard profile is selected.

If you want to change the parameter values, after the dashboard is opened in JDashboard:

1. Select ![Enter Parameter Values button](https://devnet.logianalytics.com/hc/article_attachments/4404936748567/btn_dshbrd_prm.gif) on the toolbar to display the  [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009720082-Enter-Parameter-Values) dialog box.

   ![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936900631/enterprmvlu.gif)
2. Edit the parameter values according to your requirement.

   The way to specify a parameter value varies according to the type and properties of the parameter. Here are several ways you can use to specify parameter values:

   * ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")In the parameter value combo box, select the down arrow ![Drop Down button](https://devnet.logianalytics.com/hc/article_attachments/4404942452631/btn_dshbrd_more1.gif) and then select the required value from the drop-down list. To ensure performance, by default at most 500 values are listed.

     When a parameter's values are encrypted, the value drop-down list will be disabled. In this case, if the Hide Parameter Value check box is available, you can clear it to enable the drop-down list to view and select the required value.
   * Type the value manually in the parameter value text box if the parameter allows for type-in values but not multiple values.
   * Click in the parameter value combo box to [specify multiple values](#MultiValue) if the parameter allows for multiple values.
   * Select or clear the check box to specify a Yes/No value.
   * Select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values#DateTime).
3. If you want to save the specified values as the default values for the parameters, select **[Save as default](#Default)**.
4. To reset the parameter values, make use of the Reset button.
   * When Save as default is available in the dialog box, the Reset button contains a text part and a triangle icon. You can choose to reset the values to either of the following by selecting the triangle. If you select the text part of the button directly, the values will be reset to the original default values.
     + **Original Default Values**  
        The default values defined in the parameters' definition.
     + **User Defined Default Values**  
        Your last-time saved default values.
   * When Save as default is unavailable in the dialog box, the Reset button contains only the text part. Selecting it will reset the values to the original default values.
5. Select **Submit** to apply the specified parameter values.

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

**Tip:** If you want to make the Enter Parameter Values dialog box display before running dashboards that contain parameters, you can select the JDashboard profile option [Show Enter Parameter Values Dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009718962-Customizing-JDashboard-Profile#Show).

### Specifying Multiple Values for a Parameter

For a parameter that allows for multiple values (the parameter's Allow Multiple Values property is true), you can specify one or more values to it.

1. Click in the value combo box of the parameter. Report Server displays the [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009746841-Enter-Values) dialog box.

   ![Enter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936900375/entervlu.gif)
2. ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")If the parameter's Enable the "All Values" Option property is true, the All Values check box is available and by default it is selected. It means to apply the "All" value to the parameter. When the parameter is inserted as a field into a report and All Values is selected as the value, the field will show the string "All". If you do not want to apply the "All" value to the parameter, deselect the All Values check box, then specify the desired values as shown in the following steps.
3. ![This image notes any new content for version 17 of the product. For more information please see the Release Notes or What's New topics.](https://devnet.logianalytics.com/hc/article_attachments/4404942452887/__newv17.jpg "New for version 17.")Select the required values in the Available Values box and select ![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4404942453399/btn_add2.gif) to add them to the Selected Values box; to add all the listed values, select ![Add All Values](https://devnet.logianalytics.com/hc/article_attachments/4404942453655/btn_addall1.gif). To ensure performance, by default at most 500 values are listed in the Available Values box.

   If some added values are not wanted, select them in the Selected Values box and select ![Remove Values](https://devnet.logianalytics.com/hc/article_attachments/4404936723991/btn_rmv1.gif) to remove them; to remove all added values, select ![Remove All Values](https://devnet.logianalytics.com/hc/article_attachments/4404936724247/btn_rmvall1.gif).
4. When the parameter's Allow Type-in of Value property is true, the Enter Values text box is available. You can type a value manually and select ![Add Values](https://devnet.logianalytics.com/hc/article_attachments/4404942453399/btn_add2.gif) next to add it to the Selected Values box. When the parameter is bound with a column, but the display column is different from the bound column, make sure the value you type is that of the bound column. After you type text, the values in the Available Values box will be filtered to display those containing the text. To return to the original list, clear the input text. If the parameter is of the Date, DateTime, or Time type, you can also select the **Calendar** icon ![Calendar icon](https://devnet.logianalytics.com/hc/article_attachments/4404936722455/btn_clndr.gif) to [specify a date and time value](https://devnet.logianalytics.com/hc/en-us/articles/1500009724202-Specifying-Parameter-Values#DateTime).
5. When the parameter's Allow Type-in of Value property is false, the Search box is available for you to search for values among the available values: type text and the values containing the text will be listed in the Available Values box with the text highlighted in the values. To cancel the search, clear the input text.
6. Select **OK** to select the specified values for the parameter.

### Saving Default Parameter Values

By default, when any user runs a dashboard with parameters, the parameter values saved with the dashboard are applied, which means that all users see the same parameter result. However you can customize the default parameter values of a dashboard for your own. To do this, in the Enter Parameter Values dialog box specify the parameter values you want as the default values, select the **Save as default** option, and then select **Submit**.

However when using the Save Default Parameter Values feature, you need to be aware of the following:

* After saving default parameter values for a dashboard, when you run the dashboard if any of the parameters cannot find a matched validated value from the saved default values, all the parameters will use their default values specified in the parameters' definition as the initial values.
* If you change the [parameter sharing](#Share) setting in a dashboard, the saved default values will be cancelled and the default values specified in the parameters' definition will be used.
* JDashboard remembers the last-time saved result of a dashboard and displays the exact result the next time the dashboard is opened. In the case a dashboard user sets USA as the default parameter value and then filters the result with Canada and saves the dashboard, the next time the dashboard will run with Canada, though the saved default parameter value is still kept as USA. If the user wants the dashboard to run with USA, select the option Use User Defined Default Parameter Values in the My Profile > Customize Profile > JDashboard > Properties tab.

### Saving Parameter Values for Reuse

When specifying parameter values for dashboards, you may want to save the specified parameter values for reuse next time. Logi Report provides two ways of saving. One is users decide when and which parameter values to save, the other is Logi Report saves each applied or submitted parameter value automatically. When the saved number in either way reaches the maximum, the oldest record will be removed. The number is calculated on a user-dashboard basis. Take a dashboard with two parameters for an example, supposing the maximum number is set to 3. Each user can save at most three groups of parameter values for the dashboard, with each group containing the values of the two parameters.

To switch on the function of saving parameter values, you need to configure the server profile: select **Yes** to the option [Enable Saving Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#SaveParam), then select in which way to save the values: Manually or Automatically, and specify a maximum number to limit the saved value groups via the [Maximum Number of Auto Complete Parameters List](https://devnet.logianalytics.com/hc/en-us/articles/1500009744941-Configuring-Server-Profile#MaxNo) option for each user-dashboard pair.

**Manually saving parameter values**

When you have chosen to manually save parameter values, the Use Saved Values button ![Use Saved Values button](https://devnet.logianalytics.com/hc/article_attachments/4404936900887/btn_dshbrd_ussvvlu.gif) will be available in the Enter Parameter Values dialog box. By selecting this button, you will get the following:

* **Value list**  
   The value list contains all the parameter value groups you have saved for the dashboard. Select a group to apply all the values in the group to the corresponding parameters. You can also remove any of the unwanted value group by selecting it from the list and then selecting ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404942446871/btn_dltobj.gif) next to the value list.
* ![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404942445847/btn_save.gif)**Save Values**  
   Saves the current displayed parameter values as a group for reuse afterwards. To do this, type a name for the group in the text box which shows "Save current values into list" and then select **![Save button](https://devnet.logianalytics.com/hc/article_attachments/4404942445847/btn_save.gif)**. The saved group will then be added into the value list.

**Using automatically saved parameter values**

When you have chosen to automatically save parameter values, each time a user submits a group of parameter values to a dashboard, the group is saved by Logi Report automatically. The next time the same user runs the dashboard, the auto saved parameter values will be available in the parameters' value lists for selection in the Enter Parameter Values dialog box.

## Specifying Parameter Values to a Library Component

You can access the configuration panel of a library component to specify its parameter values. To do this, select ![Options icon](https://devnet.logianalytics.com/hc/article_attachments/4404942444951/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009745081-General-Operations-in-JDashboard#TitleBar) and select **Edit Setting** from the drop-down menu to display the configuration panel. Specify the values in the panel and select **OK** to apply them to the library component. The Cancel button is used to close the configuration panel.

The "Show the panel by default" option in the panel is used to control whether to show the configuration panel before rendering the library component each time the dashboard runs or is refreshed. For example, if a library component uses parameters, and you would like to specify parameter values before loading the component rather than first loading the component and then changing the parameter values so as to run the component the second time to get the desired result, you can select this option to have the panel displayed before rendering by default.

## Sharing Parameters Between Library Components

A dashboard can have multiple library components and all these components are independent from each other. When several components contain parameters which have the values and come from the same catalog, by default these parameters are regarded as separate parameters each connected to its own component. To submit a value to all these components, you need to submit the value for each of the parameters. However by sharing the parameters, you only need to provide a value for one of them as a representative of all the parameters. The parameters do not need to have the same name but do need to share the same values. You only need to submit values to this parameter once and all the components will use the specified values. By sharing parameters, the same parameters will only send the query once to the database, thus the dashboard performance can be improved.

**What parameters can be shared**

JDashboard supports sharing two types of parameters coming from different library components in the same dashboard:

* **The same parameters**  
   The parameters with the same name and coming from the same catalog.

  For example, a parameter *@Category* comes from the catalog A.cat, and in a dashboard it is used by two library components LC1 and LC2. So in the dashboard they are two parameters marked as *LC1.@Category* and *LC2.@Category*. These two parameters are the same parameter and only require the user to specify one value for them.
* **The same meaning parameters**  
   The parameters that are not the same parameters but have the same parameter type and value data type. For cascading parameters they should have the same hierarchies and each hierarchy have the same parameter value type, then they can be shared as parameters with the same meaning even though the names are different.

  For example, there are two parameters *@Province* and *@State* which have the same parameter type and value type so they can both have the same meaning. For the cascading parameters like *(@Country, @Province)* and *(@Country, @State)* which have the same hierarchies and each hierarchy has the same parameter value type so they also can have the same meaning.

**The rule for merging the values of the shared parameters**

Within a sharing group, if all the shared parameters allow for type-in values, the merged value result is the union of the values of all the parameters. The merged value names are distinct. However if any of the shared parameters does not allow type-in values, the merged value result is the intersection of all the values.

**Unexpected results after sharing parameters**

Sometimes there may be unexpected parameter sharing that does no harm to the report system and report data, but the dashboard result may be unexpected.

After sharing parameters, their values will be merged. The merged values result may be bigger or smaller than the value lists of some of the shared parameters, which might lead to some values cannot be supported by some components or some values can never be available to some components.

For example in the case of @Province and @State, if the parameters are shared then the list of values will be all states and provinces. However, one library component may use a query that limits the data to US only, thus if the user selects a Canadian province from the list the component will have no data.

**How to share parameters**

1. Select the **Options** button ![Options button](https://devnet.logianalytics.com/hc/article_attachments/4404936890647/btn_dshbrd_optn.gif) on the toolbar and then select **Share Parameter** from the option list. Report Server displays the [Share Parameters Setting](https://devnet.logianalytics.com/hc/en-us/articles/1500009747061-Share-Parameters-Setting) dialog box.

   ![Share Parameters Setting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936892439/shareprm.gif)
2. Select the parameters you would like to share by holding the Ctrl key. If the selected parameters support being shared, the Share button will be enabled. Select the button. The parameters will be added into one sharing group.

   To add another parameter into a sharing group, select any parameter in the group while holding Ctrl and then select the parameter, then select **Share**.

   To remove parameters from a sharing group, select the parameters and then select **Cancel Share** which appears in the place of the Share button.
3. Select **OK** to finish.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009745061-Filtering-the-Data-Components-in-a-Dashboard)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009745041-Exporting-and-Printing-Library-Components)
