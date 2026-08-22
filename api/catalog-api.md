# Catalog API

The Catalog API builds and edits catalogs in code instead of through the Designer GUI:
connections, tables, queries, business views, formulas, parameters, WHERE portions and
user-defined data sources. Combine it with the [Design API](design-api.md) to produce a
whole report from Java.

Primary source: [Using Catalog API to Manipulate Catalogs (Designer v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735511547799-using-catalog-api-to-manipulate-catalogs.md).
The server guide carries a shorter version, [Using Catalog API to Manage Catalogs (Server v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741381190423-using-catalog-api-to-manage-catalogs.md),
which defers to the Designer guide for detail. Era: `logi-report-v17-v19`.

## Two classes, split at v13.5

- `jet.api.CatalogAPI` for catalogs created before v13.5.
- `jet.api.MultipliedCatalogAPI` for catalogs created since v13.5.

The catalog structure changed enough at v13.5 that the original class could not cover it,
so the second set extends and enhances the first. Both v15 and v19 documentation state
this split, so it predates the rename and is not an era difference. The method reference
below comes from the article on the original `jet.api.CatalogAPI` class; the corpus does
not give an equivalent method-by-method listing for `MultipliedCatalogAPI`.

Sources: the two articles above, plus the v15 [Logi JReport Catalog API](../docs/jreport-v15-v16/working-with-apis-logi-jreport-designer-v15/1500009582561-logi-jreport-catalog-api.md).

## Getting an instance

The Catalog API hangs off a Design API `Designer` object.

```java
DesignerUserInfo userInfo = new DesignerUserInfo(Uid, key);
Designer desg = new Designer(catalogPath, catalogName, userInfo);
CatalogAPI catalog = desg.getCatalogAPI();
```

`Designer(String path, String name, DesignerUserInfo user)` takes the catalog path, the
catalog name and the licensed user. The path must be an existing directory. The name is
an existing catalog to open one, or a new name to create one, in which case the directory
must not already hold a catalog file.

Source: [Making Preparations Before Using the Catalog API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735526662551-making-preparations-before-using-the-catalog-api.md).

## Installing

Installed with Designer. The class lives in `report.jar`. Three steps before you can
compile and run:

1. Set CLASSPATH with `JREngine.jar` **before** `report.jar`, plus `sac-1.3.jar`,
   `log4j-api`, `log4j-core`, `log4j-slf4j-impl` and `slf4j-api`.
2. Set the licensed user and Design API key in code:
   `DesignerUserInfo userInfo = new DesignerUserInfo("UID","Design API Key");`
3. Set `reporthome` to the Designer root, in the environment or as `-Dreporthome`.

The server also ships the Catalog API. If you take the classes from
`<server_install_root>\lib\JRESServlets.jar` instead of `report.jar`, you must use the
Server Design API key rather than the Design API key.

Source: [Installing the Catalog API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735526648855-installing-the-catalog-api.md).

## Methods the corpus names

From [Manipulating Catalogs with the Catalog API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735506431639-manipulating-catalogs-with-the-catalog-api.md).
Most creation methods are overloads of `insert` and return the handle of the new object,
or null on failure.

**Connections**

- `insert(boolean bUseJDBCODBCBridge, String name, String desc, String url, String driver)`
- `insert(boolean bUseJDBCODBCBridge, String name, String desc, String url, String driver, ConnectionInfo info)`
- the same two with a leading `String dataSourceName`
- `insertJSONConnection(String dataSourceName, String connectionName, String desc, JSONSchemaURIInfo jsonSchemaURIInfo, JSONInstanceURIInfo jsonInstURIInfo, boolean withAllTables)`

**Tables, views, synonyms**

- `insert(String catalogName, String schemaPattern, String tableName, int type)`
- `insert(String catalogName, String schemaPattern, String tablePattern, int type, boolean setMappingName)`

**Stored procedures**

- `insert(String procName, String catalog, String schema, String name, String remarks, int iType)`

**SQL files**

- `insert(String SQLName, String filename)`
- `insertSql(String dataSourceName, String SQLName, String filename)`

**User-defined data sources**

- `insert(String strDSName, String strClassName, String strParameter, UDSColumnInfo udsColInfo)`
- the same with a leading `String dataSourceName`

**Queries**

- `insert(String qryName, QueryFieldInfo, QueryJoinInfo, QueryQBEInfo, QueryAndInfo)`
- the same with a leading `String dataSourceName`

**Modifying a query** (all return boolean)

- tables: `set(String dataSourceName, String qryName, String tablename, String columnname, boolean isFormula)` and `deleteQueryTable(...)`
- fields: the same `set(...)` and `deleteQueryField(String dataSourceName, String qryName, String tablename, String columnname)`
- joins: `set(String dataSourceName, String qryName, String tableFrom, String columnFrom, String operator, String tableTo, String columnTo, boolean isSQL92, int outerJoin)` and `deleteQueryJoin(...)`
- QBE conditions: `setQBE(String dataSourceName, String qryName, String tablename, String columnname, String expression)` and `deleteQBE(...)`
- WHERE conditions: `setCondition(String dataSourceName, String qryName, String sExpression1, String sOperator, String sExpression2, String sLogic)` and `deleteCondition(...)`

The overload used to add a table and the one used to add a field are the same signature,
as printed in the source article. That is what the doc says; treat it with suspicion and
check against the Javadoc on a real install.

**Business views**

- `insertBusinessView(String dataSourceName, String queriableName, String businessViewName, boolean isLogicView=false)`

The article's remaining sections cover inserting a formula, summary, parameter or WHERE
portion, inserting, getting and deleting objects, refreshing the reference table, and
saving the catalog.

## Samples

`<install_root>\help\samples\APICatalog`. See
[Running the Catalog API Samples (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735520092695-running-the-catalog-api-samples.md).
The v15 set is split into one article per task, starting at
[Using the Catalog API (v15, Logi JReport)](../docs/jreport-v15-v16/working-with-apis-logi-jreport-designer-v15/1500009562182-using-the-catalog-api.md).

## Era note

Between the v15 and v19 sets the Catalog API's structure of documentation changed more
than the API did: v15 splits each operation into its own short article, v19 consolidates
them. The v13.5 catalog split is present in both. Whether individual method signatures
changed across the rename is not something this corpus lets me determine, because neither
era includes the Javadoc.
