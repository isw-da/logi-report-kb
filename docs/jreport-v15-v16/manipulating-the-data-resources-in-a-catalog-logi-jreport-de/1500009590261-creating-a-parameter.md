---
title: "Creating a Parameter"
id: 1500009590261
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter
updated_at: 2021-07-24T05:54:28Z
---

# Creating a Parameter

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590021-Parameters)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590281-User-Defined-Format-for-Parameters)

# Creating a Parameter

To create a parameter in a catalog, follow the steps below:

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog).
2. In the Catalog Manager, expand the data source in which to create the parameter, then:
   * Select the **Parameters** node or any existing parameter in the data source and select **New Parameter**  on the Catalog Manager toolbar.
   * Right-click the **Parameters** node in the data source and select **New Parameter**  on the shortcut menu.

   he [New Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog) dialog appears.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893825559/nwprm.gif)
3. In the Name field, input a name for the parameter. Since parameters and DBFields share the same name space, you might want to preface parameters with a small "p" such as pStartDate.
4. Select a parameter type from the Value Setting drop-down list: Type-in Parameter, Bind with Single Column or Bind with Cascading Columns.
5. In the values section, specify the parameter values as required. The section varies with the type you select from the Value Setting drop-down list.
   * **For Type-in Parameter:**
     1. Specify the data type of the parameter value from the Value Type drop-down list.
     2. If you want to provide the user with a default value, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a value line, select on the new line and then type in a value of the specified data type.

        If the parameter is of Date, DateTime, or Time type, you can also select the calendar button ![Calendar button](https://devnet.logianalytics.com/hc/article_attachments/4404889299735/btn_clndr.gif) to set a date and time value using either calendar or [built-in formula functions](https://devnet.logianalytics.com/hc/en-us/articles/1500009590141-Using-Built-in-Functions-to-Set-Date-and-Time-Parameter-Values).
     3. Repeat the second step to add more values.

        To adjust the order of the values, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif); to remove any unwanted value, select it in the list and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif).
     4. To make a value the default selected value in the Enter Parameter Value dialog, select it from the list.
   * **For Bind with Single Column:**
     1. From the Source drop-down list, select the required data source type: Tables and Views (including synonyms), Stored Procedures, Imported SQLs, or User Defined then all fields in the specified catalog data source of this type will be available for value selection.
     2. Select a field from the Bind Column drop-down list. At runtime, end users will see a list containing all the distinct values in this field. For example State would show a list of states the users can choose from.
     3. If you want the values of another field to be displayed in the Enter Parameter Values dialog, which has more meaning to the end users than the values of the Bind Column field, select that field from the Display Column drop-down list. For example you may bind the Customer ID column but want to display the full customer names for end users to choose from. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009590081-Binding-a-Parameter-to-a-DBField) for an example.
   * **For Bind with Cascading Columns:**
     1. From the Data Source drop-down list, select the required data source from which to get the columns. You can get data from a table, view, synonym, stored procedure, imported SQL, or user defined data source.
     2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a parameter row.
     3. Select in the Bind Column cell and select a field from the drop-down list.
     4. If you want the values of another field to be displayed in the Enter Parameter Values dialog, which has more meaning to the end users than the values of the Bind Column field, select in the Display Column cell and then select that field from the drop-down list.
     5. Select in the Parameter cell to create the parameter. A name for the parameter will then be automatically added by Logi JReport.
     6. Repeat steps b to e to create more parameters. Make sure that the selected Bind Column fields are of a cascading hierarchy. In this way, a group of cascading parameters are created. For example, the parameter group could first be by State followed by County and then by City. Select [here](https://devnet.logianalytics.com/hc/en-us/articles/1500009568642-Filtering-a-Parameter-with-Another-Parameter) for an example.

        To adjust the order of the parameters, select ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif) or ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif); to remove any unwanted parameter from the cascading group, select it and then select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif).
6. In the Options box, set [options](https://devnet.logianalytics.com/hc/en-us/articles/1500009566822-New-Parameter-Dialog#Options) for the parameter according to your requirements.
7. When done, select **OK** to create the parameter.

**Notes:**

* When you create a parameter in a catalog data source that contains only XML connections, the parameter type Bind with Cascading Columns is not supported.
* If a parameter is added in a catalog data source that contains only MongoDB connections, only tables and user defined data sources can be used to bind with the parameter.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590021-Parameters)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009590281-User-Defined-Format-for-Parameters)
