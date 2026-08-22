---
title: "Track 2: Creating Business Views"
id: 1500009770061
section: "Part III: Advanced Reporting"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009770061-Track-2-Creating-Business-Views
updated_at: 2021-07-24T00:49:52Z
---

# Track 2: Creating Business Views

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009770141-Lesson-9-Creating-a-Parameter-Based-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009742382-Track-3-Creating-Web-Reports)

# Track 2: Creating Business Views

[Business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009742582-Business-Views) are the data sources used for creating interactive reports and perform dynamic analysis in Logi Report. They enable report developers and end users to build reports and analyze data based on a set of view elements that they can easily understand. For example, they do not need to worry about where the data source is from (SQL, stored procedure, view, etc.), or what the data source is (Oracle, Sybase, XML, etc.). Business views also enable IT professionals to maintain control of business data and to ensure its integrity, while presenting end users with an intuitive view of the underlying data.

In this track, you will create a business view as a report developer using the data in the Jinfonet Gourmet Java company's database, which provides information about customers, orders, orders detail, and products.

This track contains the following tasks:

* [Task 1: Create the Business View](#Task1)
* [Task 2: Add Elements to the Business View](#Task2)
* [Task 3: Define Hierarchies in the Business View](#Task3)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404885352855/criticalicon.gif) A Live license for Designer is required in order to perform this track. If you do not have the license, please contact your Logi Analytics account manager to obtain it first.

## Task 1: Create the Business View

In this task we will create the business view to include the needed tables.

1. Select **Logi Report Designer** in the Logi Report folder on the Start menu to start Designer.

   Designer displays the main window and shows the Start Page by default. Close the Start Page.
2. Select **File** > **Open Catalog** to bring out the Open Catalog File dialog box.
3. Browse to select the **JinfonetGourmetJava.cat** catalog file in `<install_root>\Demo\Reports\JinfonetGourmetJava`, then select the **Open** button. Designer displays the Catalog Manager.
4. Expand the **Data Source 1** node, then right-click the **Business View**  node and select **New Business View**  on the shortcut menu.

   ![New Business View](https://devnet.logianalytics.com/hc/article_attachments/4404880708631/bv_addbv.gif)
5. Type **WorldWideSalesBV** in the Enter Business View Name dialog box and select **OK**.
6. In the Add Tables/Views/Queries dialog box, expand the JDBC connection node and then the **Tables** node, select these tables while holding the Ctrl key on the keyboard: **Customers**, **Orders**, **Orders Detail**, and **Products**, then select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404885696919/btn_add.gif) to add them to the right box. Select **OK** to close the dialog box.

   ![Add Tables](https://devnet.logianalytics.com/hc/article_attachments/4404885697175/bv_adddt.gif)

   Designer enables you to combine tables, views, synonyms, queries, imported SQLs, stored procedures, and user-defined data sources into a business view to mash up multiple data resources in a single business view, and create distributed joins to set up inter-relationships between the data resources. In this example, we only use tables for the business view.
7. Designer displays the four tables with their columns and automatically joins them based on the auto join criteria in the Query Editor dialog box (you can view the join options from the Query > Auto Join menu).

   ![Query Editor](https://devnet.logianalytics.com/hc/article_attachments/4404880708887/bv_qryedtr.gif)
8. In the **Customers** table, select the top check box to select all columns in the table, then clear these columns: **Address2**, **Customers\_Fax**, and **Annual Sales**; in the **Orders** table, select **Orders\_Order ID**, **Order Date**, and **Payment Received**; in the **Orders Detail** table, select **Unit Price**, **Quantity**, and **Discount**; in the **Products** table, select all its columns first by selecting the top check box, then clear **Inventory** and **Reorder Level**.
9. Select **OK** at the bottom of the Query Editor dialog box to finish selecting data resources for the business view.

   Designer displays the Business View Editor dialog box, showing the selected tables and table columns, as well as the formulas and summaries that are valid to them, in the Resource Objects panel in the dialog box. We can now create view elements based on these resources.

   ![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404880709143/bv_bvedtr.gif)

## Task 2: Add Elements to the Business View

In this task, we create three categories in the business view to hold customer, order, and product information respectively.

1. Select **New Category** on the toolbar of the Business View Editor dialog box.
2. In the Category Property dialog box, type **Customers** in the **Display Name** text box, then select **OK**.
3. Expand the **WorldWideSalesBV** node in the Business View panel to display the newly added category.

   ![New Category](https://devnet.logianalytics.com/hc/article_attachments/4404880709399/bv_ctgry.gif)
4. Expand the **Customers** table in the Resource Objects panel, select the fields **Customer Name**, **Customers\_City**, **Customers\_Country**, **Customers\_Region**, **Customers\_State**, and **Customers\_Territory** in the table, then drag them into the Customers category in the Business View panel.

   ![Add Element for Customer](https://devnet.logianalytics.com/hc/article_attachments/4404880709655/bv_cstmr.gif)
5. Right-click the **Customers** category and select **New Category** from the shortcut menu to create a sub category **Address** in it, which we want to use to hold address information.
6. From the Customers table in the Resource Objects panel, select **Address1**, **Customers\_Country**, **Customer Name**, and **Customers\_Phone** and drag them into the Address category.

When adding elements to a business view by dragging DBFields from the Resource Objects panel, Designer uses the elements as Group object by default. Next, we want to edit the type of the elements in the Address category to Detail, so that we can use them to show detail information in reports.

1. Select the four elements in the **Address** category, right-click them and select **Edit** on the shortcut menu. In the Edit View Element dialog box, select **Detail** from the **Type** drop-down list and select **OK** (using the dialog box, you can edit the Type, Tip, and Description properties of multiple view elements at the same time).

   ![Edit View Element](https://devnet.logianalytics.com/hc/article_attachments/4404880710167/bv_edtvw.gif)

   The Address category now contains four detail objects as follows:

   ![Address Category](https://devnet.logianalytics.com/hc/article_attachments/4404880710423/bv_adrs.gif)

By now, we have finished creating the Customers category with the Address sub category. Next, let's create the Orders Detail category.

1. Select **WorldWideSalesBV** in the Business View panel.
2. Select **New Category** on the toolbar to create a category **Orders Detail**.
3. Add the following fields from the Resource Objects panel into the category: all the fields in the **Orders** and **Orders Detail** tables, and **Cost** in the **Products** table.
4. Right-click **Orders\_Order ID** and select **Rename** from the shortcut menu to edit its display name to **Order ID**.
5. Edit the type of Cost, Discount, Order Date, Quantity, and Unit Price to Detail using the Edit View Element dialog box [as shown above](#EditType).

   The Order Detail category shows as follows:

   ![Define the Orders Detail Category](https://devnet.logianalytics.com/hc/article_attachments/4404880710679/bv_order1.gif)

You can also add view elements to a business view by using dialog box in addition to dragging and dropping. Next, we add more elements to the Orders Detail category via dialog box.

1. Select the **Orders Detail** category and select **New Detail** on the toolbar.
2. In the New View Element dialog box, select the **ellipsis** button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404880710935/btn_chsr.gif) next to the **Mapping Name** text box. In the View Element Resources dialog box, expand the **Formulas** node and double-click **Total** to add it as the mapping field. Select **OK** to create the element.

   ![Add Total as Element](https://devnet.logianalytics.com/hc/article_attachments/4404880711191/bv_total.gif)
3. Select the **Orders Detail** category again, right-click it and select **New View Element** from the shortcut menu.
4. In the New View Element dialog box, type **Total Cost** in the **Display Name** text box, select ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404880710935/btn_chsr.gif) and select **Cost** in the **Products** table as the mapping field, select **Aggregation** from the **Type** drop-down list, then select **Sum** from the **Aggregate Function** drop-down list. Select **OK** to create the aggregation.

   ![Create Cost Aggregation](https://devnet.logianalytics.com/hc/article_attachments/4404880711447/bv_cost.gif)
5. Create another two aggregations **Total Quantity** which sums on **Quantity** and **Total Sales** which sums on the formula **Total** using the same way.

   The Orders Detail category now contains the following elements:

   ![Arrange the Orders Detail Category](https://devnet.logianalytics.com/hc/article_attachments/4404880711959/bv_order2.gif)

Next, we create the Products category to hold product related information.

1. Select **WorldWideSalesBV** in the Business View panel and select **New Category** on the toolbar to create a category **Products**.
2. Drag **Category**, **Product Name**, **Product Type Name**, and **Products\_Product ID** from the **Products** table in the Resource Objects panel to the Product category.
3. Right-click **Product Type Name** and select **Rename** from the shortcut menu to edit its display name to **Product Type**.

   ![Create the Products Category](https://devnet.logianalytics.com/hc/article_attachments/4404880712215/bv_prdct.gif)
4. Select the **Sort** icon ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404880712471/btn_sort.gif) at the upper right corner of the Business View panel and select **Ascending** from the drop-down menu to sort the elements that we have added to the business view in the ascending order.
5. Select **Save** on the toolbar to save the business view.

## Task 3: Define Hierarchies in the Business View

In this task, we define two hierarchies in the business view: one containing customer's geographic information, from region down to city, and the other containing product's hierarchical groups.

1. In the Business View Editor dialog box, select **WorldWideSalesBV** in the Business View panel, then select **New Hierarchy** on the toolbar.
2. In the New Hierarchy dialog box, type **Geography** and select **OK**. Designer then adds the Geography hierarchy node at the bottom under the business view root node.
3. In the Business View panel, drag the group objects **Region**, **Territory**, **Country**, **State**, and **City** from the **Customers** category one by one following this order to the Geography hierarchy node. Region is the highest level and City the lowest.
4. Follow the above steps to create another hierarchy **Product** and add **Product Type**, **Category**, and **Product Name** in the **Products** category to this hierarchy.

   The two hierarchies show as follows in the Business View panel:

   ![Create Hierarchies](https://devnet.logianalytics.com/hc/article_attachments/4404880712727/bv_hrchy.gif)
5. Save the business view to save the hierarchies, then close the Business View Editor dialog box.
6. Select **Save Catalog** on the Catalog Manager toolbar to save the business view into the catalog.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404885299607/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009770141-Lesson-9-Creating-a-Parameter-Based-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880128919/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009742382-Track-3-Creating-Web-Reports)
