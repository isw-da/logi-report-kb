---
title: "Maintaining Catalogs with the Catalog Doctor"
id: 1500010028562
section: "Creating and Managing Catalogs - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010028562-Maintaining-Catalogs-with-the-Catalog-Doctor
updated_at: 2021-07-24T10:39:32Z
---

# Maintaining Catalogs with the Catalog Doctor

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028542-Merging-Catalogs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections)

# Maintaining Catalogs with the Catalog Doctor

Logi JReport Designer provides the Catalog Doctor for you to maintain catalogs and diagnose problems with catalogs. This topic shows how to use the Catalog Doctor to diagnose the specific resources of catalogs: connections, tables and fields, formulas and summaries, and queries.

Below is a list of the sections covered in this topic:

* [Errors the Catalog Doctor Can Detect](#Error)
* [Starting the Catalog Doctor](#Start)
* [Diagnosing and Fixing Problems](#Fix)
  + [For Connections](#Connection)
  + [For Tables and Fields](#Table)
  + [For Formulas and Summaries](#Formula)
  + [For Queries](#Query)
* [Merging Catalogs](#Merge)

## Errors the Catalog Doctor Can Detect

With the Catalog Doctor you can diagnose and validate data resources in a catalog. Since the data resources in a catalog are constructed independently from each other, the Catalog Doctor diagnoses each type of data resource independently. For example, when it checks formulas, it only looks into the definition of parameters and DBFields in the current catalog, and does not check whether the DBFields exist in the connected database; when it checks queries, it only looks for the mapping fields which are currently in the catalog, and does not confirm whether the formulas are valid.

For your convenience, in the following statements database refers to a raw database connected via JDBC, mapped table/view/synonym refers to a table/view/synonym in a catalog, raw table/view/synonym refers to a table/view/synonym in a raw database, and raw column refers to the columns in a raw database.

**Mapped table/view/synonym and DBField**

* Checks whether the raw table/view/synonym of a mapped table/view/synonym exists in the database.
* Checks whether the raw column of a DBField exists in the database. If it exists, then it checks to see whether the stored information such as SQL Date type matches the raw column in the database.

**Formulas and summaries**

* Checks to see whether the formulas and summaries have correct syntax. It checks whether the remapped parameters and DBFields need to be remapped again.

**Queries**

* Checks whether the data resources referenced by the query exist in the catalog.
* Checks whether or not the data resources are valid.
  + Whether the DBFields of the data resources match those saved in the query.
  + Whether or not the formulas and parameters can be found in the catalog.

## Starting the Catalog Doctor

To start the Catalog Doctor, run the batch file named CatDr.bat or CatDr.sh on Unix/Linux in the `<install_root>\bin` directory.

You can also start it by issuing the following commands from an MS-DOS command prompt:

`>cd c:\jreport\designer\bin  
 c:\jreport\designer\bin\>catdr`

## Diagnosing and Fixing Problems

After the Catalog Doctor is started, you can select **File** > **Open** to open the catalog you want to diagnose. All the resources in the specified catalog will then be listed in the left panel of the Catalog Doctor window. Select a resource from the resource tree. In the right panel, you will see the information of the selected resource.

You should diagnose the resources in the following order: connection > table and field > formula and summary > query.

### For Connections

The Catalog Doctor can be used to diagnose connections in the following aspects:

* **Finding information of the current connection**  
   Select a connection from the resource tree. The connection information will be displayed in the left panel.
* **Modifying the current connection**  
  Right-click the connection in the resource tree, and then select **Modify** on the shortcut menu. The Get JDBC Connection Information dialog will appear. You can now modify the connection.

  For a JDBC driver, fill in the class name of the driver, the URL, user ID and password (if necessary).

  For a JDBC-ODBC bridge, uncheck the **Driver**  checkbox and check **Use ODBC Data Source**, then give the ODBC data source name, and the user ID and password (if necessary).

  You can also change the properties values in the Properties sheet directly. Select a property value, and then choose or type in the value.

  **Note:** The JDBC-ODBC bridge is no longer included with Java for JDK 8 or later. To solve this issue, you need to add the path information of the ODBC-JDBC bridge to the class path during installation or by editing the setenv.bat (setenv.sh on Unix/Linux) file in `<install_root>\bin`.

### For Tables and Fields

The Catalog Doctor can be used to diagnose tables and fields in the following aspects:

* **Finding all the mapping tables, views, synonyms and DBFields in the catalog**  
   In the resource tree, expand the connection node, then go to the **Tables**, **Views** or **Synonyms** node and reveal it. All the mapping tables, views, synonyms and DBFields in the catalog will then be listed. The icon in front of each object has a specific meaning, which indicates whether the object is valid or not.  

  The following are descriptions of the icons in front of each object:

  ![Table button](https://devnet.logianalytics.com/hc/article_attachments/4404901346071/ctlg_mntn_tblfld1.gif): Table

  ![Table not existing button](https://devnet.logianalytics.com/hc/article_attachments/4404909292823/ctlg_mntn_tblfld2.gif): Table which does not exist in the database

  ![Table with invalid field button](https://devnet.logianalytics.com/hc/article_attachments/4404901346327/ctlg_mntn_tblfld3.gif): Table which has invalid fields

  ![View button](https://devnet.logianalytics.com/hc/article_attachments/4404901346583/ctlg_mntn_tblfld4.gif): View

  ![View not existing button](https://devnet.logianalytics.com/hc/article_attachments/4404909293079/ctlg_mntn_tblfld5.gif): View which does not exist in the database

  ![View with invalid field button](https://devnet.logianalytics.com/hc/article_attachments/4404909293335/ctlg_mntn_tblfld6.gif): View which has invalid fields

  ![Synonym button](https://devnet.logianalytics.com/hc/article_attachments/4404909293591/ctlg_mntn_tblfld10.gif): Synonym

  ![Field button](https://devnet.logianalytics.com/hc/article_attachments/4404901346839/ctlg_mntn_tblfld7.gif): Field

  ![Field not existing button](https://devnet.logianalytics.com/hc/article_attachments/4404901347095/ctlg_mntn_tblfld8.gif): Field which does not exist

  ![Field type mismatch button](https://devnet.logianalytics.com/hc/article_attachments/4404909293847/ctlg_mntn_tblfld9.gif): Field with a name which can be found in the database, but has a type mismatch.
* **Finding the stored information of a mapping table/view/synonym or a DBField**  
   Select a table/view/synonym or a DBField in the resource tree to find its stored properties. The information will be listed in the Properties sheet.
* **Finding all the raw tables/views/synonyms**  
   Select a table/view/synonym in the Tables/Views/Synonyms node. All the raw tables/views/synonyms will be shown in the Choose from following to re-map panel. Each item there shows the name of a table/view/synonym.
* **Getting the raw columns in a raw table/view/synonym**  
   First select a mapping table/view/synonym, then choose a raw table/view/synonym from the Choose from following to re-map panel. The raw columns will be shown in the bottom panel.

  **Note:** If you select a mapping table/view/synonym with an existing raw table/view/synonym, the raw table/view/synonym will automatically be selected.
* **Deleting a set of mapping tables, views, synonyms or DBFields**  
   To delete the mapping object, you can use one of the following methods:
  + Select an object from the resources tree, right-click and on the shortcut menu select **Delete**.
  + Select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404901170455/btn_delete.gif) on the toolbar after selecting the object.
  + Select the object and press **Delete** on your keyboard.

  To delete a set of mapping tables, views, synonyms or DBFields, select the objects you want to delete, and select ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404901170455/btn_delete.gif) on the toolbar (or press **Delete** on your keyboard).
* **Re-mapping (Updating) a mapping table/view/synonym**  
   First select the mapping table/view/synonym that is to be updated from the resource tree. Then, select the raw table/view/synonym which the mapping table/view/synonym refers to from the Choose from following to re-map panel, and select the **Update** button ![Update button](https://devnet.logianalytics.com/hc/article_attachments/4404909294103/ctlg_mntn_updtbtn.gif) on the toolbar.

  **Note:** The tree is sorted by the validation status of each object (invalid objects are listed ahead). So, after you have updated a mapping table/view/synonym, the order of the objects will probably change. If the table was invalid and becomes valid after updating, it will be listed after the invalid objects.
* **Re-mapping (Updating) a DBField**   
   Before updating a DBField, you must make sure that the mapping table/view/synonym of the DBField is valid. That is, the raw table/view/synonym that the mapping table/view/synonym refers to exists in the database.

  Select the DBField you want to update from the resource tree, choose the raw column you want the DBField to refer to in the bottom right panel, and then select the Update button on the toolbar.
* **Adding tables/views/synonyms**  
   select the **Add Table** button ![Add Table button](https://devnet.logianalytics.com/hc/article_attachments/4404909294359/btn_addtbl.gif)， the **Add View** button ![Add View button](https://devnet.logianalytics.com/hc/article_attachments/4404909294615/btn_addview.gif)，or the Add Synonym button ![Add Synonym button](https://devnet.logianalytics.com/hc/article_attachments/4404909294871/btn_addsynym.gif) on the toolbar, or right-click the Tables, Views, or Synonyms node, or a table, view or synonym and select **Add Table**, **Add View** or **Add Synonym** from the shortcut menu. In the Add Table/View/synonym dialog, select the tables/views/synonyms you would like to add, and select **Add**. To finish adding, select **Done**.
* **Adding a DBField**  
   Select a table or a synonym from the resource tree, right-click and on the shortcut menu select **Insert Column** to bring out the Add Column dialog. Then select the column you want and select **Add**. When you have finished adding columns, select **Done** to close the dialog.

### For Formulas and Summaries

The Catalog Doctor can be used to diagnose formulas and summaries in the following aspects:

* **Finding all the formulas and summaries in the catalog**  
   Expand the Formulas and Summaries node on the resources tree. The formulas and summaries in the catalog will be listed in the tree. They will be sorted by their validity and names. If the icon of a formula/summary is marked by a cross, it means it is invalid (it fails on compiling).
* **Finding the compile Error message of a formula/summary**  
   Select the formula/summary that is to be checked. The compile error messages will then be displayed in the Error panel.
* **Replacing a mapping field with another in formulas and summaries**  
   A frequent error is caused when the mapping fields are not found in a catalog. In which case, you will need to replace the mapped field in formulas/summaries with a valid one.
  1. Select the formula/summary that contains unknown fields in the resource tree.
  2. Select the **Replace All** button in the Error panel. The Replace dialog appears.
  3. Input the field name that is to be replaced in the Mapping Name text box.
  4. Select the **Browse** button, the Mapping Fields Browse dialog appears.
  5. In the Tree View tab, you can select an existing field to replace the unknown field.
  6. In the List View tab, you will see the mapping fields in alphabetical order and the type for each mapping field. If the mapping field is a DBField, you will see the tables/views/synonyms it belongs to. Select the field you want to use as a replacement and select **OK**.
  7. Select the **Replace** button in the Replace dialog.
* **Editing a formula/summaries**  
   Select the formula/summary to be edited, and select the **Edit** button in the Error panel.
* **Removing formulas/summaries**  
   Select the formulas/summaries that are to be removed, then, do one of the following:
  + Right-click and on the shortcut menu, select **Delete**.
  + Select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404901170455/btn_delete.gif) on the toolbar.
  + Press the **Delete** key on your keyboard.

### For Queries

The Catalog Doctor can be used to diagnose queries in the following aspects:

* **Finding all the queries in the catalog**  
   Expand the Queries node in a data source. All the queries will be listed in the resources tree.
* **Finding the data resources selected in a query**  
   Expand a query. All the data resources will be listed.
* **Finding the DBFields selected from a data resource in a query**   
   Expand a data resource in a query. All the DBFields in the data resource will be listed.
* **Finding the formulas or computed columns in a query**  
   Formulas and computed columns are listed in a query if there are.
* **Editing a query**  
   Select the query that is to be edited, and select the **Edit** button in the Error panel (or right-click the query, and select **Edit Query** from the shortcut menu).
* **Deleting queries, DBFields, formulas, computed columns and a data resource selected in a query**  
   To delete the object, you can use one of the following methods:
  + Select an object from the resources tree, right-click and on the shortcut menu select **Delete**.
  + Select the **Delete** button ![Delete button](https://devnet.logianalytics.com/hc/article_attachments/4404901170455/btn_delete.gif) on the toolbar after selecting the object.
  + Select the object and press **Delete** on your keyboard.
* **Creating cached query result** **for a query**  
   Select the query and select **Run** (or right-click the query, and select **Create Cached Query Result** on the shortcut menu). Then in the Save Cached Query Result dialog, specify the file name with or without an extension and the folder where you want to save the result file and then select **Save**. For detailed usage of cached query results, see [Cached Query Results](https://devnet.logianalytics.com/hc/en-us/articles/1500010034602-Cached-Query-Results).

## Merging Catalogs

With the Catalog Doctor, you can also merge the resources from two catalogs into one. However, before merging, you need to first specify at which level the differences between these two catalogs will be checked by the Catalog Doctor.

**To specify the checking level:**

1. Select **File** > **Options** to display the Options dialog.

   ![Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901347351/ctlg_mntn_optn.gif)
2. In the Merge Catalog Options box, specify the checking level.
   * **Identify all differences**  
      The Catalog Doctor will check for differences between the two catalogs. All the resources of the report are displayed in the Merge dialog with all conflicting resources marked.
   * **Identify critical differences**  
      The Catalog Doctor will check for any differences that may cause the engine to fail to run a report. All the resources of the report are displayed in the Merge dialog with any critical conflicting resources marked.
   * **Ignore differences**  
      Does not show the differences between the two catalogs. Any conflicts will remain in the target catalog.
3. Select **OK** to accept the setting.

With the checking level specified, you can then start to merge catalogs.

**To merge catalogs:**

1. Open the target catalog in the Catalog Doctor.
2. Select **File** > **Import**, and then select the catalog that is to be imported. The Import from Catalog dialog appears.

   ![Import from Catalog dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901347607/ctlg_mntn_impt.gif)
3. Select the resources from the catalog and select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901120791/btn_addarrow.gif) to add it to the Imported node, then select **OK**.
4. If you specified the checking level as Identify All Differences or Identify Critical Differences and the selected resources conflict with those in the target catalog, the Merge dialog appears for dealing with conflicting resources. The conflicting resources will be marked with red question marks.

   ![Merge dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901199511/merge.gif)
5. Select the **Rename** button to rename, or the **Replace** button to replace. You can also select the **Skip** button to skip.
6. Select the **Differences** button to see the property values of the objects in the target catalog and the sources catalogs. Different property values will be highlighted.
7. Select the **Target Relation** button to see the relationship between the object and its parent node.
8. Repeat the steps above to manage conflicting resources, and then select the **Merge** button to merge the two catalogs. If the connections in the two catalogs connect to different data sources, you will be asked to modify the existing data source in the target catalog. For safety purposes, it is better to create a new data source.
9. Select **File** > **Save** to save the changes and exit the Catalog Doctor.
10. Launch Logi JReport Designer, and open the merged catalog. The resources you just imported are now available and new data sources have been created.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010028542-Merging-Catalogs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010029402-Data-Source-Connections)
