---
title: "Track 2: Creating Business Views"
id: 1500011431502
section: "Logi JReport Tutorial v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500011431502-Track-2-Creating-Business-Views
updated_at: 2021-07-24T10:39:41Z
---

# Track 2: Creating Business Views

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011463441-Lesson-9-Creating-a-Parameter-Based-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901097111/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463421-Track-3-Creating-Web-Reports)

# Track 2: Creating Business Views

[Business views](https://devnet.logianalytics.com/hc/en-us/articles/1500011431322-Business-Views) are the data sources used for creating interactive reports and perform dynamic analysis in Logi JReport. They enable report developers and end users to build reports and analyze data based on a set of view elements that they can easily understand. For example, they do not need to worry about where the data source is from (SQL, stored procedure, view, etc.), or what the data source is (Oracle, Sybase, XML, etc.). Business views also enable IT professionals to maintain control of business data and to ensure its integrity, while presenting end users with an intuitive view of the underlying data.

In this track, you will create a business view as a report developer using the data in the Jinfonet Gourmet Java company's database, which provides information about customers, orders, orders detail and products.

This track contains the following tasks:

* [Task 1: Create the Business View](#Task1)
* [Task 2: Add Elements to the Business View](#Task2)
* [Task 3: Define Hierarchies in the Nusiness View](#Task3)

**Note:** A Logi JReport Live license for Logi JReport Designer is required in order to perform this track. If you do not have the license, please contact your Logi Analytics account manager to obtain it first.

## Task 1: Create the Business View

In this task we will create the business view to include the needed tables.

1. Select **JReport Designer** in the JReport folder on the Start menu to start Logi JReport Designer.

   The Logi JReport Designer window with the Start Page appears. Close the Start Page.
2. Select **File** > **Open Catalog** to bring out the Open Catalog File dialog.
3. Browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select the **Open** button. The Catalog Manager is displayed.
4. Expand the **Data Source 1** node, then right-click the **Business View**  node and select **New Business View**  on the shortcut menu.

   ![New Business View](https://devnet.logianalytics.com/hc/article_attachments/4404909104023/bv_addbv.gif)
5. Type in **WorldWideSalesBV** in the Enter Business View Name dialog and select **OK**.
6. In the Add Tables/Views/Queries dialog, expand the JDBC connection node and then the **Tables** node, select these tables while holding the Ctrl key on the keyboard: **Customers**, **Orders**, **Orders Detail** and **Products**, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404909104279/btn_add.gif) to add them to the right box. select **OK** to close the dialog.

   ![Add Tables](https://devnet.logianalytics.com/hc/article_attachments/4404901100567/bv_adddt.gif)

   Logi JReport Designer allows you to combine tables, views, synonyms, queries, imported SQLs, stored procedures and user defined data sources into a business view to mash up multiple data resources in a single business view, and create distributed joins to set up inter-relationships between the data resources. In this example we only use tables for the business view.
7. The four added tables are displayed with their columns and automatically joined based on the auto join criteria in the Query Editor (you can view the join options from the Query > Auto Join menu).

   ![Query Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901100823/bv_qryedtr.gif)
8. In the Customers table, check the **\*** checkbox to select all columns in the table, then uncheck these columns: **Address2**, **Customers\_Fax**, and **Annual Sales**. In the Orders table, select **Orders\_Order ID**, **Order Date**, and **Payment Received**. In the Orders Detail table, select **Unit Price**, **Quantity**, and **Discount**. In the Products table, select all its columns first by checking \*, then unselect **Inventory** and **Reorder Level**.
9. Select **OK** at the bottom of the Query Editor to finish selecting data resources for the business view.

   The Business View Editor is displayed. The selected tables and table columns are displayed in the Resource Objects panel in the editor, and the formulas and summaries that are valid to them are also available in the panel. We can then create view elements based on these resources.

   ![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404909104535/bv_bvedtr.gif)

## Task 2: Add Elements to the Business View

We will create three categories in the business view to hold customer, order and product information respectively.

1. Select **New Category** on the Business View Editor toolbar.
2. In the Category Property dialog, input **Customers** as the Display Name, then select **OK**.
3. Expand the **WorldWideSalesBV** node in the Business View panel to display the newly added category.

   ![New Category](https://devnet.logianalytics.com/hc/article_attachments/4404901101079/bv_ctgry.gif)
4. Expand the **Customers** table in the Resource Objects panel, select the fields **Customer Name**, **Customers\_City**, **Customers\_Country**, **Customers\_Region**, **Customers\_State**, and **Customers\_Territory** in the table, then drag them into the Customers category in the Business View panel.

   ![Add Element for Customer](https://devnet.logianalytics.com/hc/article_attachments/4404901101335/bv_cstmr1.gif)
5. Change the display names of the added objects using the shortcut menu option Rename to **City**, **Country**, **Region**, **State**, and **Territory**, by removing "Customers\_". Then select **Customer Name** and select ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404909104791/btn_down.gif) twice to move it below Country to make the objects displayed in alphabetical order.

   ![Edit Name and Position](https://devnet.logianalytics.com/hc/article_attachments/4404901101719/bv_cstmr2.gif)
6. Select the **Customers** category, right-click it and select **New Category** from the shortcut menu to create a sub category **Address** in it, which will be used to hold address information. Move the Address category above the City group object by using the button ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404901101975/btn_up.gif).

   ![Address Category](https://devnet.logianalytics.com/hc/article_attachments/4404909105175/bv_adrs1.gif)
7. From the Customers table in the Resource Objects panel, select **Address1**, **Customers\_Country**, **Customer Name**, and **Customers\_Phone** and drag them into the Address category.

When adding elements to a business view by dragging DBFields from the Resource Objects panel, the elements will be used as Group object by default. Next we will manually edit the type of the elements in the Address category to Detail so that they can be used to show detail information in reports.

1. Select the four elements in the Address category, right-click them and select **Edit** on the shortcut menu. In the Edit View Element dialog, select Detail from the Type drop-down list and select **OK**. Via the dialog you can edit the Type, Tip and Description properties of multiple view elements at the same time.

   ![Edit View Element](https://devnet.logianalytics.com/hc/article_attachments/4404901102359/bv_edtvw.gif)
2. Right-click **Customers\_Country** and select **Rename** from the shortcut menu to change its display name to **Country**. Rename **Customers\_Phone** to **Phone** in the same way.

   The Address category now contains four detail objects as follows:

   ![Elements in the Address Category](https://devnet.logianalytics.com/hc/article_attachments/4404909105431/bv_adrs2.gif)

By now the Customers category with the Address sub category is finished. Next, we are going to create the Orders Detail category.

1. Select **WorldWideSalesBV** in the Business View panel, then select **New Category** on the toolbar to create a category **Orders Detail**.
2. Add the following fields from the Resource Objects panel into the category: all the fields from the Orders and Orders Detail tables, and Cost from the Products table. Rename Orders\_Order ID to **Order ID**. Arrange the order of the added objects to make them sorted in alphabetical order. Edit the type of Cost, Discount, Order Date, Quantity and Unit Price to **Detail** using the Edit View Element dialog.
   See the result:

   ![Define the Orders Detail Category](https://devnet.logianalytics.com/hc/article_attachments/4404909105687/bv_order1.gif)

View elements can also be added into a business view by using dialog in addition to dragging and dropping. Next, we are going to add more elements to the Orders Detail category via dialog.

1. Select the **Orders Detail** category and select **New Detail** on the toolbar.
2. In the New View Element dialog, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901102615/btn_chsr.gif) next to the Mapping Name text box. In the View Element Resources dialog expand the **Formulas** node and double-click **Total** to add it as the mapping field. select **OK** to create the element.

   ![Add Total as Element](https://devnet.logianalytics.com/hc/article_attachments/4404901102871/bv_total.gif)
3. Select the **Orders Detail** category again, right-click it and select **New View Element** from the shortcut menu.
4. In the New View Element dialog, type **Total Cost** in the Display Name text box, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404901102615/btn_chsr.gif) next to the Mapping Name text box and select **Cost** in the Products table as the mapping field, select **Aggregation** from the Type drop-down list, then select **Sum** from the Aggregate Function drop-down list. select **OK** to create the aggregation.

   ![Create Cost Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404909105943/bv_cost.gif)
5. Create another two aggregations **Total Quantity** which sums on Quantity and **Total Sales** which sums on the formula **Total** using the same way.
6. Arrange the elements in the Orders Detail category in alphabetical order:

   ![Arrange the Orders Detail Category](https://devnet.logianalytics.com/hc/article_attachments/4404909106199/bv_order2.gif)

Next, we will create the Products category to hold product related information.

1. Select **WorldWideSalesBV** in the Business View panel and select **New Category** on the toolbar to create a category **Products**, drag **Category**, **Product Name**, **Product Type Name**, and **Products\_Product ID** from the Products table in the Resource Objects panel to it, modify the display names of Product Type Name to **Product Type** and Products\_Product ID to **Product ID**, then arrange the elements in alphabetical order.

   ![Create the Products Category](https://devnet.logianalytics.com/hc/article_attachments/4404909106455/bv_prdct.gif)
2. Select **Save** on the Business View Editor toolbar to save the business view.

## Task 3: Define Hierarchies in the Business View

In this task, we will define two hierarchies in the business view: one containing customer's geographic information, from region down to city, and the other product's hierarchical groups.

1. In the Business View Editor, select**WorldWideSalesBV**in the Business View panel, then select **New****Hierarchy**on the toolbar.
2. In the New Hierarchy dialog, input **Geography** and select **OK**. The Geography hierarchy node is then added at the bottom under the business view root node.
3. In the Business View panel, drag these group objects **Region**, **Territory**, **Country**, **State** and **City** from the Customers category one by one following this order to the Geography hierarchy node. Region is the highest level and City the lowest.
4. Follow steps 1 to 3 to create another hierarchy named **Product** and add **Product Type**, **Category** and **Product Name** in the Products category to the hierarchy.

   Now, two hierarchies have been defined in the business view.

   ![Create Hierarchies](https://devnet.logianalytics.com/hc/article_attachments/4404901103127/bv_hrchy.gif)
5. Save the business view to save the hierarchies, then close the Business View Editor.
6. Select **Save Catalog** on the Catalog Manager toolbar to save the business view into the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404909062551/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500011463441-Lesson-9-Creating-a-Parameter-Based-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901097111/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500011463421-Track-3-Creating-Web-Reports)
