# Design API

The Design API creates and edits report templates and library components from Java: report
sets, report tabs, tables, crosstabs, charts, DBFields, formulas, labels, images, groups,
filters and properties. It is what you use when a report must be generated rather than
drawn.

Primary source: [Using Design API to Design Reports (Designer v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735520110743-using-design-api-to-design-reports.md).
The server guide's [short version](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741386010903-using-design-api-to-design-reports.md)
defers to the Designer guide. Era: `logi-report-v17-v19`.

## Two packages and two licences

There is a workstation package (Design API) and a server package (Server Design API).
Designer's copy is single threaded; the server's copy is multithreaded.

The behavioural difference: methods that edit catalogs, queries, reports and parameters
take an extra leading UID parameter in the Server Design API, and do not in the Design API.

The licences are independent of every other Logi Report licence and are not
interchangeable. Which key you need follows from where your classpath points at run time:
`<server_install_root>\lib` needs the Server Design API key, `<designer_install_root>\lib`
needs the Design API key. The licence is applied to your program, not to the installation.

Source: [Design API Packages and License (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735526718103-design-api-packages-and-license.md).

## Installing

From Designer, `<designer_install_root>\lib` gives you `JREngine.jar`, `report.jar`,
`sac-1.3.jar` and the log4j and slf4j jars. Put `JREngine.jar` ahead of `report.jar` on
the classpath, add your JDBC driver jars, set `-Dreporthome` to the Designer root, and
register the licensed user and key in source. The article also covers installing from the
server and installing the two independent packages with no other Logi Report product
present.

Source: [Installing the Design API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735520121111-installing-the-design-api.md).

## Preparations: licence, catalog, handles

```java
DesignerUserInfo userInfo = new DesignerUserInfo(Uid, key);
Designer desg = new Designer(catalogPath, catalogName, userInfo);          // page report
MultipliedDesigner md = new MultipliedDesigner(path, catName, Designer.CAT, userInfo); // web report
```

`setUserInfo(String uid, String key)` sets the licence and must be called before any other
Design API method. `getCatalogAPI()` returns the [Catalog API](catalog-api.md) instance for
the catalog the reports will be saved into.

Everything else runs on handles. The Design API identifies every node and object in the
report tree by a HANDLE string, and the super class `API` provides:

- `getHandles()` returns every handle in the report
- `getHandles(String handle)` returns the child handles of a node
- `getHandles(String handle, int type)` returns child handles of one type
- `getHandles(String handle, int type, int depth)` adds a depth limit, where -1 is the
  whole report, 0 is the current level, and n is n levels plus the current one
- `getParent(String handle)` returns the parent handle

Source: [Making Preparations Before Using the Design API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735563463191-making-preparations-before-using-the-design-api.md).

## Class hierarchy

`API` is the root abstract class of the hierarchy and holds the editing methods. `Designer`
is the principal class that manipulates reports, and its super class is `API`. Reports must
be created against an existing catalog file, otherwise you get an error.

## Methods the corpus names

From [Designing Reports with the Design API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735511592855-designing-reports-with-the-design-api.md).

**Report lifecycle**

- `createReportSet(String name)` new page report
- `addReport(String reportsetHandle, String name)` new report tab in a page report
- `createWebReportSet(String reportsetName, String reportTabName)` new web report, which
  gets a report tab automatically
- `open(String name)`, `close(String handle)`, `closeReportSet()`, `quit(String handle)`
  (closes without saving), `deleteReport(String name)`

**Objects in a report**

- `insert(String parent, int type, String name)` generic object
- `insert(String parent, int type, String name, String mapping)` DBField, parameter,
  formula or summary
- `insertTable(String parent, TableTemplateInfo info, boolean increasePanel)`
- `insert(String parent, String name, CTRowColFieldInfo colInfo[], CTRowColFieldInfo rowInfo[], CTAggFieldInfo aggInfo[])` crosstab with children
- `insert(String parent, CTRowColFieldInfo colInfo, CTRowColFieldInfo rowInfo, CTAggFieldInfo aggInfo)` crosstab children into an existing crosstab
- `insert(String parent, String name, String paperName, int charttype, String gName1, String gName2, String value, ChartLegendInfo, ChartLabelInfo)` chart with children
- `insert(String parent, int type, String name, String topSection, String bottomSection)` drawing object
- `insert(String parent, String name, GroupInfo groupInfo)` group or sort
- `changeZOrder(String objectHandle, int zorderType)`, `delete(String handle)`

**Dynamic formulas and aggregations**

- `addDynamicFormula(String reportHandle, String datasetHandle, String formulaName, String expression, int useType, boolean isRawExpression)`
- `addDynamicAggregation(String reportHandle, String datasetHandle, String aggregationName, String basedFieldName, String function)`
- `modifyDynamicFormula(String formulaHandle, FormulaInfo formulaInfo, int useType, boolean isRawExpression)`
- `modifyDynamicAggregation(String aggHandle, BVAggregationInfo aggInfo)`
- `compileDynamicFormulas(String objHandle)`, which compiles every dynamic formula in the
  report when passed a report handle

The article's later sections cover getting and setting object properties, report metadata,
object information, filters, editing information, library components and exiting the
editing status.

## Worked example: read a catalog's connection details

The corpus's own starter example compiles and runs `TellMeConnection.java` from
`<install_root>\help\samples\APICatalog`:

```
javac -classpath <install_root>\lib\JREngine.jar;<install_root>\lib\sac-1.3.jar;<install_root>\lib\report.jar TellMeConnection.java

java -classpath "...;<install_root>\lib\JREngine.jar;<install_root>\lib\report.jar;<install_root>\lib\sac-1.3.jar;..." -Dreporthome=<install_root> TellMeConnection -path=<catalog_path> -catalog=<catalog_name>
```

Set the key with `dr.setUserInfo("UID","XXXXXXXXXXX")` inside the sample first. Output is
the connection name, driver, JDBC URL, user, and the timestamp, time and date formats.

Source: [Getting Started Using the Design API (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735526762007-getting-started-using-the-design-api.md).
More samples: [Running the Design API Samples (v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735498221463-running-the-design-api-samples.md).

## Exit functions are a different thing

Designer provides three exit functions, After Init Parameter, After Run and Before Run,
which return a status that tells the engine whether to keep running. They hook the run,
they do not design anything. See
[Exit Functions (Server v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-server-v19/5741394590743-exit-functions.md)
and [Using the Exit Functions (Designer v19)](../docs/logi-report-v17-v19/working-with-apis-logi-report-designer-v19/5735563519639-using-the-exit-functions.md).

## Era note

The v15 Logi JReport documentation splits the same material across many short articles,
beginning at [Logi JReport Design API](../docs/jreport-v15-v16/working-with-apis-logi-jreport-designer-v15/1500009562342-logi-jreport-design-api.md)
and [Design API Packages and License](../docs/jreport-v15-v16/working-with-apis-logi-jreport-designer-v15/1500009582741-design-api-packages-license.md).
The two-package, two-licence split is present in both eras. Whether individual method
signatures changed across the rename cannot be determined from this corpus, since neither
era ships the Javadoc.
