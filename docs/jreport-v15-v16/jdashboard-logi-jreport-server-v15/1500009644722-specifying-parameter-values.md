---
title: "Specifying Parameter Values"
id: 1500009644722
section: "JDashboard Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009644722-Specifying-Parameter-Values
updated_at: 2021-07-24T20:55:17Z
---

# Specifying Parameter Values

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644822-Saving-Dashboards)

# Specifying Parameter Values

This topic introduces how to specify parameter values in dashboard and library components.

Below is a list of the sections covered in this topic:

* [Specifying Parameter Values to a Dashboard](#Dashboard)
* [Specifying Parameter Values to a Library Component](#LC)
* [Saving Parameter Values for Reuse](#Save)
* [Customizing Default Parameter Values](#DefaultParam)
* [Sharing Parameters Between Library Components](#Share)

## Specifying Parameter Values to a Dashboard

When you run a dashboard that contains parameters, the default values of the parameters are applied automatically to the dashboard by default. If you want to change the parameter values, after the dashboard is opened in JDashboard, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920398103/btn_dshbrd_prm.gif) on the toolbar to display the  [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009670301-Enter-Parameter-Values) dialog which lists all the parameters used in the dashboard.

The way to specify a parameter value varies with the type and properties of the parameter. Here are several ways you can use to specify parameter values:

* In the parameter value combo box, input the value manually or select the required one from the drop-down list. If you have chosen to [automatically save parameter values](#Auto), the saved value groups will be available on the top of the parameters' value lists for selection.
* Select or unselect the checkbox to specify a Yes/No value.
* Select the button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920430487/btn_chsr1.gif) to specify multiple values in the [Enter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009646022-Enter-Values) dialog.
* Select the calendar button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920401431/btn_clndr.gif) to specify a date and time value using either calendar or expression in the [Calendar](https://devnet.logianalytics.com/hc/en-us/articles/1500009670741-Calendar) dialog. If you use an expression to specify the value, when you hover the mouse pointer on this value, a tip will appear showing its expression. Select on the value, the expression will be displayed in the value text box and you can edit the expression in the text box directly if you want. After editing, when you select elsewhere outside of the value text box:
  + If the edited expression is correct, a new value calculated by the expression will be displayed in the parameter value text box.
  + If the edited expression is wrong, no value will be created and the expression itself will be displayed and highlighted in red in the value text box. Correct the expression, or select the calendar button to specify a value.
* Select the **Use Saved Values**  button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920594583/btn_dshbrd_ussvvlu.gif) and select a previously saved parameter value group to apply to the dashboard. For details, see [Manually saving parameter values](#Manual).

**Tip:** You can customize the [JDashboard profile](https://devnet.logianalytics.com/hc/en-us/articles/1500009669321-Customizing-JDashboard-Profile) to make the Enter Parameter Values dialog display before running dashboards that contain parameters. To do this, go to the Profile > Customize Profile > JDashboard > Properties tab, then check the option **Show Enter Parameter Values Dialog**.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Specifying Parameter Values to a Library Component

You can access the configuration panel of a library component to specify its parameter values. To do this, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404920355095/btn_dshbrd_more.gif) on the [component title bar](https://devnet.logianalytics.com/hc/en-us/articles/1500009644662-General-Operations-in-JDashboard#TitleBar) and select **Edit Setting** from the drop-down menu to display the configuration panel. Specify the values in the panel and select **OK** to apply them to the library component. The Cancel button is used to close the configuration panel.

The **Show the panel by default** option in the panel is used to control whether to show the configuration panel before rendering the library component each time the dashboard is run or refreshed. For example, if a library component uses parameters, and you would like to specify parameter values before loading the component rather than first loading the component and then changing the parameter values so as to run the component the second time to get the desired result, you can check this option to have the panel displayed before rendering by default.

**Note:** You are recommended not to use blank as the thousands separator in Number-typed parameter values under French locale, otherwise your input will not be correctly recognized because of a JVM bug. For details, see <http://bugs.sun.com/view_bug.do;jsessionid=c8cdaf911b20fffffffffd9fc6340b30d670?bug_id=4510618>.

This document also introduces some useful techniques for setting parameter values.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Saving Parameter Values for Reuse

When specifying parameter values for dashboards, you may want to save the specified parameter values for reuse next time. Logi JReport provides two ways of saving. One is users decide when and which parameter values to save, the other is Logi JReport saves each applied or submitted parameter value automatically. When the saved number in either way reaches the maximum, the oldest record will be removed. The number is calculated on a user-dashboard basis. Take a dashboard with two parameters for an example, supposing the maximum number is set to 3. Each user can save at most three groups of parameter values for the dashboard. Each group contains the values of the two parameters.

To switch on the function of saving parameter values, you need to configure the server profile. Go to the Profile > Customize Server Preferences > Advanced tab, select **Yes** to the option [Enable Saving Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#SaveParam), select a way to do the saving: Manually or Automatically, and then specify a maximum number to limit the saved value groups which is called the auto complete parameters list for each user-dashboard pair.

**Manually saving parameter values**

When you have chosen to manually save parameter values, the Use Saved Values button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920594583/btn_dshbrd_ussvvlu.gif) will be available in the Enter Parameter Values dialog. After selecting the button, a drop-down list that contains the lists of previously saved parameter values will be displayed for you to choose one to apply.

![](https://devnet.logianalytics.com/hc/article_attachments/4404920647831/dshbrd_param_vlulst.gif)

The button ![](https://devnet.logianalytics.com/hc/article_attachments/4404920360855/btn_dltobj.gif) next to a drop-down list is used to delete the saved list from the list library.

You can also save the current parameter values as a whole marked as a list for reuse next time, by typing a name for the list in the text box which shows "Save current values into list" and then selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4404926628119/btn_save.gif). The parameter value lists saved for a dashboard are limited. The maximum number is controlled by the option [Maximum Number of Auto Complete Parameters List](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#MaxNo) in the Profile > Customize Server Preferences > Advanced tab. By default it is 3. When the number of the saved parameter value lists reaches the maximum number, if you want to save another parameter value list, it will overwrite the oldest one.

**Using automatically saved parameter values**

When you have chosen to automatically save parameter values, each time a user submits a group of parameter values to a dashboard, the group is saved by Logi JReport automatically. The next time the same user runs the dashboard, the auto saved parameter values will be available in the parameters' value lists for selection in the Enter Parameter Values dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Customizing Default Parameter Values

When specifying parameter values for a dashboard, if you would like the current specified parameter values to be the default selected values in the Enter Parameter Values dialog next time when you run the dashboard, select the **Save as default** option in the dialog (to make this option available, you need to make sure the [Enable Setting Default Parameter Values For Dashboard](https://devnet.logianalytics.com/hc/en-us/articles/1500009644582-Configuring-Server-Profile#DefaultParam) is selected in the Profile > Customize Server Preferences > Advanced tab).

The save as default option is a user-dashboard level setting, that is to say, it takes effect when both the same user and dashboard are matched. This also applies to admin users, and therefore admin cannot customize the setting for all users.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

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

1. Select the **Options** button ![](https://devnet.logianalytics.com/hc/article_attachments/4404926748951/btn_dshbrd_optn.gif) on the toolbar and then select **Share Parameter** from the option list. The [Share Parameters Setting](https://devnet.logianalytics.com/hc/en-us/articles/1500009670481-Share-Parameters-Setting) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404920583191/shareprm.gif)
2. Select the parameters you would like to share by holding the Ctrl key. If the selected parameters support being shared, the Share button will be enabled. Select the button. The parameters will be added into one sharing group.

   To add another parameter into a sharing group, select any parameter in the group while holding Ctrl and then select the parameter, then select **Share**.

   To remove parameters from a sharing group, select the parameters and then select **Cancel Share** which appears in the place of the Share button.
3. Select **OK** to finish.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009669261-Filtering-Component-Data)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009644822-Saving-Dashboards)
