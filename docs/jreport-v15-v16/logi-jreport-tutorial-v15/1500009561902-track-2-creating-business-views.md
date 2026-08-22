---
title: "Track 2: Creating Business Views"
id: 1500009561902
section: "Logi JReport Tutorial v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009561902-Track-2-Creating-Business-Views
updated_at: 2021-07-24T05:56:27Z
---

# Track 2: Creating Business Views

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562042-Lesson-9-Creating-a-Parameter-based-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562062-Track-3-Creating-Web-Reports)

# Track 2: Creating Business Views

Business views are the data sources used for creating [web reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009562062-Track-3-Creating-Web-Reports) and [library components](https://devnet.logianalytics.com/hc/en-us/articles/1500009561942-Track-4-Creating-Library-Components) in Logi JReport Designer, as well as creating ad hoc reports and performing visual analysis in Logi JReport Server. They enable report developers and end users to build reports and analyze data based on a set of view elements that they can easily understand. For example, they do not need to worry about where the data source is from (SQL, stored procedure, view, etc.), or what the data source is (Oracle, Sybase, XML, etc.). Business views also enable IT professionals to maintain control of business data and to ensure its integrity, while presenting end users with an intuitive view of the underlying data.

Business views are created and managed in Logi JReport Designer. A business view is built from four kinds of elements:

* **Group objects** are typically DBFields and formulas by which you want to group data. They present the availability and key performance of data, and characteristically return text data or dates, and answer the following question: who, when, what, where and which.
* **Aggregation objects** are typically numeric DBFields and formulas to which an aggregate function, such as Sum, is applied or they can be an existing aggregation from the catalog.
* **Detail objects** can be any DBField or formula, typically they are values that you would want to display in the Detail section of a table. They can not be used in charts and crosstabs.
* **Categories** are simply folders for organizing the other three elements.

A business view can also contain hierarchies. A hierarchy is defined as a hierarchy category holding one group of group objects sharing a hierarchical relationship, following the order from the highest level to the lowest. Hierarchies allow end users to drill report data up and down to particular groups at runtime.

In this track, we will create a business view based on data in Data Source 1 of the JinfonetGourmetJava catalog, which provides data information about customers, orders, orders detail and products.

This track contains the following tasks:

* [Task 1: Create the Business View](#Task1)
* [Task 2: Add Elements to the Business View](#Task2)
* [Task 3: Define Hierarchies in the Business View](#Task3)

**Note:** A Logi JReport Live license for Logi JReport Designer is required in order to perform this track. If you do not have the license, please contact your Jinfonet Software account manager to obtain it first.

## Task 1: Create the Business View

In this task we will create the business view to include the needed tables.

1. Select **Start** > **Logi JReport 15** > **Report Designer** to start Logi JReport Designer. The Logi JReport Designer window with the Start Page appears. Close the Start Page.
2. Select **File** > **Open Catalog** to bring out the Open Catalog File dialog.
3. Browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select the **Open** button. The Catalog Manager is displayed.
4. Expand the **Data Source 1** node, then right-click the **Business View**  node and select **New Business View**  on the shortcut menu.

   ![New Business View](https://devnet.logianalytics.com/hc/article_attachments/4404894048023/bv_addbv.gif)
5. Type in **WorldWideSalesBV** in the Enter Business View Name dialog and select **OK**.
6. In the Add Tables/Views/Queries dialog, expand the JDBC connection node and then the **Tables** node, then select these tables: **Customers**, **Orders**, **Orders Detail** and **Products**, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404889454231/btn_add.gif) to add them to the right box, then select **OK**.

   ![Add Tables](https://devnet.logianalytics.com/hc/article_attachments/4404894048279/bv_adddt.gif)
7. The four added tables are displayed with their columns and automatically joined based on the auto join criteria in the Query Editor.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404889454487/bv_qryedtr.gif)
8. In the Customers table, check the **\*** checkbox to select all columns in the table, then uncheck these columns: **Address2**, **Customers\_Fax**, and **Annual Sales**. In the Orders table, select **Orders\_Order ID**, **Order Date**, and **Payment Received**. In the Orders Detail table, select **Unit Price**, **Quantity**, and **Discount**. In the Products table, select all its columns first by checking \*, then unselect **Inventory** and **Reorder Level**.
9. Select **OK** at the bottom of the Query Editor.

   The Business View Editor is then displayed. The tables and table columns selected in steps 6 and 8 are displayed in the Resource Objects panel in the editor, and the formulas and summaries that are valid to them are also available in the panel. We can then create view elements based on these resources.

## Task 2: Add Elements to the Business View

We will create three categories in the business view to hold customer, order and product information respectively.

1. In the Business View panel of the Business View Editor, select **WorldWideSalesBV** and right-click, then select **Add Category** from the shortcut menu.

   ![Add Category](https://devnet.logianalytics.com/hc/article_attachments/4404894048535/bv_ctg.gif)
2. In the Category Property dialog, input **Customers** as the Display Name, then select **OK**.
3. Expand the **WorldWideSalesBV** node in the Business View panel to display the newly added category.
4. Expand the **Customers** table in the Resource Objects panel, select the fields **Customer Name**, **Customers\_City**, **Customers\_Country**, **Customers\_Region**, **Customers\_State**, and **Customers\_Territory** in the table, then drag them into the Customers category in the Business View panel.

   ![Add Element for Customer](https://devnet.logianalytics.com/hc/article_attachments/4404894048791/bv_cstm1.gif)
5. Change their display names using the shortcut menu option Rename to **City**, **Country**, **Region**, **State**, and **Territory**, by removing "Customers\_". Then select **Customer Name** and select ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404894049047/btn_down.gif) twice to move it below Country to make the objects displayed in alphabetical order.

   ![Edit Name and Position](https://devnet.logianalytics.com/hc/article_attachments/4404894049303/bv_cstm2.gif)
6. Select the **Customers** category and select **New Category** on the toolbar to create a sub category **Address** in it, which will used to hold address information. Move the Address category above the City group object by using the button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404894049559/btn_up.gif).

   ![Address Category](https://devnet.logianalytics.com/hc/article_attachments/4404894049815/bv_cstm3.gif)
7. From the Customers table in the Resource Objects panel, select **Address1**, **Customers\_Country**, **Customer Name**, and **Customers\_Phone** and drag them into the Address category.

When adding elements to a business view by dragging DBFields from the Resource Objects panel, the elements will be used as Group object by default. So next we will manually edit the type of the elements in the Address category to Detail so that they can be used to show detail information in reports.

1. Select **Customers\_Country**, right-click it and select **Edit** on the shortcut menu. In the Edit View Element dialog, edit its display name to **Country** and type to **Detail**, then select **OK**. Edit the display name of Customers\_Phone to **Phone** and type to **Detail** using the same way.
   Then select **Address1** and **Customer Name**, right-click and select **Edit** to edit their type to **Detail** at the same time in the Edit View Element dialog**.** 

   ![Change Element Type](https://devnet.logianalytics.com/hc/article_attachments/4404889454743/bv_cstm4.gif)

By now the Customers category is finished. Next, we are going to create the Orders Detail category.

1. Select **WorldWideSalesBV** in the Business View panel, then select **New Category** on the toolbar to create a category **Orders Detail**. Add these fields from the Resource Objects panel into the category: all the fields from the Orders and Orders Detail tables, and Cost from the Products table. Use the shortcut menu option Rename to edit the display name of Orders\_Order ID to **Order ID**. Arrange the order of the added fields to make them sorted in alphabetical order. Edit the type of Cost, Discount, Order Date, Quantity and Unit Price to **Detail** using the Edit View Element dialog.
   See the result:

   ![Define the Orders Detail Category](https://devnet.logianalytics.com/hc/article_attachments/4404889454999/bv_ord.gif)

View elements can also be added into a business view by using a dialog instead of dragging and dropping. Next, we are going to add more objects to the Order Detail category using a dialog.

1. Select the **Orders Detail** category, right-click it and select **Add View Element** from the shortcut menu.
2. In the Add View Element dialog, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404894050199/btn_chsr.gif) next to the Mapping Name text field, in the View Element Resources dialog expand the **Formulas** node and double-click **Total** to add it as the mapping field, then set Type to **Detail** and select **OK** to create the detail object.

   ![Add Total as Element](https://devnet.logianalytics.com/hc/article_attachments/4404889455255/bv_fmla.gif)
3. Select the **Orders Detail** category again and select **New Aggregation** on the toolbar.
4. In the Add View Element dialog, type **Total Cost** in the Display Name text field, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404894050199/btn_chsr.gif) next to the Mapping Name text field to double-click **Cost** in the Products table, select **Sum** from the Aggregate Function drop-down list. Select **OK** to create the aggregation.

   ![Create Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404894050455/bv_ord1.gif)
5. Create another two aggregations **Total Quantity** which sums on Quantity and **Total Sales** which sums on the formula **Total** using the same way.
6. Arrange the objects in the Orders Detail category in alphabetical order:

   ![Arrange the Orders Detail Category](https://devnet.logianalytics.com/hc/article_attachments/4404889455767/bv_ord4.gif)

Next, we will create the Products category to hold product related information.

1. Create a category **Products** in WorldWideSalesBV, add **Category**, **Product Name**, **Product Type Name**, and **Products\_Product ID** from the Products table in the Resource Objects panel to it, modify the display names of Product Type Name to **Product Type** and Products\_Product ID to **Product ID**, then arrange the objects in alphabetical order.

   ![Create the Products Category](https://devnet.logianalytics.com/hc/article_attachments/4404889456023/bv_pro.gif)
2. Select **Save** on the Business View Editor toolbar to save the business view.

## Task 3: Define Hierarchies in the Business View

In this task, we will define two hierarchies in the business view: one containing customer's geographic information, from region down to city, and the other product's hierarchical groups.

1. In the Business View Editor, select**WorldWideSalesBV**in the Business View panel, then select **New****Hierarchy**on the toolbar.
2. In the New Hierarchy dialog, input **Geography** and select **OK**. The Geography hierarchy node is then added at the bottom under the business view root node.
3. In the Business View panel, drag these objects **Region**, **Territory**, **Country**, **State** and **City** from the Customers category one by one following this order to the Geography hierarchy node. Region will be the highest level and City the lowest.
4. Follow steps 1 to 3 to create another hierarchy named **Product**, then add **Product Type**, **Category** and **Product Name** to the hierarchy.

   Now, two hierarchies have been defined in the business view.

   ![Create Hierarchies](https://devnet.logianalytics.com/hc/article_attachments/4404894050711/bv_hrchy.gif)
5. Save the business view to save the hierarchies, then close the Business View Editor.
6. Select **Save Catalog** on the Catalog Manager toolbar to save the business view into the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404893760791/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562042-Lesson-9-Creating-a-Parameter-based-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404893761047/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562062-Track-3-Creating-Web-Reports)
