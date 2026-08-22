---
title: "Track 2: Creating Business Views"
id: 1500009604602
section: "Logi Report Tutorial v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009604602-Track-2-Creating-Business-Views
updated_at: 2021-07-24T16:05:34Z
---

# Track 2: Creating Business Views

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009627741-Lesson-9-Creating-a-Parameter-Based-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604762-Track-3-Creating-Web-Reports)

# Track 2: Creating Business Views

[Business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009627961-Business-Views) are the data sources used for creating interactive reports and perform dynamic analysis in Logi Report. They enable report developers and end users to build reports and analyze data based on a set of view elements that they can easily understand. For example, they do not need to worry about where the data source is from (SQL, stored procedure, view, etc.), or what the data source is (Oracle, Sybase, XML, etc.). Business views also enable IT professionals to maintain control of business data and to ensure its integrity, while presenting end users with an intuitive view of the underlying data.

In this track, you will create a business view as a report developer using the data in the Jinfonet Gourmet Java company's database, which provides information about customers, orders, orders detail, and products.

This track contains the following tasks:

* [Task 1: Create the Business View](#Task1)
* [Task 2: Add Elements to the Business View](#Task2)
* [Task 3: Define Hierarchies in the Business View](#Task3)

**Note:** A Logi Report Live license for Logi Report Designer is required in order to perform this track. If you do not have the license, please contact your Logi Analytics account manager to obtain it first.

## Task 1: Create the Business View

In this task we will create the business view to include the needed tables.

1. Select **Logi Report Designer** in the Logi Report folder on the Start menu to start Logi Report Designer.

   The Logi Report Designer window appears, with the Start Page shown by default. Close the Start Page.
2. Select **File** > **Open Catalog** to bring out the Open Catalog File dialog box.
3. Browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select the **Open** button. The Catalog Manager is displayed.
4. Expand the **Data Source 1** node, then right-click the **Business View**  node and select **New Business View**  on the shortcut menu.

   ![New Business View](https://devnet.logianalytics.com/hc/article_attachments/4404916881815/bv_addbv.gif)
5. Type **WorldWideSalesBV** in the Enter Business View Name dialog box and select **OK**.
6. In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the **Tables** node, select these tables while holding the Ctrl key on the keyboard: **Customers**, **Orders**, **Orders Detail** and **Products**, then select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404904583191/btn_add.gif) to add them to the right box. Select **OK** to close the dialog box.

   ![Add Tables](https://devnet.logianalytics.com/hc/article_attachments/4404904583447/bv_adddt.gif)

   Logi Report Designer allows you to combine tables, views, synonyms, queries, imported SQLs, stored procedures, and user defined data sources into a business view to mash up multiple data resources in a single business view, and create distributed joins to set up inter-relationships between the data resources. In this example we only use tables for the business view.
7. The four added tables are displayed with their columns and automatically joined based on the auto join criteria in the Query Editor (you can view the join options from the Query > Auto Join menu).

   ![Query Editor](https://devnet.logianalytics.com/hc/article_attachments/4404916882327/bv_qryedtr.gif)
8. In the Customers table, select the top checkbox to select all columns in the table, then clear these columns: **Address2**, **Customers\_Fax**, and **Annual Sales**. In the Orders table, select **Orders\_Order ID**, **Order Date**, and **Payment Received**. In the Orders Detail table, select **Unit Price**, **Quantity**, and **Discount**. In the Products table, select all its columns first by selecting the top checkbox, then clear **Inventory** and **Reorder Level**.
9. Select **OK** at the bottom of the Query Editor to finish selecting data resources for the business view.

   The Business View Editor is displayed. The selected tables and table columns are displayed in the Resource Objects panel in the editor, and the formulas and summaries that are valid to them are also available in the panel. We can then create view elements based on these resources.

   ![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404904583703/bv_bvedtr.gif)

## Task 2: Add Elements to the Business View

We will create three categories in the business view to hold customer, order, and product information respectively.

1. Select **New Category** on the Business View Editor toolbar.
2. In the Category Property dialog box, type **Customers** as the Display Name, then select **OK**.
3. Expand the **WorldWideSalesBV** node in the Business View panel to display the newly added category.

   ![New Category](https://devnet.logianalytics.com/hc/article_attachments/4404904583959/bv_ctgry.gif)
4. Expand the **Customers** table in the Resource Objects panel, select the fields **Customer Name**, **Customers\_City**, **Customers\_Country**, **Customers\_Region**, **Customers\_State**, and **Customers\_Territory** in the table, then drag them into the Customers category in the Business View panel.

   ![Add Element for Customer](https://devnet.logianalytics.com/hc/article_attachments/4404904584215/bv_cstmr.gif)
5. Right-click the **Customers** category and select **New Category** from the shortcut menu to create a sub category **Address** in it, which will be used to hold address information.
6. From the Customers table in the Resource Objects panel, select **Address1**, **Customers\_Country**, **Customer Name**, and **Customers\_Phone** and drag them into the Address category.

When adding elements to a business view by dragging DBFields from the Resource Objects panel, the elements will be used as Group object by default. Next we will manually edit the type of the elements in the Address category to Detail so that they can be used to show detail information in reports.

1. Select the four elements in the Address category, right-click them and select **Edit** on the shortcut menu. In the Edit View Element dialog box, select **Detail** from the Type drop-down list and select **OK**. Via the dialog box you can edit the Type, Tip, and Description properties of multiple view elements at the same time.

   ![Edit View Element](https://devnet.logianalytics.com/hc/article_attachments/4404916882583/bv_edtvw.gif)

   The Address category now contains four detail objects as follows:

   ![Address Category](https://devnet.logianalytics.com/hc/article_attachments/4404916882839/bv_adrs.gif)

By now the Customers category with the Address sub category is finished. Next, we are going to create the Orders Detail category.

1. Select **WorldWideSalesBV** in the Business View panel, then select **New Category** on the toolbar to create a category **Orders Detail**.
2. Add the following fields from the Resource Objects panel into the category: all the fields from the Orders and Orders Detail tables, and Cost from the Products table. Rename Orders\_Order ID to **Order ID**. Arrange the order of the added objects to make them sorted in alphabetical order. Edit the type of Cost, Discount, Order Date, Quantity, and Unit Price to Detail using the Edit View Element dialog box [as shown above](#EditType). See the result:

   ![Define the Orders Detail Category](https://devnet.logianalytics.com/hc/article_attachments/4404904584855/bv_order1.gif)

View elements can also be added into a business view by using dialog box in addition to dragging and dropping. Next, we are going to add more elements to the Orders Detail category via dialog box.

1. Select the **Orders Detail** category and select **New Detail** on the toolbar.
2. In the New View Element dialog box, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404916883095/btn_chsr.gif) next to the Mapping Name text box. In the View Element Resources dialog box expand the **Formulas** node and double-click **Total** to add it as the mapping field. Select **OK** to create the element.

   ![Add Total as Element](https://devnet.logianalytics.com/hc/article_attachments/4404904585495/bv_total.gif)
3. Select the **Orders Detail** category again, right-click it and select **New View Element** from the shortcut menu.
4. In the New View Element dialog box, type **Total Cost** in the Display Name text box, select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404916883095/btn_chsr.gif) next to the Mapping Name text box and select **Cost** in the Products table as the mapping field, select **Aggregation** from the Type drop-down list, then select **Sum** from the Aggregate Function drop-down list. Select **OK** to create the aggregation.

   ![Create Cost Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404904585879/bv_cost.gif)
5. Create another two aggregations **Total Quantity** which sums on Quantity and **Total Sales** which sums on the formula **Total** using the same way.

   The Orders Detail category now contains the following elements:

   ![Arrange the Orders Detail Category](https://devnet.logianalytics.com/hc/article_attachments/4404904586135/bv_order2.gif)

Next, we will create the Products category to hold product related information.

1. Select **WorldWideSalesBV** in the Business View panel and select **New Category** on the toolbar to create a category **Products**, drag **Category**, **Product Name**, **Product Type Name**, and **Products\_Product ID** from the Products table in the Resource Objects panel to it, then right-click **Product Type Name** and select **Rename** from the shortcut menu to edit its display name to **Product Type**.

   ![Create the Products Category](https://devnet.logianalytics.com/hc/article_attachments/4404904586391/bv_prdct.gif)
2. Click the **Sort** button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404904586647/btn_sort.gif) at the upper right corner of the Business View panel and select **Ascending** from the drop-down menu to sort the elements that have been added to the business view in the ascending order.
3. Click **Save** on the Business View Editor toolbar to save the business view.

## Task 3: Define Hierarchies in the Business View

In this task, we will define two hierarchies in the business view: one containing customer's geographic information, from region down to city, and the other product's hierarchical groups.

1. In the Business View Editor, select **WorldWideSalesBV** in the Business View panel, then select **New Hierarchy** on the toolbar.
2. In the New Hierarchy dialog box, type **Geography** and select **OK**. The Geography hierarchy node is then added at the bottom under the business view root node.
3. In the Business View panel, drag these group objects **Region**, **Territory**, **Country**, **State** and **City** from the Customers category one by one following this order to the Geography hierarchy node. Region is the highest level and City the lowest.
4. Follow steps 1 to 3 to create another hierarchy named **Product** and add **Product Type**, **Category** and **Product Name** in the Products category to the hierarchy.

   Now, two hierarchies have been defined in the business view.

   ![Create Hierarchies](https://devnet.logianalytics.com/hc/article_attachments/4404904587031/bv_hrchy.gif)
5. Save the business view to save the hierarchies, then close the Business View Editor.
6. Select **Save Catalog** on the Catalog Manager toolbar to save the business view into the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911569687/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009627741-Lesson-9-Creating-a-Parameter-Based-Report) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911569943/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009604762-Track-3-Creating-Web-Reports)
